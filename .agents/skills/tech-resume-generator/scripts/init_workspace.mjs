#!/usr/bin/env node
/**
 * Create workspace-root tech-resume-generator_files/ with input/output subfolders + READMEs.
 *
 * Layout:
 *   tech-resume-generator_files/
 *     README.md
 *     user_professional_data/README.md
 *     job_description_data/README.md
 *     output/README.md
 *
 * Usage:
 *   node scripts/init_workspace.mjs
 *   node scripts/init_workspace.mjs --workspace /path/to/project
 *   node scripts/init_workspace.mjs --help
 *
 * Does not overwrite existing README.md files.
 */
import { copyFileSync, existsSync, mkdirSync, realpathSync, writeFileSync } from 'node:fs'
import { homedir } from 'node:os'
import { basename, dirname, join, resolve, sep } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const __dirname = dirname(fileURLToPath(import.meta.url))
const skillRoot = resolve(__dirname, '..')
const templatesDir = join(skillRoot, 'assets', 'templates')

const WORKSPACE_DIR = 'tech-resume-generator_files'
const SUBFOLDERS = [
  {
    name: 'user_professional_data',
    template: 'user_professional_data_README.md',
  },
  {
    name: 'job_description_data',
    template: 'job_description_data_README.md',
  },
  {
    name: 'output',
    template: 'output_README.md',
  },
]

const CLIENT_DIRS = new Set([
  '.agents',
  '.cursor',
  '.claude',
  '.codex',
  '.grok',
  '.gemini',
])

function printHelp() {
  console.log(`Usage: node scripts/init_workspace.mjs [--workspace <project-root>]

Creates <project-root>/${WORKSPACE_DIR}/ with:
  user_professional_data/  — career materials
  job_description_data/    — job postings (JD-tailored mode)
  output/                  — generated résumés

Examples (run from your project root after npx skills add):
  node .agents/skills/tech-resume-generator/scripts/init_workspace.mjs
  node .cursor/skills/tech-resume-generator/scripts/init_workspace.mjs
  node /path/to/skill/scripts/init_workspace.mjs --workspace .

Exit codes: 0 success, 1 error`)
}

function isGlobalClientRoot(clientDir) {
  const home = homedir()
  return CLIENT_DIRS.has(basename(clientDir)) && dirname(clientDir) === home
}

function projectRootFromSkillPath() {
  const skillsDir = resolve(skillRoot, '..')
  if (basename(skillsDir) !== 'skills') return null
  const clientDir = resolve(skillsDir, '..')
  if (!CLIENT_DIRS.has(basename(clientDir))) return null
  if (isGlobalClientRoot(clientDir)) return null
  return resolve(clientDir, '..')
}

function skillInstalledUnder(dir) {
  const markers = [
    join(dir, '.agents', 'skills', 'tech-resume-generator', 'SKILL.md'),
    join(dir, '.cursor', 'skills', 'tech-resume-generator', 'SKILL.md'),
    join(dir, '.claude', 'skills', 'tech-resume-generator', 'SKILL.md'),
    join(dir, '.codex', 'skills', 'tech-resume-generator', 'SKILL.md'),
    join(dir, '.grok', 'skills', 'tech-resume-generator', 'SKILL.md'),
  ]
  return markers.some((p) => existsSync(p))
}

function resolveWorkspace(argv) {
  const help = argv.includes('--help') || argv.includes('-h')
  if (help) return { help: true }

  const w = argv.indexOf('--workspace')
  if (w >= 0) {
    const value = argv[w + 1]
    if (!value || value.startsWith('-')) {
      throw new Error('--workspace requires a directory path')
    }
    return { root: resolve(value) }
  }

  const cwd = resolve(process.cwd())
  const fromSkill = projectRootFromSkillPath()

  if (skillInstalledUnder(cwd)) {
    return { root: cwd }
  }

  if (cwd === skillRoot || cwd.startsWith(skillRoot + sep)) {
    if (fromSkill) return { root: fromSkill }
    throw new Error(
      'This looks like a global skill install. Re-run from your project root, or pass --workspace /path/to/project',
    )
  }

  if (fromSkill) return { root: fromSkill }

  return { root: cwd, warn: 'Using current working directory as workspace root.' }
}

function ensureReadme(destReadme, templateName) {
  const templatePath = join(templatesDir, templateName)
  if (!existsSync(templatePath)) {
    throw new Error(`Missing template: ${templatePath}`)
  }
  if (existsSync(destReadme)) {
    console.log(`Already exists (left unchanged): ${destReadme}`)
    return
  }
  copyFileSync(templatePath, destReadme)
  console.log(`Created ${destReadme}`)
}

function initWorkspace(root) {
  const base = join(root, WORKSPACE_DIR)
  mkdirSync(base, { recursive: true })
  ensureReadme(join(base, 'README.md'), 'tech_resume_generator_files_README.md')

  for (const sub of SUBFOLDERS) {
    const dir = join(base, sub.name)
    mkdirSync(dir, { recursive: true })
    const gitkeep = join(dir, '.gitkeep')
    if (!existsSync(gitkeep)) writeFileSync(gitkeep, '')
    ensureReadme(join(dir, 'README.md'), sub.template)
  }

  console.log(`Workspace ready at: ${base}`)
  console.log('Add career files under user_professional_data/, JDs under job_description_data/, then run tech-resume-generator.')
}

const isDirectRun = (() => {
  if (!process.argv[1]) return false
  try {
    const argvPath = realpathSync(resolve(process.argv[1]))
    const selfPath = realpathSync(fileURLToPath(import.meta.url))
    return argvPath === selfPath
  } catch {
    return import.meta.url === pathToFileURL(resolve(process.argv[1])).href
  }
})()

if (isDirectRun) {
  try {
    const parsed = resolveWorkspace(process.argv.slice(2))
    if (parsed.help) {
      printHelp()
      process.exit(0)
    }
    if (parsed.warn) console.warn(`Warning: ${parsed.warn}`)
    initWorkspace(parsed.root)
  } catch (err) {
    console.error(`Error: ${err instanceof Error ? err.message : err}`)
    process.exit(1)
  }
}

export { initWorkspace, resolveWorkspace, skillRoot, WORKSPACE_DIR }
