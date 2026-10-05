# 🎯 JobHunt

### Your personal AI job-search agent — built to find the right jobs, not apply to everything.

JobHunt is a **privacy-conscious, AI-powered job-search automation system** that checks public ATS job boards every morning, filters out irrelevant roles using deterministic rules, evaluates the remaining jobs against your profile, generates tailored application drafts, and sends a concise daily digest to your inbox.

**It never submits an application.**

You stay in control.

```text
                    JOBHUNT PIPELINE

       Public ATS Boards
              │
              ▼
       ┌──────────────┐
       │   FETCH      │  Greenhouse / Lever / Ashby
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ PRE-FILTER   │  Title • Location • Freshness
       │   $0 / LLM   │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ AI SCREENING │  Resume ↔ Job Description
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ AI DRAFTING  │  Cover Note • Talking Points
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │    DIGEST    │  Top opportunities
       └──────┬───────┘
              │
              ▼
          📧 YOUR INBOX
              │
              ▼
       YOU REVIEW → YOU APPLY
```

### The basic idea

```text
2,000 jobs
    ↓
   40 relevant
    ↓
    5 worth your time
    ↓
  1 daily digest
```

Instead of spending hours searching job boards, JobHunt spends its time doing the boring work.

You spend your time making decisions.

---

## ✨ Why JobHunt?

Most job-search automation makes the wrong optimization:

> **"How many jobs can I apply to?"**

JobHunt asks a different question:

> **"Which jobs are actually worth applying to?"**

The system deliberately separates **cheap deterministic filtering** from **expensive AI reasoning**.

```text
                    2,000 postings
                         │
                         ▼
               ┌──────────────────┐
               │ Deterministic    │
               │ filtering        │
               │                  │
               │ Title            │
               │ Location         │
               │ Seniority        │
               │ Freshness        │
               └────────┬─────────┘
                        │
                        ▼
                    ~40 jobs
                        │
                        ▼
               ┌──────────────────┐
               │ LLM screening    │
               │                  │
               │ Resume fit       │
               │ Skills           │
               │ Experience       │
               │ Requirements     │
               └────────┬─────────┘
                        │
                        ▼
                     ~5 jobs
                        │
                        ▼
               ┌──────────────────┐
               │ LLM drafting     │
               │                  │
               │ Cover note       │
               │ Talking points   │
               │ Application kit │
               └────────┬─────────┘
                        │
                        ▼
                    📧 Digest
```

**The LLM never sees the 2,000 jobs.**

That's the key design decision.

---

# 🚀 Features

### 🔎 Multi-ATS job discovery

JobHunt currently supports public job boards from:

- Greenhouse
- Lever
- Ashby

Each ATS has its own parser and its own quirks.

The system normalizes everything into a common `Job` model.

---

### ⚡ Zero-cost deterministic filtering

Before an LLM is called, jobs are filtered using:

- Job title
- Seniority
- Location
- Remote eligibility
- Posting age
- Function
- Duplicate status

Example:

```yaml
filters:
  include_titles:
    - '\bsde\b'
    - 'software development engineer'
    - 'machine learning engineer'
    - 'ai engineer'
    - 'data scientist'

  exclude_titles:
    - '\b(staff|principal)\b'
    - '\b(manager|director)\b'
    - '\bintern\b'
    - '\bjunior\b'

  locations:
    - bangalore
    - bengaluru
    - hyderabad
    - india

  allow_remote: true
  max_age_days: 30

score_threshold: 7.0
max_per_digest: 5
```

This stage uses **no LLM and costs nothing**.

---

# 🧠 AI-Powered Job Screening

Once the deterministic gate has done its job, the remaining opportunities are evaluated against your profile.

The model considers things like:

- Technical skills
- Years of experience
- Industry experience
- Required technologies
- Preferred technologies
- Seniority
- Location
- Responsibilities
- Career trajectory
- Overall fit

Instead of simply asking:

