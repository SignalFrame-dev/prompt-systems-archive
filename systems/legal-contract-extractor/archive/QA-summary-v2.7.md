QA Summary: Legal Contract Clause Extractor (v2.7)

Prompt version tested: legal-contract-extractor-v2.7.txt
Testing timeframe: July 19–22, 2025
Tested by: Manual evaluation by SignalFrame
Purpose: Verify clause extraction, scope enforcement, and strict formatting across multiple models.

📋 Test Scope

The system was evaluated on its ability to:

Extract only obligations, restrictions, renewal/termination clauses explicitly present in the contract text.

Copy clauses word-for-word (no paraphrasing, no truncation).

Output in enforced format:

**[Label]:** "[Full clause text]"


Return entire sentence(s) that make up the clause.

Omit any labels if a clause type is not present.

🧪 Models Tested

GPT-4o

Claude 3.5 (Opus)

Gemini 2.5 Flash

Perplexity AI

✅ Results Summary
Constraint	Pass/Fail (All Models)
Enforced output format	⚠️ Partial — Gemini drifted
Word-for-word clause reproduction	⚠️ Partial — Claude paraphrased
No truncation of sentences	⚠️ Partial — GPT-4o truncated in 1 test
Scope-limited extraction (only O/R/R clauses)	✅ Pass (All)
Labels omitted if clause absent	✅ Pass (All)
🧠 Notable Observations

Claude 3.5: Occasionally rewrote clauses into plainer language. Needed explicit word-for-word rule.

Gemini: Produced extra explanation text outside the required list. Required model-specific override.

GPT-4o: Once returned partial clause sentence instead of full set. Fix applied in v2.9 by mandating “entire sentence(s)”.

🧯 Known Issues (v2.7)

No universal enforcement of verbatim extraction.

Gemini non-compliance with structured-list-only constraint.

🏁 Verdict

Status: ❌ QA failed — v2.7 did not consistently enforce word-for-word clause copying or Gemini drift suppression.
Next step: Prompt hardened into v2.9_Locked with explicit rules and overrides.
