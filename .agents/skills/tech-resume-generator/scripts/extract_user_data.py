#!/usr/bin/env python3
"""Extract text and file inventories from a career-materials folder.

Usage (from inside the skill folder):
  python3 scripts/extract_user_data.py --help
  python3 scripts/extract_user_data.py \\
    --input ../../tech-resume-generator_files/user_professional_data \\
    --output ../../tech-resume-generator_files/user_professional_data/_extracted

From the repo / workspace root:
  python3 skills/tech-resume-generator/scripts/extract_user_data.py \\
    --input tech-resume-generator_files/user_professional_data \\
    --output tech-resume-generator_files/user_professional_data/_extracted

Writes:
  - text/          selectable PDF text and copied plaintext sources
  - images/        inventory of image files (agent may OCR/vision separately)
  - copies/        copies of structured sources (.md .txt .json .ts .csv)
  - renders/       optional PNG renders for low-text PDFs (needs poppler + Pillow)
  - manifest.json  index of everything processed

Requires: python3. Optional: poppler-utils (pdftotext, pdfinfo, pdftoppm), Pillow.
No network access. Non-interactive (all options via flags).
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

TEXT_EXTS = {".md", ".txt", ".json", ".ts", ".tsx", ".js", ".csv", ".yml", ".yaml", ".html"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".tif", ".tiff"}
PDF_EXTS = {".pdf"}
SKIP_DIR_NAMES = {"_extracted", "node_modules", ".git", "__pycache__"}
SKIP_FILE_NAMES = {".gitkeep", ".DS_Store"}

SLICE_HEIGHT = 1800
SLICE_OVERLAP = 120
RENDER_DPI = 110
LOW_TEXT_CHARS = 80


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def rel_key(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def safe_name(rel: str) -> str:
    return rel.replace("/", "__").replace(" ", "_")


def pdf_to_text(pdf_path: Path) -> str:
    if not have("pdftotext"):
        return "[pdftotext not installed — install poppler-utils or use agent vision]"
    result = run(["pdftotext", "-layout", str(pdf_path), "-"])
    if result.returncode != 0:
        return f"[pdftotext failed: {result.stderr.strip()}]"
    return result.stdout


def pdfinfo(pdf_path: Path) -> dict[str, str]:
    if not have("pdfinfo"):
        return {}
    result = run(["pdfinfo", str(pdf_path)])
    info: dict[str, str] = {}
    for line in result.stdout.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()
    return info


def render_pdf_to_png(pdf_path: Path, dest_prefix: Path, dpi: int = RENDER_DPI) -> list[Path]:
    if not have("pdftoppm"):
        return []
    dest_prefix.parent.mkdir(parents=True, exist_ok=True)
    result = run(
        [
            "pdftoppm",
            "-png",
            "-r",
            str(dpi),
            str(pdf_path),
            str(dest_prefix),
        ]
    )
    if result.returncode != 0:
        print(f"[pdftoppm failed] {pdf_path}: {result.stderr}", file=sys.stderr)
        return []
    return sorted(dest_prefix.parent.glob(dest_prefix.name + "*.png"))


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.name in SKIP_FILE_NAMES:
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        files.append(path)
    return files


def extract_pdfs(input_root: Path, out: Path) -> list[dict]:
    records = []
    text_dir = out / "text"
    render_dir = out / "renders"
    for pdf in [p for p in iter_files(input_root) if p.suffix.lower() in PDF_EXTS]:
        rel = rel_key(pdf, input_root)
        text = pdf_to_text(pdf)
        info = pdfinfo(pdf)
        dest = text_dir / (safe_name(rel) + ".txt")
        write_text(dest, text)
        record: dict = {
            "source": rel,
            "kind": "pdf",
            "pages": info.get("Pages"),
            "page_size": info.get("Page size"),
            "file_size_bytes": pdf.stat().st_size,
            "extracted_chars": len(text),
            "text_preview_ok": len(text.strip()) > 5,
            "text_path": str(dest.relative_to(out)),
        }
        if len(text.strip()) < LOW_TEXT_CHARS:
            renders = render_pdf_to_png(pdf, render_dir / safe_name(rel), dpi=140)
            record["renders"] = [str(p.relative_to(out)) for p in renders]
        records.append(record)
        print(f"pdf   {rel}: {len(text)} chars")
    return records


def copy_text_sources(input_root: Path, out: Path) -> list[dict]:
    records = []
    copies = out / "copies"
    for path in [p for p in iter_files(input_root) if p.suffix.lower() in TEXT_EXTS]:
        rel = rel_key(path, input_root)
        dest = copies / safe_name(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = path.read_text(encoding="utf-8", errors="replace")
        write_text(dest, content)
        records.append(
            {
                "source": rel,
                "kind": "text",
                "file_size_bytes": path.stat().st_size,
                "extracted_chars": len(content),
                "copy_path": str(dest.relative_to(out)),
            }
        )
        print(f"text  {rel}: {len(content)} chars")
    return records


def inventory_images(input_root: Path, out: Path) -> list[dict]:
    records = []
    listing = out / "images" / "inventory.json"
    images = [p for p in iter_files(input_root) if p.suffix.lower() in IMAGE_EXTS]
    for path in images:
        rel = rel_key(path, input_root)
        records.append(
            {
                "source": rel,
                "kind": "image",
                "file_size_bytes": path.stat().st_size,
                "absolute_hint": str(path.resolve()),
                "note": "Agent should read/OCR this image; not auto-converted to text.",
            }
        )
        print(f"img   {rel}")
    write_text(listing, json.dumps(records, indent=2))
    return records


def inventory_other(input_root: Path, known: set[str]) -> list[dict]:
    records = []
    for path in iter_files(input_root):
        rel = rel_key(path, input_root)
        if rel in known:
            continue
        records.append(
            {
                "source": rel,
                "kind": "unsupported",
                "extension": path.suffix.lower(),
                "file_size_bytes": path.stat().st_size,
                "note": (
                    "No bundled extractor for this format. "
                    "Agent should write scripts/extractors/<format>_extract.py, run it, and continue."
                ),
            }
        )
        print(f"other {rel} ({path.suffix})")
    return records


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="extract_user_data.py",
        description=(
            "Inventory and extract career files for tech-resume-generator. "
            "Writes text copies, PDF text, image inventory, and manifest.json."
        ),
        epilog=(
            "Examples:\n"
            "  python3 scripts/extract_user_data.py "
            "--input ../../tech-resume-generator_files/user_professional_data "
            "--output ../../tech-resume-generator_files/user_professional_data/_extracted\n"
            "  python3 scripts/extract_user_data.py --help\n"
            "Exit codes: 0 success, 1 missing input or fatal error."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("tech-resume-generator_files/user_professional_data"),
        help="Input folder (career materials). Default: tech-resume-generator_files/user_professional_data",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output folder (default: <input>/_extracted)",
    )
    args = parser.parse_args()
    input_root = args.input.resolve()
    out = (args.output or (args.input / "_extracted")).resolve()

    if not input_root.is_dir():
        print(
            f"Error: --input folder not found: {input_root}\n"
            f"Expected a directory of career files (PDF, md, images, etc.).",
            file=sys.stderr,
        )
        sys.exit(1)

    out.mkdir(parents=True, exist_ok=True)
    pdf_records = extract_pdfs(input_root, out)
    text_records = copy_text_sources(input_root, out)
    image_records = inventory_images(input_root, out)
    known = {r["source"] for r in pdf_records + text_records + image_records}
    other_records = inventory_other(input_root, known)

    manifest = {
        "input": str(input_root),
        "output": str(out),
        "pdfs": pdf_records,
        "text_sources": text_records,
        "images": image_records,
        "unsupported": other_records,
        "tools": {
            "pdftotext": have("pdftotext"),
            "pdfinfo": have("pdfinfo"),
            "pdftoppm": have("pdftoppm"),
        },
    }
    write_text(out / "manifest.json", json.dumps(manifest, indent=2))
    print(f"\nWrote manifest to {out / 'manifest.json'}")
    if other_records:
        print(
            f"Note: {len(other_records)} unsupported file(s) — agent should add extractors.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