> "Does this job contain Python?"

JobHunt asks:

> "Given this candidate's experience, how strong is the actual match?"

Each job receives a structured score.

```json
{
  "job_id": "greenhouse:example:12345",
  "score": 8.7,
  "recommendation": "strong_match",
  "matched_skills": [
    "Python",
    "FastAPI",
    "AWS",
    "RAG",
    "LLMs"
  ],
  "missing_skills": [
    "Kubernetes"
  ],
  "reason": "Strong match for the core AI/ML requirements..."
}
```

---

# ✍️ Application Kit Generation

For the best opportunities, JobHunt generates a small application kit.

For example:

```text
┌─────────────────────────────────┐
│        APPLICATION KIT          │
├─────────────────────────────────┤
│ Match Score:        9.1 / 10    │
│                                 │
│ Why this fits                  │
│ ─────────────────────────────   │
│ 3–5 concise reasons            │
│                                 │
│ Cover Note                     │
│ ─────────────────────────────   │
│ Tailored draft                  │
│                                 │
│ Talking Points                 │
│ ─────────────────────────────   │
│ 3–5 points for recruiter call  │
│                                 │
│ Potential Gaps                 │
│ ─────────────────────────────   │
│ Skills worth reviewing         │
└─────────────────────────────────┘
```

The AI drafts.

**You decide.**

---

# 📧 Daily Digest

Instead of receiving dozens of alerts, you receive one focused digest.

Example:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        JOBHUNT DAILY DIGEST
        Monday • 06 October
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5 opportunities found

🥇 9.3  Senior AI Engineer
    Company A • Hyderabad
    Strong match

🥈 8.9  Machine Learning Engineer
    Company B • Bangalore
    Strong match

🥉 8.4  GenAI Engineer
    Company C • Remote India
    Good match

──────────────────────────────────

3 additional opportunities available

[View Full Digest]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

No endless scrolling.

No job-board spam.

Just the opportunities worth investigating.

---

# 🔐 Human-in-the-Loop by Design

JobHunt intentionally **does not auto-submit applications**.

There is no:

```text
AI → Apply
```

Instead:

```text
AI → Find
   → Filter
   → Score
   → Draft
   → Notify
          ↓
       HUMAN
          ↓
        APPLY
```

This is deliberate.

You review the job.

You review the AI-generated content.

You make the final decision.

You press **Submit**.

---

# 🛠️ Supported Providers

JobHunt uses a provider abstraction so the AI layer can be swapped without changing the rest of the application.

| Provider | Environment Variable | PDF | Typical Use |
|---|---|---:|---|
| Anthropic | `ANTHROPIC_API_KEY` | ✅ | High-quality screening/drafting |
| Google Gemini | `GEMINI_API_KEY` | ✅ | Cost-efficient |
| Groq | `GROQ_API_KEY` | ❌ | Fast screening |
| OpenAI-compatible | configurable | ❌ | OpenRouter / Together / vLLM |
| Ollama | None | ❌ | Local/private inference |

Screening and drafting can use different providers.

For example:

```bash
LLM_PROVIDER=anthropic

SCREEN_PROVIDER=groq
DRAFT_PROVIDER=anthropic

SCREEN_MODEL=<fast-screening-model>
DRAFT_MODEL=<high-quality-drafting-model>
```

This lets you use:

**cheap + fast model → screening**

and

**stronger model → final drafting**

---

# 💰 Cost Architecture

The system is designed around one simple principle:

> **Don't spend tokens deciding whether a job should have been filtered by a regex.**

For example:

```text
2,000 jobs
   │
   │  No LLM
   ▼
  40 jobs
   │
   │  Cheap model
   ▼
  10 jobs
   │
   │  Strong model
   ▼
   5 jobs
```

With a tight configuration, the AI workload is tiny compared with the number of jobs initially discovered.

You can also run screening through providers with free tiers or use Ollama locally.

---

