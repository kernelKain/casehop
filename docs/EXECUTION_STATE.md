# CaseHop Execution State

This file records execution evidence according to `docs/HANDOFF.md` Section 13.
It is updated in the same atomic commit as the step it records.
Never record secrets, balances, tokens, raw prompts, raw model output, or transcripts.

## Current state

| Field | Value |
|---|---|
| Phase | Stack Foundation |
| Branch | `phase/stack-foundation` |
| Last verified step | SF-01 |
| Last commit hash | `a8a81e6` (SF-01) |
| Next action | SF-02 — verify and commit Entire configuration |

## Step log

### SF-01 — Establish locked handoffs and execution tracking

- **Status:** Complete
- **Phase branch:** `phase/stack-foundation`
- **Commit hash:** `a8a81e63d0fb09ff49539a02ded6f31091e733f0`
- **Files changed:** `.gitignore`, `docs/HANDOFF.md`, `docs/EXECUTION_STATE.md` (`docs/HANDOFF_0.md` verified, unchanged)
- **Acceptance criteria:** Contract preservation and resume policy; supports AC-17 — satisfied
- **Verification output:** `git diff --check` passed; `cmp docs/HANDOFF.md docs/HANDOFF_1.md` identical; HANDOFF_0.md product locks present; secret scan clean; working tree clean after commit.
- **Risks and decisions:** HANDOFF_1.md retained as source artifact. No secrets committed.
- **Time used:** unknown
- **Next action:** Complete (committed and verified).

### SF-02 — Configure development-session evidence

- **Status:** In progress
- **Phase branch:** `phase/stack-foundation`
- **Commit hash:** pending
- **Files changed:** `.entire/`, `.codex/hooks.json`, `.opencode/plugins/entire.ts`, `.github/copilot-instructions.md`
- **Acceptance criteria:** Supports AC-15 and conditional AC-16
- **Verification output:** `entire version` → Entire CLI 0.11.4; `entire checkpoint list` → 0 checkpoints (expected before first session); `entire doctor` → Codex/OpenCode hooks installed, OpenCode hook config OK, git hooks OK. Codex hook trust shows 7 hooks needing approval via `/hooks` in Codex (recorded as risk; auth is valid).
- **Risks and decisions:** Entire CLI 0.11.5 available but not upgraded (avoid broad upgrade). Codex hooks require approval in Codex TUI before capture is active. Entire auth logged in as github:kernelKain (expires in 29d). No secrets in generated files. `.entire/.gitignore` excludes tmp/settings.local/metadata/logs.
- **Time used:** unknown
- **Next action:** Review full diff, run `git diff --check`, commit with locked message.

## Resume policy

After interruption, reinspect branch, status, log, and diff; compare with this file; resume only the active step. Never begin the next step while the active step is uncommitted.
