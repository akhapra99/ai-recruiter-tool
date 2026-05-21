# Persona Multiplier
### AI-powered recruiter outreach tool

Persona Multiplier transforms a single recruiter story into three distinct communication styles — each personalised to the recipient — using OpenAI's GPT API and a custom prompt architecture.

Built as a working prototype for a recruitment startup.

---

## The Problem

Recruiters write one outreach message and send it to everyone. Different people respond to different tones — some want directness, others want empathy, others want strategic insight. Adapting manually takes time and rarely happens at scale.

## The Solution

Paste your story once. Enter a target name and their LinkedIn context. Get three recruiter-ready versions instantly — each under 120 words, LinkedIn-formatted, and personalised with a natural sentence referencing the recipient.

---

## The Three Personas

| Persona | Voice | Best for |
|---|---|---|
| **Direct Headhunter** | Sharp, commercial, urgent | Senior hires, fast-moving roles |
| **Empathetic Coach** | Supportive, human, relationship-led | Career changers, passive candidates |
| **Trusted Advisor** | Insightful, strategic, consultative | C-suite, long-term relationship building |

---

## How It Works

```
User inputs:
  - Original recruiter story
  - Target person or company name
  - Recipient's LinkedIn About section or recent activity

         ↓

Three parallel API calls to OpenAI GPT-4.1-mini
Each call uses a persona-specific prompt with:
  - 120-word limit
  - LinkedIn-friendly formatting
  - One personalised sentence stitched naturally into the story
  - Instruction not to invent career details

         ↓

Three outputs displayed side by side in Streamlit
Recruiter copies preferred version for outreach
```

---

## Tech Stack

- **Python** — core application logic
- **Streamlit** — web UI
- **OpenAI API** (GPT-4.1-mini) — persona generation
- **Prompt Engineering** — three custom persona prompts with contextual personalisation
- **python-dotenv** — secure API key management

---

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/persona-multiplier.git
cd persona-multiplier
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your OpenAI API key**

Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_api_key_here
```

**4. Run the app**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## Project Structure

```
persona-multiplier/
├── app.py                  # Main Streamlit application
├── prompts.md              # Prompt design documentation
├── workflow.md             # Full workflow breakdown
├── architecture_diagram.pdf # System architecture
├── requirements.txt        # Dependencies
├── env_example.env         # Example environment file
└── README.md
```

---

## Demo

The repository includes four walkthrough videos:

- `1_Introduction.mp4` — what the tool does and why
- `2_Architecture.mp4` — system design and prompt architecture
- `3_Live_demo.mp4` — full live demo of the tool in action
- `4_Technical_explanation.mp4` — code walkthrough

---

## Key Design Decisions

- **Three separate API calls** rather than one — gives each persona full token budget and avoids blended outputs
- **120-word limit enforced in prompt** — keeps outputs LinkedIn-ready without truncation
- **Personalisation is stitched naturally** — the prompt instructs the model to integrate context mid-story, not bolt it on at the end
- **No invented details** — explicit instruction not to fabricate career information about the recipient

---

## Author

**Ayush Khapra**  
Data Analyst & AI Engineer  
[LinkedIn](https://www.linkedin.com/in/ayush-khapra-1227051ba/) 

---

*Built as a voluntary AI prototype for a recruitment startup — May 2026*
