══════════════════════════════════════════════════════
Name: CaseHop
Backup name: Benchmate
Name status: No prominent CaseHop software or AI-product collision found on
17 October 2026 through preliminary web, GitHub, package-registry, and Product
Hunt checks. This is not legal clearance; review relevant trademark databases
before commercial use.

What: CaseHop compares an existing AI model with open alternatives using the
customer’s reviewed examples and requirements, exposes consequential failures,
and produces an evidence-backed model decision and controlled-switch plan.

Why: General benchmarks cannot tell a small SaaS team whether another model
will perform its specific application task without losing facts, inventing
information, or breaking expected outputs.

Hook: A cheaper candidate initially looks promising, but CaseHop highlights
that it changed order number A-1847 to A-1841 and immediately marks the model
REJECT. Another open candidate preserves the evidence, earns TRY, and receives
a controlled Hop Plan.

Hackathon:
  Event/dates: Hacktoberfest Open-Source AI Challenge: Week 2,
  12–18 October 2026
  Deadline: 19 October 2026 at 12:29 PM IST
  Judging criteria: Writing Quality, weighted most heavily; Relevance to the
  Prompt and Theme; Creativity; Technical Execution; meaningful partner
  technology use for entered partner categories
  Primary track: Side Hustle
  Qualification: Build something people could pay for with open-source AI at
  its core → open models perform the customer’s actual support-ticket task →
  the demo shows one candidate being rejected for inventing an order number
  and another earning a controlled-trial recommendation
  Secondary track: Best Use of Render
  Qualification: Use Render as the project’s AI runtime or application host →
  Render provides the public CaseHop evaluation experience → judges open the
  deployed product, run the prepared comparison, and receive the Model Decision
  Report and Hop Plan
  Conditional categories: Best Use of Entire and Best Use of GitHub Copilot
  may be entered only if the final submission contains material, visible proof.
  Best Use of Backboard remains provisional pending Prompt 1 validation.
  Required technology:
    - Open-weight models perform the application task being evaluated; removing
      them destroys the central open-innovation purpose.
    - Render provides the public, judge-accessible product experience; removing
      it invalidates the Render category but not the local product concept.
    - Entire records the Codex and OpenCode sessions behind an important product
      decision; removing it preserves customer functionality but invalidates
      the Entire-category claim.
    - GitHub Copilot performs a review whose material finding and resulting fix
      must be shown; without such evidence, do not enter its category.
    - Backboard, if retained, provides meaningful candidate-model access; its
      removal invalidates only the provisional Backboard category.
  Target prize: Primary Side Hustle challenge recognition and Best Use of
  Render; conditional Entire, GitHub Copilot, and Backboard categories only
  when honestly earned
  Official sources:
    - https://dev.to/challenges/hacktoberfest-week2-2026-10-12
    - https://dev.to/challenges/hf26

Builder context:
  Hours: 20 realistic hours
  Backend preference: Python; preference only, not a stack decision
  Team: Solo
  Coding mode/tool/model: AI-assisted coding with Codex and OpenCode; Entire
  records the sessions and model details
  Frontend constraint: Basic React/Vite ability; not a design specialist
  API/access preference: Prefer no more than two external APIs and free tiers
  or already available credits; Prompt 1 must validate all access

