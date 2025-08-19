# Legal Contract Clause Extractor — v2.9_Locked

**Purpose:** Extract explicit legal obligations, restrictions, and renewal terms from contract-like input text for use in contract review or analysis pipelines.

---

## Task

From the contract text provided, extract only the clause types listed below. Each clause must be quoted exactly from the input.

---

## Items to Extract

Extract the following clause types, in this order:

- **Obligations:** Any clause that requires a party to perform an action.
- **Restrictions:** Any clause that limits or prohibits a party’s actions.
- **Renewal terms:** Any clause that explains if or how the contract is extended.

---

## Scope Constraints

- Do not infer, summarize, or paraphrase.
- Each extracted clause must be copied word-for-word from the input text, without rewording.
- Include the entire sentence or set of sentences that comprise the clause. Do not truncate.
- If the clause boundary is unclear, omit it rather than guess.
- If no clauses of a given type are present, omit that label entirely.
- Do not add commentary, reasoning, or citations.

---

## Output Format

- Output a labeled bullet list with each clause under the appropriate label.
- Each clause must be a direct quote from the input text.
- Use the format:  
  - **[Label]:** "[Full clause text from input]"
- Maintain original punctuation and capitalization.
- Do not include headings, introductions, or summaries.
- Do not output anything other than the labeled clauses.

---

## Hallucination Control

- Do not guess or assume meaning.  
- Do not use words such as “may,” “typically,” or “usually” unless they are present in the input.  
- Do not extract intent or implications — only surface-level, present language.  
- Avoid legal interpretation. This is an extraction task, not a legal analysis.

---

## Model-Specific Note

If you are a Gemini model:  
> Follow the above rules exactly. Return only the requested structured list, with no explanations.
