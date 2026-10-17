# CaseHop Copilot Review Instructions

Review pull requests in this repository with emphasis on the following areas.
Findings should be concrete, severity-labelled, and include a suggested fix.

## Factual preservation (highest priority)

- Verify that must-preserve facts (especially order numbers such as `A-1847`) are
  compared by exact normalized set equality, never by substring or fuzzy match.
- Flag any code path that could silently repair, normalize, or coerce a model
  output before the check runs.
- Flag any place where a mutated fact could be reported as a pass.

## Cost and abuse controls

- Confirm the public deployment accepts only the prepared Case Pack and never
  arbitrary prompts or model IDs.
- Confirm rate limits, one global live-run semaphore, bounded concurrency, and
  the Backboard balance floor remain intact.
- Flag any change that could increase per-run cost or remove a guard.

## Privacy

- Confirm no raw support messages, raw model output, full prompts, secrets, or
  account balances appear in logs, errors, or responses.
- Confirm the Backboard key is used only server-side.

## Fallbacks and honesty

- Confirm fixture, recorded, and live evidence remain visibly distinct.
- Confirm a failed live run degrades to the prepared run without implying live
  evidence.
- Flag any change that hides unresolved human-review items or unverified cost.

## General

- Prefer the smallest change that fixes the issue.
- Do not suggest scope expansion, new services, or new dependencies.
- Treat the locked handoff (`docs/HANDOFF.md`) as the source of truth.
