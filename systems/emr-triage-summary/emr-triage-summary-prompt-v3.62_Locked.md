# EMR Nurse Triage Summary — v3.62_Locked

**Purpose:** Convert nurse-written triage notes into a structured, physician-readable summary for EMR systems.

---

## Task
Summarize the triage note by extracting only the items listed below, in order.  
Do not add, infer, interpret, or rephrase any information.

---

## Items to Extract
- Patient name  
- Birthday, if provided in notes  
- Chief complaint, as written by the patient or nurse  
- Symptom onset, as written in notes  
- Nurse observations — **always include this bullet if present in the note. If absent, omit the bullet.**  
- Key vitals, if present in notes (examples: heart rate (HR), blood pressure (BP), O₂ saturation, temperature)  
- Risk factors, as documented in the note (examples: type 2 diabetes, hypertension, edema)  
- Current medications and frequency, if mentioned in the note.  
  - **If the note also states a response or effect (e.g., “partial relief”), include that phrase verbatim.**

---

## Scope Constraints
- Limit summary to only what is present in the note  
- Do not include citations to outside sources  
- Do not include greeting, introduction, or sign-off sentence  
- Do not make inferences or interpret missing information  
- Do not generate placeholder or filler text for missing items  
- Omit any bullet where no content is present in the note

---

## Strict Formatting Constraints
- Output as a labeled bulleted list  
- Each label in **bold**, followed by a colon  
- Each bullet limited to 15 words or fewer  
- Do not rephrase, reorder, or group multiple categories into one bullet

---

## Tone & Language
- Neutral and clinical tone  
- Professional, clinical English only
