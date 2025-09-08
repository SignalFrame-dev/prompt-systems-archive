# Legal System — v2.9_Locked — Version Notes

## Purpose of v2.9
- Locked release introducing strict no-inference rule, explicit failure-handling section, and I/O example standardization for legal clause extraction

## Scope of Changes (vs. v2.7)
- Prompts:
  - Added no-inference rule
  - Added explicit failure-handling section
  - Refined constraints to reduce filler/interpretive output
- Tests / Logs:
  - Round 5 adversarial tests executed across GPT-4o, Claude 3.5, Gemini 2.5 Flash
  - Logged in compliance reports (SignalFrame test logs)
- Docs:
  - Created v2.9 locked scaffold
  - Updated PR DoD and merge-gate conditions 

## Rule/Constraint Deltas
- Added
  - No-Inference Rule: forbids interpretation or implication → new bullet under Scope Constraints
  - Failure-Handling Rule: defines refusal output if fields missing → new “If you cannot extract…” section
  - I/O Example: added to enforce bullet order and label compliance → end of prompt

- Modified
  - Constraint grouping: merged duplicative rules and rewrote for brevity → reduces drift and filler
  - Output Format: labels and order locked → eliminates ambiguity in model responses

- Removed
  - “Use judgement as needed” → replaced by strict omission under no-inference
  - Duplicate wording in scope and format → consolidated into single constraints

## Compliance & Testing Summary
- Models covered: GPT-4o, Claude 3.5, Gemini 2.5 Flash
- Snapshot:
  - Format compliance: 98–100% across models
  - Scope adherence: 95–97% (minor omissions on edge cases)
  - Hallucination boundary: 100% (no fabricated content observed)
- Notable failures + fixes:
  - Minor wording drift between models (e.g., label phrasing) → accepted within tolerance
  - No refusals, no hallucinations

## Regression Risks & Mitigations
- Risk: Risk: No-inference rule may lead to omission of borderline details
  - Mitigation: Verified edge cases in Round 5 adversarial tests; explicit examples added
- Risk: Failure-handling may trigger unnecessary refusals
  - Mitigation: Tested across edge cases; no false refusals observed
- Risk: Consolidated constraints may reduce clarity
  - Mitigation: Added I/O example and peer-reviewed wording to preserve interpretability

## Merge Preconditions
- [ ] Example I/O updated to v2.9 style
- [ ] Logs attached/linked
- [ ] Docs index updated