Product:
  Target user/situation: A founder-engineer or product engineer at a small SaaS
  needs to replace the model behind an existing structured-output AI feature
  because of cost, latency, deprecation, privacy, or self-hosting requirements.

  User job and problem: Determine whether an open model can perform the team’s
  real application task without losing important details, inventing facts, or
  breaking expected behavior.

  Failed workaround: Public leaderboards, model playgrounds, spreadsheets, and
  generic evaluation tools leave testing, failure review, decision-making, and
  migration preparation fragmented.

  Input:
    - One narrowly defined AI task
    - Approximately 30 representative, reviewed cases
    - Approved outcomes
    - Facts that must be preserved
    - Forbidden behavior
    - One current model
    - Two open-model candidates
    - Optional acceptable cost and latency limits

  Product mechanism:
    1. Build a Case Pack from representative examples, approved outcomes, and
       explicit requirements.
    2. Give the same Case Pack to the current model and two open candidates.
    3. Check outputs against the requirements and send ambiguous cases for
       human review.
    4. Present passes, failures, available measurements, and unknowns.
    5. Issue an evidence-limited TRY, HOLD, or REJECT verdict.
    6. Produce a Hop Plan for the selected candidate with limitations,
       verification conditions, and rollback guidance tied to tested evidence.

  Visible outcome:
    - Model Decision Report
    - Requirement-level pass and failure evidence
    - Individual failure examples
    - Human-review decisions
    - Available latency and cost measurements
    - Explicit unknowns
    - TRY, HOLD, or REJECT verdict
    - Downloadable, repeatable Case Pack
    - Evidence-bound Hop Plan

  Required-technology role: Open models perform the customer’s actual task
  rather than commenting on it. Render makes the live product accessible.
  Entire and GitHub Copilot provide separately attributable build evidence.

  Non-wrapper thesis: CaseHop maintains a customer-specific Case Pack, approved
  outcomes, must-preserve facts, forbidden behavior, human-review status,
  comparable run history, requirement-level evidence, decision thresholds, and
  a Hop Plan constrained by observed results. A generic chat assistant does not
  preserve this tested contract and decision trail.

  Closest analogue/difference: Langfuse and Promptfoo provide broad evaluation
  infrastructure. EvalShift and ProofShift are closer model-migration or
  change-safety analogues. CaseHop’s proposed difference is a guided,
  case-first journey for small SaaS teams from “Can this model do our job?” to
  “Here is the evidence and a controlled way to try the switch.” This
  differentiation remains an assumption requiring user validation.

  Visual signature: The original customer message containing order number
  A-1847 appears beside a candidate output containing invented number A-1841.
  The mismatch is exposed, and the promising candidate receives REJECT.

  Judge fit:
    - Writing Quality: One user, one commercial problem, and one clear story
    - Relevance: Open models perform the real application task
    - Creativity: Moves from model comparison to an evidence-bound switch plan
    - Technical Execution: Shows requirement-level evidence and uncertainty
    - Product potential: Addresses a recurring, costly small-SaaS decision
    - Partner technology: Render is visible in the public experience; Entire
      and Copilot are supported by concrete development evidence if claimed

  60-second product story:
    - 0–8 seconds: Introduce a SaaS replacing an expensive support-ticket model.
    - 8–16 seconds: Run the same 30 reviewed cases through the current model and
      two open alternatives.
    - 16–28 seconds: Expose the cheaper candidate inventing order number A-1841.
    - 28–38 seconds: Show a second candidate preserving essential facts and
      earning TRY on the tested evidence.
    - 38–49 seconds: Select it and display its limitations, trial conditions,
      verification guidance, and rollback conditions.
    - 49–55 seconds: Show that open models performed the actual task through
      the public Render-hosted CaseHop experience.
    - 55–60 seconds: Close with: “CaseHop does not tell you which model wins a
      generic benchmark. It shows whether a model can do your job—and how to
      try the switch without hiding the risks.”

  Must-be-true claim: Given approximately 30 reviewed examples, approved
  outcomes, and explicit requirements for one support-ticket extraction task,
  CaseHop produces an evidence-backed comparison, requirement-level failure
  report, and controlled-trial recommendation for a small SaaS team evaluating
  its current model against two open alternatives.

Product potential:
  Recurring need: Teams must reevaluate models after new releases, pricing
  changes, deprecations, prompt changes, privacy requirements, and regressions.

  Early adopter/buyer: An indie SaaS founder-engineer operating a support-message
  extraction or routing feature; the founder or small engineering team is the
  likely buyer.

  Distribution wedge: Founder communities, open-source model communities, and
  direct outreach to small SaaS teams already discussing model cost or
  self-hosting; assumption only.

  Expansion/monetization:
    - Free open-source self-hosted edition
    - Assumed $99 one-off hosted model-switch rehearsal
    - Assumed $49 per month for recurring comparisons and regression checks
    - Future expansion into prompt comparisons, agent evaluations, larger Case
      Pack libraries, continuous checks, and team review workflows

  Evidence level:
    - Verified: Conceptual fit with the official open-AI, Side Hustle, Render,
      Entire, and GitHub Copilot category descriptions
    - Supported: General benchmarks do not establish fitness for a customer’s
      specific application cases
    - Assumption: Small SaaS teams will pay for the guided decision and Hop Plan
    - Unknown: Willingness to pay, category access, comparative measurement
      quality, and whether the workflow is sufficiently better than alternatives

