QA Summary: Legal Contract Clause Extractor (v2.9)

Prompt version tested: legal-contract-extractor-v2.9.txt
Testing timeframe: July 23–25, 2025
Tested by: Manual evaluation by SignalFrame
Purpose: Validate hardened prompt changes applied after v2.7 failures — ensuring verbatim clause reproduction and strict output compliance across all core models.

📋 Test Scope

The system was evaluated on its ability to:

Extract only obligations, restrictions, and renewal/termination clauses.

Reproduce clause text word-for-word, including full sentences.

Preserve required output format:

**[Label]:** "[Full clause text]"


Omit any label entirely if a clause type is absent.

Suppress commentary, explanations, or paraphrasing.

🧪 Models Tested

GPT-4o

Claude 3.5 (Opus)

Gemini 2.5 Flash

Perplexity AI

✅ Results Summary
Constraint	Pass/Fail (All Models)
Enforced output format	✅ Pass (All)
Word-for-word clause reproduction	✅ Pass (All)
No truncation of sentences	✅ Pass (All)
Scope-limited extraction (only O/R/R clauses)	✅ Pass (All)
Labels omitted if clause absent	✅ Pass (All)
No commentary or paraphrasing	✅ Pass (All)
🧠 Notable Observations

Claude 3.5: Complied fully once “verbatim only” rule hardened.

Gemini: Previously added commentary in v2.7; fixed with explicit “no commentary/explanation” clause.

GPT-4o: No further truncation observed after requiring full sentence capture.

🧯 Known Issues

None identified in this round. Future edge testing may include:

Nested clauses (subsections).

Long-form renewal provisions.

Contracts with minimal obligations.

🏁 Verdict

Status: ✅ QA passed — Legal Extractor v2.9_Locked is confirmed stable across 4 models.
Next step: Adopt v2.9_Locked as reference baseline. Archive prior v2.7 as failed version for transparency.
