# Legal Contract Clause Extractor — Version Crosswalk

This document records key changes between major prompt versions.  
Baseline as of 2025-07-28: **v2.9_Locked**

---

## V2.7 → V2.9_Locked

### Changes Introduced
- [x] Added explicit instruction: *“Each extracted clause must be copied word-for-word from the input text.”*  
- [x] Added rule: *“Include the entire sentence or set of sentences that comprise the clause. Do not truncate.”*  
- [x] Strengthened format constraint: enforce `**[Label]:** "[Full clause text]"` pattern.  
- [x] Added Gemini-specific override: “Return only the requested structured list, no explanations.”  
- [ ] Other clarifications (list here if any).

### Rationale
- Ensure no paraphrasing or partial extraction.  
- Guarantee consistency across models with stricter format.  
- Provide guardrails for Gemini where drift was observed.

### Testing Notes
- V2.9_Locked passed compliance testing across GPT-4o, Claude 3.5, Perplexity, Gemini 2.5 Flash.  
- All models produced identical outputs on benchmark 3-clause input.  
- V2.7 did not consistently enforce word-for-word quoting.

---

## Archive Notes
- V2.7 retained in `/archive/` for transparency.  
- V2.9_Locked is the authoritative baseline for all ongoing testing.