Product boundary:
  Essential:
    - One support-message extraction and routing task
    - Approximately 30 reviewed examples
    - One current model and two open candidates
    - Approved outcomes and explicit requirements
    - Requirement-level checks and human review for ambiguity
    - Individual failure evidence before aggregate results
    - Available quality, latency, and cost evidence with unknowns preserved
    - TRY, HOLD, or REJECT verdict
    - One evidence-bound Hop Plan
    - Downloadable Model Decision Report and repeatable Case Pack
    - Visible open-model execution

  Optional:
    - Recorded demonstration fallback
    - Comparison-history summary
    - Additional failure categories
    - Backboard candidate access
    - Entire session embed
    - Material GitHub Copilot review evidence
    - Detailed cost-savings projection
    - Additional export format
    - Second Case Pack

  Excluded:
    - Arbitrary AI tasks
    - Multiple supported application types
    - Production-safety certification
    - Automatic production migration
    - Automatically applied code or configuration changes
    - Model training or fine-tuning
    - Tinker-category participation
    - Prompt and agent evaluation
    - Continuous regression or CI workflows
    - Team collaboration
    - Large public benchmark libraries
    - Broad provider coverage
    - Authentication, billing, and account management
    - Guaranteed cost comparison
    - Claims that 30 cases establish production reliability

  Hook-preserving fallback:
    - Run at least one candidate live.
    - Clearly label unavailable candidates as recorded results.
    - Preserve the invented-order-number failure and verdict.
    - Mark missing cost information as unknown.
    - Provide a manual controlled-trial checklist instead of unsupported changes.
    - Retain the Model Decision Report and Hop Plan as the final outcome.
    - If Render is unavailable, demonstrate locally and withdraw its category.

Prompt 1 must investigate:
  Product assumptions:
    - Whether target users value a guided decision and Hop Plan enough to pay
    - Whether TRY, HOLD, and REJECT improve rather than oversimplify the decision
    - Whether the CaseHop journey is meaningfully easier than existing tools
    - Whether approximately 30 reviewed examples provide a useful initial signal
    - Whether the Hop Plan can remain specific and evidence-bound

  Technical feasibility questions:
    - Validate one current model and two open candidates for the same task.
    - Determine how the same task and requirements can be applied fairly.
    - Determine which requirements can be checked reliably and which require
      human review.
    - Define defensible verdict conditions without implying certification.
    - Validate genuinely comparable latency and cost measurements.
    - Determine how each Hop Plan statement remains traceable to evidence.
    - Validate one supported example application for credible proposed changes,
      verification guidance, and rollback guidance.
    - Confirm the essential product can be completed within 20 realistic hours.

  Access and dependency risks:
    - Candidate availability, limits, response time, and demonstration cost
    - Render access and suitability for the required public experience
    - Entire session capture and shareability
    - Availability of a material GitHub Copilot review contribution
    - Backboard credits, candidate lineup, limits, and category significance
    - Model or service failure during the live demonstration
    - Privacy handling for submitted examples and demonstration data

  Claims to validate:
    - Open candidates perform the same customer task comparably.
    - Requirement failures can be exposed reliably enough to support the Hook.
    - The Hop Plan is constrained by actual tested evidence.
    - Render usage is meaningful enough for its category.
    - Entire and GitHub Copilot contributions are sufficiently material.
    - Backboard deserves entry only if its use becomes genuine and visible.
    - The final product never presents a small test set as production proof.

  Open engineering decisions:
    - Architecture and system boundaries
    - Programming language confirmation, frameworks, and libraries
    - Model-access approach and exact candidates
    - Evaluation and human-review approach
    - Data representation and persistence
    - Detailed UX and screen behavior
    - Privacy and security controls
    - Report and Case Pack formats
    - Hop Plan grounding and safety controls
    - Render deployment and runtime configuration
    - Entire, Copilot, and optional Backboard integration details
    - Testing, observability, failure recovery, and demo fallback
    - Engineering scope, acceptance criteria, phases, branches, and commits

History:
  Rejected directions:
    - Broad general-purpose model evaluation platform: too large and
      insufficiently differentiated for the available time
    - Generic leaderboard or benchmark dashboard: does not answer whether a
      model works for the customer’s application
    - Automatic model migration: unsafe and not credible within the boundary
    - Fine-tuning extension: optional experiment would threaten the core build
    - Multi-task and continuous-evaluation platform: outside the initial Hook
    - Benchmate name: replaced by the more distinctive CaseHop identity

  Selection reason: CaseHop combines a concrete commercial problem, visible
  open-model participation, a memorable invented-order-number failure, honest
  uncertainty, and a differentiated path from evaluation evidence to a
  controlled model-switch decision. Its narrow first version appears compatible
  with 20 hours of solo, AI-assisted work, subject to Prompt 1 validation.

Boundary:
  Product identity, user, problem, promise, Hook, track proof, required-technology
  role, differentiation, and product boundary are approved.

  Prompt 1 exclusively owns technical validation, architecture, stack, detailed
  UX, APIs, data, security, deployment, engineering scope, acceptance criteria,
  testing, risks, phase planning, branches, commits, and implementation queue.

  Prompt 2 exclusively owns implementation, repository mutation, commands,
  verification, Git operations, deployment, and delivery.
══════════════════════════════════════════════════════