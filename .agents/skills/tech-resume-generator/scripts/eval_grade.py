#!/usr/bin/env python3
"""Grade tech-resume-generator eval outputs against assertions.

Usage:
  python3 scripts/eval_grade.py \\
    --evals evals/evals.json \\
    --eval-id 1 \\
    --outputs /path/to/workspace/output \\
    --workspace /path/to/eval-run-dir

Writes grading.json to --workspace (default: stdout dir / grading.json).
Exit 0 if all assertions pass; 1 otherwise.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HELPED = re.compile(r"\b(helped|assisted|responsible for)\b", re.I)
# Metrics that must not appear unless present in Alex fixtures
FORBIDDEN_INVENTED = re.compile(
    r"(wcag|99%|kubernetes|k8s|\bacme\b.*(engineer|employee)|FAANG)",
    re.I,
)
STREET = re.compile(r"\b\d{1,5}\s+\w+\s+(st|street|ave|avenue|rd|road|blvd)\b", re.I)

REQUIRED_ROOT = ["meta", "header", "links", "skills", "experience", "education"]
REQUIRED_HEADER = ["name", "headline", "location", "phone", "email"]


def load_evals(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def find_json_resumes(output_dir: Path, sub: str | None = None) -> list[Path]:
    root = output_dir / sub if sub else output_dir
    if not root.exists():
        return []
    return sorted(p for p in root.rglob("*.json") if p.is_file())


def validate_schema(data: dict) -> list[str]:
    errors = []
    for key in REQUIRED_ROOT:
        if key not in data:
            errors.append(f"missing root.{key}")
    if "header" in data:
        for key in REQUIRED_HEADER:
            if key not in data["header"] or data["header"][key] in (None, ""):
                errors.append(f"missing header.{key}")
        for link_key in ("phone", "email"):
            obj = data["header"].get(link_key)
            if not isinstance(obj, dict) or "label" not in obj or "href" not in obj:
                errors.append(f"header.{link_key} must be {{label, href}}")
    if "links" in data and (not isinstance(data["links"], list) or len(data["links"]) == 0):
        errors.append("links must be non-empty array")
    if "experience" in data and not isinstance(data["experience"], list):
        errors.append("experience must be array")
    if "education" in data and not isinstance(data["education"], list):
        errors.append("education must be array")
    return errors


def blob(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False).lower()


def grade_case(case: dict, output_dir: Path, workspace: Path) -> dict:
    results = []
    pd = output_dir / "professional_data.md"
    general = find_json_resumes(output_dir, "general")
    tailored = find_json_resumes(output_dir, "tailored")
    any_resume = general + tailored + find_json_resumes(output_dir)
    # de-dupe
    seen = set()
    resumes = []
    for p in any_resume:
        if p.resolve() not in seen:
            seen.add(p.resolve())
            resumes.append(p)

    primary = None
    primary_data = None
    if resumes:
        # Prefer tailored for jd cases, else general
        slug = case.get("slug", "")
        if "jd" in slug or "tailored" in slug:
            pool = tailored or resumes
        else:
            pool = general or resumes
        primary = pool[0]
        try:
            primary_data = json.loads(primary.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            primary_data = None
            results.append(
                {
                    "text": "Resume JSON parses",
                    "passed": False,
                    "evidence": f"{primary}: {e}",
                }
            )

    def add(text: str, passed: bool, evidence: str) -> None:
        results.append({"text": text, "passed": passed, "evidence": evidence})

    for assertion in case.get("assertions", []):
        a = assertion.lower()
        if "professional_data.md exists" in a:
            ok = pd.is_file()
            name_ok = True
            if ok and "alex rivera" in a:
                name_ok = "alex rivera" in pd.read_text(encoding="utf-8").lower()
            if ok and "jordan lee" in a:
                name_ok = "jordan lee" in pd.read_text(encoding="utf-8").lower()
            add(assertion, ok and name_ok, f"exists={ok} name_match={name_ok} path={pd}")
        elif "json exists under output/general" in a:
            add(assertion, len(general) > 0, f"found={len(general)} files={general}")
        elif "json exists under output/tailored" in a:
            add(assertion, len(tailored) > 0, f"found={len(tailored)} files={tailored}")
        elif "json exists under output/general/ or output/tailored" in a:
            add(assertion, len(resumes) > 0, f"found={len(resumes)}")
        elif "validates against the generate_resume_pdf schema" in a:
            if not primary_data:
                add(assertion, False, "no resume JSON loaded")
            else:
                errs = validate_schema(primary_data)
                add(assertion, len(errs) == 0, "ok" if not errs else "; ".join(errs))
        elif "header name is alex rivera" in a:
            name = (primary_data or {}).get("header", {}).get("name", "")
            add(assertion, name == "Alex Rivera", f"name={name!r}")
        elif "skills section has 2" in a:
            skills = (primary_data or {}).get("skills") or []
            add(assertion, 2 <= len(skills) <= 3, f"count={len(skills)}")
        elif "cloudnine before pixelforge" in a or "newest-first" in a or "reverse-chronological" in a:
            exp = (primary_data or {}).get("experience") or []
            companies = [e.get("company", "").lower() for e in exp]
            if "cloudnine" in " ".join(companies) and "pixelforge" in " ".join(companies):
                i_c = next(i for i, c in enumerate(companies) if "cloudnine" in c)
                i_p = next(i for i, c in enumerate(companies) if "pixelforge" in c)
                add(assertion, i_c < i_p, f"order={companies}")
            else:
                # student case or missing — for newest-first just check list non-empty
                add(assertion, len(exp) > 0, f"companies={companies}")
        elif "state university only" in a:
            edu = (primary_data or {}).get("education") or []
            schools = [e.get("school", "") for e in edu]
            ok = any("State University" == s or "State University" in s for s in schools)
            bad = any("mit" in s.lower() or "stanford" in s.lower() for s in schools)
            add(assertion, ok and not bad, f"schools={schools}")
        elif "riverside community college" in a:
            edu = (primary_data or {}).get("education") or []
            blob_edu = json.dumps(edu).lower()
            add(assertion, "riverside" in blob_edu, f"education={edu}")
        elif "no street address" in a or "photo, or dob" in a:
            raw = blob(primary_data or {})
            has_street = bool(STREET.search(raw))
            has_dob = "dob" in raw or "date of birth" in raw
            add(assertion, not has_street and not has_dob, f"street={has_street} dob={has_dob}")
        elif "helped/assisted/responsible" in a:
            exp = (primary_data or {}).get("experience") or []
            text = " ".join(
                " ".join(job.get("bullets") or []) for job in exp
            )
            m = HELPED.search(text)
            add(assertion, m is None, f"match={m.group(0) if m else None}")
        elif "no metric appears that is absent" in a or "does not invent accessibility" in a:
            raw = blob(primary_data or {})
            # Allow fixture metrics; ban clear inventions
            bad = bool(re.search(r"wcag|aa\/aaa|100% accessible", raw))
            add(assertion, not bad, f"invented_a11y={bad}")
        elif "sibling pdf exists" in a:
            if not primary:
                add(assertion, False, "no json")
            else:
                pdf = primary.with_suffix(".pdf")
                add(assertion, pdf.is_file(), f"pdf={pdf} exists={pdf.is_file()}")
        elif "react and typescript" in a:
            raw = blob(primary_data or {})
            add(assertion, "react" in raw and "typescript" in raw, "checked skills/bullets blob")
        elif "does not claim employment at acme" in a:
            exp = (primary_data or {}).get("experience") or []
            companies = " ".join(e.get("company", "") for e in exp).lower()
            add(assertion, "acme" not in companies, f"companies={companies}")
        elif "alex's real links" in a or "header links remain" in a:
            links = (primary_data or {}).get("links") or []
            hrefs = " ".join(l.get("href", "") for l in links).lower()
            add(
                assertion,
                "alexrivera.dev" in hrefs or "github.com/alexrivera" in hrefs,
                f"hrefs={hrefs}",
            )
        elif "does not invent faang" in a:
            raw = blob(primary_data or {})
            bad = any(x in raw for x in ("google", "meta", "amazon", "apple", "netflix", "faang"))
            # allow if somehow in links only — still fail for student
            add(assertion, not bad, f"found_faangish={bad}")
        elif "expert/beginner" in a:
            raw = blob(primary_data or {})
            bad = bool(re.search(r"\b(expert|beginner|proficient|novice)\b", raw))
            add(assertion, not bad, f"proficiency_labels={bad}")
        else:
            add(assertion, False, "grader has no handler for this assertion — update eval_grade.py")

    passed = sum(1 for r in results if r["passed"])
    failed = sum(1 for r in results if not r["passed"])
    report = {
        "eval_id": case.get("id"),
        "slug": case.get("slug"),
        "assertion_results": results,
        "summary": {
            "passed": passed,
            "failed": failed,
            "total": len(results),
            "pass_rate": (passed / len(results)) if results else 0.0,
        },
        "primary_resume": str(primary) if primary else None,
    }
    workspace.mkdir(parents=True, exist_ok=True)
    out = workspace / "grading.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(f"Wrote {out}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Grade tech-resume-generator eval outputs")
    parser.add_argument("--evals", type=Path, required=True, help="Path to evals.json")
    parser.add_argument("--eval-id", type=int, required=True, help="Eval id from evals.json")
    parser.add_argument("--outputs", type=Path, required=True, help="Directory with professional_data.md and resumes")
    parser.add_argument("--workspace", type=Path, required=True, help="Where to write grading.json")
    args = parser.parse_args()

    data = load_evals(args.evals)
    case = next((e for e in data["evals"] if e["id"] == args.eval_id), None)
    if not case:
        print(f"Error: eval id {args.eval_id} not found", file=sys.stderr)
        sys.exit(1)

    report = grade_case(case, args.outputs.resolve(), args.workspace.resolve())
    sys.exit(0 if report["summary"]["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
