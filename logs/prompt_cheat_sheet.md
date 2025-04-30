# ChatGPT Prompt Design Cheat Sheet (RECAPS)

Use this framework to create high-quality prompts that yield focused, relevant, and actionable responses.

## 🔁 RECAPS Framework

| Element | Description | Example |
|--------|-------------|---------|
| **R — Role** | Specify who ChatGPT should act as. | "Act as a Linux sysadmin…" |
| **E — End Goal** | Clarify your desired outcome. | "I want a Bash script to select a subfolder and `cd` into it." |
| **C — Context** | Provide any necessary background, constraints, or assumptions. | "I'm using WSL, prefer no dependencies." |
| **A — Action Request** | Explicitly state what you want done. | "Write a script..." or "Summarize this..." |
| **P — Preferred Format** | Indicate how you want the output. | "Code only, with inline comments." or "Markdown list." |
| **S — Style/Scope** | Define tone, depth, or coverage. *(Optional)* | "Concise and technical", "Blog tone", "High-level only." |

---

## 🧩 Prompt Template

Use this template to build high-impact prompts:

```plaintext
I want you to act as a [role] and help me achieve [end goal].  
Here’s some context: [context or constraints].  
Please [specific action request].  
Format the result as [preferred format], with [any style or scope preferences].
```


### Examples
```plaintext
Act as a Bash expert.
I want to create a script that lists subdirectories and lets me select one to cd into.
I'm using WSL and prefer minimal dependencies.
Please provide the script with inline comments only, no explanation.
Keep it concise and readable.
```

### Other Tips
Avoid vagueness → Be direct with your request and format.

Use constraints → Time limits, line counts, or dependency restrictions help focus the response.

Build iteratively → Start simple, then refine in follow-ups.