# 🧪 Development Mode

Want to try the complete system without API keys?

Run:

```bash
python -m jobhunt run --mock --scorer keyword
```

The mock mode uses realistic ATS fixtures and exercises the **actual parser and pipeline code**.

Example:

```text
[1/5] fetching
      Greenhouse: 800
      Lever:      650
      Ashby:      550

[2/5] filtering
      prefilter: 2000 → 40
      dropped:
        title=1,420
        location=310
        stale=230

[3/5] screening
      40 jobs
      11 scored >= 7.0

[4/5] drafting
      5 application kits

[5/5] digest
      wrote out/digest.html

────────────────────────────────────
FUNNEL

2,000 scanned
      ↓
40 passed filters
      ↓
40 new
      ↓
11 strong matches
      ↓
5 in digest
────────────────────────────────────
```

Open:

```text
out/digest.html
```

in your browser.

No API key.

No network.

No money.

---

# ⚡ Quick Start

## 1. Clone

```bash
git clone <your-repo>
cd jobhunt
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the demo

```bash
python -m jobhunt run --mock --scorer keyword
```

You now have a working end-to-end job-search pipeline.

---

# 🎯 Configure Your Target Companies

Edit:

```text
companies.yaml
```

Example:

```yaml
companies:

  - name: Stripe
    ats: greenhouse
    slug: stripe

  - name: Netlify
    ats: lever
    slug: netlify

  - name: Ramp
    ats: ashby
    slug: ramp
```

The slug normally corresponds to the final part of the public careers URL.

| Careers URL | ATS | Slug |
|---|---|---|
| `boards.greenhouse.io/stripe` | greenhouse | stripe |
| `jobs.lever.co/netlify` | lever | netlify |
| `jobs.ashbyhq.com/ramp` | ashby | ramp |

Start with **10–15 companies**.

More companies do not automatically mean better results.

---

# 👤 Build Your Candidate Profile

Create your environment file:

```bash
cp .env.example .env
```

Then configure your provider.

For example:

```env
ANTHROPIC_API_KEY=your_key_here
```

Build your profile:

```bash
python -m jobhunt profile --resume resume.pdf
```

JobHunt sends the resume to the configured provider and creates:

```text
profile.json
```

Example:

```json
{
  "summary": "...",
  "years_experience": 5,
  "skills": [
    "Python",
    "Machine Learning",
    "Generative AI",
    "RAG",
    "FastAPI",
    "AWS"
  ],
  "target_roles": [
    "AI Engineer",
    "ML Engineer",
    "GenAI Engineer"
  ],
  "target_locations": [
    "Hyderabad",
    "Bangalore",
    "Remote India"
  ]
}
```

**Always review this file before using it.**

It is gitignored because it contains personal information.

---

# ▶️ Run the Agent

Build a digest:

```bash
python -m jobhunt run
```

Build and send the email:

```bash
python -m jobhunt run --send
```

Limit the number of jobs while testing:

```bash
python -m jobhunt run --limit 10
```

Skip application drafting:

```bash
python -m jobhunt run --no-draft
```

---

# 📊 Job Tracking

JobHunt maintains a local job index:

```text
seen.json
```

This prevents the same opportunity from appearing repeatedly.

Mark a job as applied:

```bash
python -m jobhunt applied "greenhouse:stripe:5501001"
```

View statistics:

```bash
python -m jobhunt stats
```

Export:

```text
out/tracker.csv
```

You can open the CSV in Excel or Google Sheets.

---

# ⏰ Automation

The repository includes:

```text
.github/workflows/daily.yml
```

The workflow can run the agent automatically on weekdays.

Conceptually:

```text
06:00 IST
   │
   ▼
GitHub Actions
   │
   ├── Fetch ATS boards
   ├── Filter jobs
   ├── Screen matches
   ├── Draft application kits
   ├── Generate digest
   └── Email candidate
