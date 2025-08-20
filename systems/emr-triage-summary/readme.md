# EMR Nurse Triage Summary

## 🔍 What It Does
- Extracts a predetermined set of fields from a nurse triage note (patient name, symptom onset, vitals, risk factors, etc.).  
- Converts unstructured triage text into a structured, physician-readable summary.  

## 🧠 Design Principles
- Designed to handle nurse notes written in inconsistent or free-text formats.  
- Enforces strict scope and no-inference guardrails.  
- Allows null-output if a field is absent in the note.  

## 📄 Files Included
- `emr-triage-summary-prompt-v1.4_Locked.md` — current baseline  
- `case-study.md` — applied case study and scenario notes  
- `human-context.md` — authorship rationale and context  
- `tests/` — compliance logs  
- `archive/` — earlier versions  

## 🏷 Version Info
- **Current baseline:** v1.4_Locked  
- **Tested models:** GPT-4o, Claude 3.5, Gemini 1.5 Pro, Perplexity, Mistral, Meta AI  
- **Result:** Passed 50+ hours of multi-model compliance testing  

## Versioning Notes
- **Locked versions** represent tested baselines safe for reference.  
- **Earlier versions** are archived for transparency but not intended for active use.
