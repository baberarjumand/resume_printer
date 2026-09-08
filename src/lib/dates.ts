import type { MonthYear } from '../types/resume.ts'

const MONTHS = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec',
] as const

const APOSTROPHE = '\u2019'
const EN_DASH = '\u2013'
const EM_DASH = '\u2014'

export function formatMonthYear(date: MonthYear): string {
  const month = MONTHS[date.month - 1]
  if (!month) {
    throw new Error(`Invalid month: ${date.month}`)
  }
  const year = String(date.year).slice(-2)
  return `${month} ${APOSTROPHE}${year}`
}

export function formatDateRange(
  start: MonthYear,
  end: MonthYear | 'Present',
): string {
  const startLabel = formatMonthYear(start)
  const endLabel = end === 'Present' ? 'Present' : formatMonthYear(end)
  return `${startLabel} ${EN_DASH} ${endLabel}`
}

export function formatYearRange(
  startYear: number,
  endYear: number | 'Present',
): string {
  if (endYear === 'Present') {
    return `${startYear} ${EN_DASH} Present`
  }
  if (startYear === endYear) {
    return String(startYear)
  }
  return `${startYear} ${EN_DASH} ${endYear}`
}

export function formatEducationYears(startYear: number, endYear: number): string {
  return `${startYear} - ${endYear}`
}

/** Brittany-style: Mar 2022 — Present */
export function formatDateRangeLong(
  start: MonthYear,
  end: MonthYear | 'Present',
): string {
  const month = MONTHS[start.month - 1]
  if (!month) {
    throw new Error(`Invalid month: ${start.month}`)
  }
  const startLabel = `${month} ${start.year}`
  if (end === 'Present') {
    return `${startLabel} ${EM_DASH} Present`
  }
  const endMonth = MONTHS[end.month - 1]
  if (!endMonth) {
    throw new Error(`Invalid month: ${end.month}`)
  }
  return `${startLabel} ${EM_DASH} ${endMonth} ${end.year}`
}