```

The workflow carries `seen.json` between runs using GitHub Actions cache.

Personal state is **not committed to the repository**.

---

# 🔑 GitHub Secrets

Configure the following repository secrets:

| Secret | Purpose |
|---|---|
| `PROFILE_JSON` | Candidate profile |
| `ANTHROPIC_API_KEY` | Anthropic provider |
| `GEMINI_API_KEY` | Gemini provider |
| `GROQ_API_KEY` | Groq provider |
| `SMTP_USER` | Email account |
| `SMTP_PASS` | Gmail App Password |
| `MAIL_TO` | Digest recipient |

Only configure the provider you actually use.

For Gmail, use an **App Password**, not your normal account password.

---

# 🏗️ Architecture

```text
jobhunt/
│
├── jobhunt/
│   │
│   ├── fetch.py
│   │     └── ATS clients + Job model
│   │
│   ├── prefilter.py
│   │     └── deterministic filtering
│   │
│   ├── providers.py
│   │     └── LLM provider abstraction
│   │
│   ├── llm.py
│   │     ├── screen()
│   │     ├── draft()
│   │     ├── build_profile()
│   │     └── keyword_stub()
│   │
│   ├── digest.py
│   │     └── HTML email generation
│   │
│   ├── mailer.py
│   │     └── SMTP delivery
│   │
│   ├── store.py
│   │     ├── deduplication
│   │     ├── tracking
│   │     └── CSV export
│   │
│   ├── mock.py
│   │     └── ATS fixtures
│   │
│   └── cli.py
│         └── command-line interface
│
├── tests/
│
├── companies.yaml
├── config.yaml
├── requirements.txt
├── .env.example
├── README.md
└── .github/
    └── workflows/
        └── daily.yml
```

---

# 🧩 Clean Parser Architecture

One important design principle:

**HTTP is separate from parsing.**

Instead of:

```text
HTTP request
   ↓
Parser
   ↓
Job
```

the system uses:

```text
HTTP
 ↓
Decoded JSON
 ↓
Parser
 ↓
Job objects
```

For example:

```python
parse_greenhouse(slug, company, body)
parse_lever(slug, company, body)
parse_ashby(slug, company, body)
```

Each parser accepts already-decoded JSON and returns:

```python
list[Job]
```

This makes the parsers:

- deterministic
- testable
- easy to mock
- independent of networking
- safe to regression-test

---

# 🧠 ATS Quirks

Real-world APIs are messy.

JobHunt explicitly handles several common ATS differences.

### Greenhouse

Greenhouse descriptions can contain HTML entities.

The parser therefore:

```text
HTML entities
      ↓
unescape
      ↓
strip HTML
      ↓
unescape again
      ↓
clean text
```

This prevents things like:

```text
&amp;
```

from leaking into the LLM prompt.

---

### Lever

Lever timestamps use:

```text
epoch milliseconds
```

not normal Python seconds.

Lever job descriptions can also be distributed across:

```text
descriptionPlain
lists[].text
lists[].content
additionalPlain
```

All relevant fields are combined before screening.

---

### Ashby

Ashby can contain unpublished jobs.

The parser ignores:

```json
{
  "isListed": false
}
```

so draft/unpublished positions never enter the pipeline.

---

# 🧪 Testing

Run:

```bash
python -m pytest tests -q
```

The test suite requires:

- no API key
- no network
- no external services

Tests cover:

- Greenhouse parsing
- Lever parsing
- Ashby parsing
- HTML cleanup
- timestamp conversion
- title filtering
- location filtering
- freshness filtering
- seniority filtering
- deduplication
- unpublished Ashby jobs
- LLM batching
- JSON parsing
- malformed LLM responses
- out-of-order results
- failed batches
- JD truncation
- draft generation

---

# 🐛 One Tiny Regex That Can Cost You Hundreds of Jobs

This is surprisingly important.

Don't write:

```regex
sde
```

and assume it means:

```text
Software Development Engineer
```

It doesn't.

Instead, explicitly support:

```yaml
include_titles:
  - '\bsde\b'
  - 'software development engineer'
