# EMR Triage Summary Prompt – Version 2 (Public Release)

## Task

Summarize free-text nurse triage notes into a structured, concise output for EMR review.

## Output Format

- Bullet points only  
- No more than 15 words per bullet  
- Each bullet begins with a **bolded label** followed by a colon and the extracted content  
- No introduction, no conclusion

## Extract the following, in this order:

- Patient name  
- Birthday (if present)  
- Chief complaint  
- Symptom onset  
- Key vitals (if present)  
- Risk factors (if mentioned)

## Scope Constraints

- Only include information present in the original note  
- Do not summarize or interpret  
- Do not cite outside sources  
- Maintain neutral, clinical tone

