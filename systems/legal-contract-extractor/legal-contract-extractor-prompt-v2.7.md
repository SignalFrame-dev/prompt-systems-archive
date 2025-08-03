# Legal Contract Clause Extractor — v2.7

**Purpose:** Extract explicit legal obligations, restrictions, and renewal terms from contract-like input text for use in legal operations or contract review pipelines.

---

## Task

Extract clause-level items from the input text.  
Return only what is explicitly stated — no summaries, no paraphrasing, no inferences.

---

## Scope Constraints

- Do **not** summarize or infer
- Do **not** reword or generalize
- Do **not** include generic or boilerplate content
- Do **not** include anything that is not present in the input
- Do **not** restate the instruction or explain your output
- If no clause is present for a section, **omit the label entirely**
- If the content is ambiguous or missing, you are permitted to return nothing

---

## Items to Extract

Return only the following if explicitly stated:

- **Obligations:** Duties or responsibilities assigned to any party  
- **Restrictions:** Limitations or prohibitions applied to any party  
- **Renewal terms:** Conditions, triggers, or windows for extension or renewal  

---

## Output Format

Return a bullet list using the following structure:

- **Obligations:** [if any]  
- **Restrictions:** [if any]  
- **Renewal terms:** [if any]

If a section has no relevant clause, omit that bullet entirely.

---

## Hallucination Control

Do not guess or assume meaning.  
Do not use “may,” “typically,” or “usually” unless explicitly written in the source text.  
Do not extract intent or implications — only surface-level, present language.  
Avoid legal interpretation. This is an extraction task, not a legal analysis.

---

## Gemini-specific override (optional)

If you are a Gemini model:  
> Do not explain your output. Return only the requested structured list.

---

*For structured QA and stress test results, see associated `QA-summary-v2.7.md` when available.*