```

The test suite pins this behavior so a future configuration change doesn't silently destroy your job funnel.

---

# 🔄 Idempotency & Deduplication

Every job receives a globally unique identifier:

```text
{ats}:{slug}:{id}
```

Example:

```text
greenhouse:stripe:5501001
```

This means rerunning the pipeline doesn't repeatedly show the same job.

The system maintains:

```text
seen.json
```

which acts as both:

- deduplication index
- lightweight application tracker

---

# 🛡️ Privacy & Safety

JobHunt is intentionally conservative.

### It does NOT:

❌ submit applications  
❌ automate CAPTCHA solving  
❌ scrape LinkedIn  
❌ scrape Naukri  
❌ impersonate the candidate  
❌ automatically send recruiter messages  
❌ commit your resume/profile to Git  
❌ automatically make career decisions  

### It DOES:

✅ read public ATS job data  
✅ filter opportunities  
✅ score candidate-job fit  
✅ draft application material  
✅ track what you've already seen  
✅ send you a digest  

The final decision always stays with the candidate.

---

# 🌐 Why No LinkedIn or Naukri?

JobHunt is deliberately built around public ATS endpoints rather than scraping sites that don't provide an appropriate public API for this use case.

Supported sources are:

```text
Greenhouse
Lever
Ashby
```

This keeps the ingestion layer simpler and reduces dependence on fragile scraping techniques.

---

# 🗺️ Roadmap

JobHunt can evolve considerably without changing its core architecture.

### Phase 1 — Foundation

- [x] Greenhouse ingestion
- [x] Lever ingestion
- [x] Ashby ingestion
- [x] Deterministic filtering
- [x] Resume profile
- [x] LLM screening
- [x] Application drafting
- [x] HTML digest
- [x] Job deduplication

### Phase 2 — Intelligence

- [ ] Semantic job matching
- [ ] Skill-gap detection
- [ ] Company preference scoring
- [ ] Career-growth scoring
- [ ] Salary-aware ranking
- [ ] Remote-work scoring
- [ ] Recruiter/contact extraction
- [ ] Personalized ranking history

### Phase 3 — Analytics

```text
Jobs discovered
       ↓
Jobs shortlisted
       ↓
Applications submitted
       ↓
Recruiter responses
       ↓
Interviews
       ↓
Offers
```

Track conversion rates across:

- companies
- roles
- skills
- locations
- salary ranges
- application sources

Eventually, the system can learn:

> "Which types of jobs actually produce interviews for this candidate?"

That's much more valuable than simply finding more jobs.

---

# 💡 The Bigger Idea

JobHunt isn't really a job scraper.

It's a **personal opportunity-ranking engine**.

The interesting part isn't fetching jobs.

Fetching jobs is easy.

The interesting part is progressively reducing uncertainty:

```text
                    JOB UNIVERSE
                         │
                         ▼
                ┌─────────────────┐
                │ Is it relevant? │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Is it fresh?    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Am I qualified? │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Is it a strong  │
                │ career move?    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Is it worth my  │
                │ time today?     │
                └────────┬────────┘
                         │
                         ▼
                    TOP 5 JOBS
                         │
                         ▼
                       YOU
```

The goal isn't:

> **Apply to 500 jobs.**

The goal is:

> **Find the 5 jobs you would have regretted missing.**

---

# ⭐ Project Philosophy

```text
Automation should remove repetition,
not remove judgment.
```

JobHunt automates the boring parts.

You keep the important parts.

**Find intelligently.  
Filter ruthlessly.  
Rank objectively.  
Draft quickly.  
Decide yourself.**

---

## License

Add your preferred license here.

---

## Built for people who would rather spend 30 minutes applying to 5 excellent opportunities than spend 5 hours applying to 100 random ones.
