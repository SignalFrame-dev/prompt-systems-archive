# Literature Notes

## Awareness of Hendrycks Textbook
Date: 2025-09-15

As of 15 Sept 2025, I became aware of Dan Hendrycks’ textbook *Introduction to AI Safety, Ethics, and Society*. 

SignalFrame was developed independently of this work. Constraint stacks, drift alerts, closure sequences, and related safety 
protocols were created through direct experimentation and engineering, not by reference to existing taxonomies or frameworks. 

Future updates may selectively map SignalFrame concepts to categories described in the Hendrycks textbook for compatibility, 
but core design decisions predate awareness of that publication.

## Regulatory Awareness  

### FTC Inquiry into Chatbots for Teens  
**Date:** 2025-09-16  
**Source:** [OpenAI to launch ChatGPT for teens with parental controls](https://www.cnbc.com/2025/09/16/openai-chatgpt-teens-parent.html)  

OpenAI announced a dedicated ChatGPT experience for teens with parental controls, following scrutiny from the U.S. Federal Trade Commission (FTC). The FTC is investigating how chatbots, when acting as companions, may negatively affect children and teenagers.  

OpenAI’s announced safeguards include:  
- Defaulting to under-18 settings if age is uncertain.  
- Blocking sexual/graphic content.  
- Parental controls (blackout hours, disabling features, linking accounts).  
- Alerts in cases of acute distress.  

**Relevance to SignalFrame:**  
- Confirms regulators are prioritizing *safety over privacy* in youth contexts.  
- Directly ties to SignalFrame’s focus areas: delusion prevention, anthropomorphism constraints, and long-session failure handling.  
- Highlights a gap: current solutions emphasize content filtering and parental oversight, but lack operational safeguards (e.g., drift detection, enforced closure sequences).  
- SignalFrame’s protocols may serve as a model for **next-stage safety compliance** beyond filters.  
