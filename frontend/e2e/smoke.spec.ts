import { test, expect } from '@playwright/test'

test('landing page renders CaseHop', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByText('CaseHop')).toBeVisible()
})
