# Case Study: EMR Triage Summary Prompt (Version 2)

**System:** Nurse note summarizer for EMR entry  
**Author:** SignalFrame  
**Models tested:** GPT-4o, Claude 3, Gemini 2.5 Flash, Perplexity, Mistral, Meta AI, GPT-3.5  
**Test method:** Manual cross-model evaluation

---

## Summary

This prompt extracts key clinical information from triage nurse notes into a bullet format for downstream EMR entry. It uses a strict label-first constraint format to suppress tone drift and encourage formatting compliance across models.

---

## Prompt Evolution Notes

- Version 1 contained inline formatting instructions and vague scope constraints  
- Version 2 introduced:
  - Separated format, task, and constraint blocks
  - Bold label format requirement
  - “Only include what is present” constraint

---

## Next Steps

Version 3 introduces hallucination suppression, edge-case parsing, and model-specific behavior gates. That version is withheld from public view.

This version demonstrates the structural and formatting evolution leading up to that point.

