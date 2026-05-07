# 🎓 Team Onboarding Guide

**How to get non-technical team members running the Denim Trend Analyzer in 10 minutes.**

## Overview

You have two types of users:

| User Type | Tech Level | Setup Time | Guide |
|-----------|-----------|-----------|-------|
| **Tech-savvy** | Comfortable with CLI, git, Python | 5 min | [QUICKSTART.md](QUICKSTART.md) |
| **Non-technical** | Uses GUI, doesn't know CLI | 10 min | [NON_TECHNICAL_GUIDE.md](NON_TECHNICAL_GUIDE.md) |
| **Everyone else** | In between | 7 min | Follow below |

## Quick Decision Tree

```
Do they know how to use Terminal/Command Prompt?
│
├─ YES → Send them QUICKSTART.md (5 min)
│
└─ NO → Send them NON_TECHNICAL_GUIDE.md (10 min)
        + setup.sh (Mac) or setup.py (Windows)
```

## For Non-Technical Users: Three Steps

### Step 1: Send Them This Package

Send a zip file or GitHub link containing:
- `setup.sh` (or `setup.py`)
- `NON_TECHNICAL_GUIDE.md`
- Everything else in the repo

### Step 2: They Get API Keys (3 minutes)

They follow the section **"Step 1: Get Your Free API Keys"** in [NON_TECHNICAL_GUIDE.md](NON_TECHNICAL_GUIDE.md)

- Nebius: https://console.anthropic.com
- Tavily: https://tavily.com

Both are free and take < 2 min to get.

### Step 3: They Run Setup (5 minutes)

#### **On Mac:**
```bash
cd denim-trend-analyzer
bash setup.sh
```

#### **On Windows:**
```bash
cd denim-trend-analyzer
python setup.py
```

The script:
- ✅ Checks Python is installed
- ✅ Asks for API keys
- ✅ Installs all dependencies
- ✅ Tests everything works
- ✅ Done! ✨

**They don't need to understand what's happening - it just works.**

### Step 4: They Run Analysis (2 minutes)

```bash
python denim_analyzer.py --full
```

Report appears in: `outputs/project_sent_denim_v1.md`

---

## What the Setup Script Does (For Your Understanding)

The `setup.sh` / `setup.py` automates all the technical stuff:

```
User runs setup.sh
    ↓
Checks Python installed ✓
    ↓
Asks for API keys
    ↓
Creates .env file (protects with permissions)
    ↓
Installs dependencies (uv or pip)
    ↓
Tests that everything works
    ↓
Success! Ready to run.
```

**No git, no virtual environments, no CLI knowledge required.**

---

## Common Non-Technical Questions & Answers

### "What are API keys?"
Think of them like **passwords that let the software talk to online services**. They're free and safe - just treat them like passwords.

### "Why do I need two keys?"
Because the software uses two different services:
1. **Nebius** - the AI brain (analyzes trends)
2. **Tavily** - searches the web for denim info

Both are free tier.

### "Will it steal my keys?"
No - they're stored in a `.env` file that's protected and never shared online. Only your computer can use them.

### "Can I run it multiple times?"
Yes! Every time you run:
```bash
python denim_analyzer.py --full
```

It creates a new report with today's trends.

### "What if I forget my keys?"
Go back to where you got them and get new ones:
- Nebius: https://console.anthropic.com
- Tavily: https://tavily.com

Then edit `.env` and paste the new keys.

### "Does it cost money?"
No! Both Nebius and Tavily have free tiers that are generous. The script uses < $1 per week in API calls.

---

## Distribute to Your Team

### Email Template

```
Subject: 🧵 New Denim Analysis Tool - Easy Setup

Hi team!

We've built a tool that analyzes trending denim products automatically every week.

Getting started is easy:

1. Download/clone: [GITHUB LINK]

2. If you're technical:
   → See QUICKSTART.md (5 minutes)

3. If you're non-technical:
   → See NON_TECHNICAL_GUIDE.md (10 minutes)
   → Run setup.sh (Mac) or setup.py (Windows)

4. Run your first analysis:
   python denim_analyzer.py --full

Questions? Ask [YOUR NAME]

Enjoy! 🎉
```

### Slack Message

```
🧵 New tool: Denim Trend Analyzer

Just deployed! Analyzes trending denim products & generates CAD concepts automatically.

📌 Setup: 10 minutes
💰 Cost: Free
⏰ Runs: Weekly (automatic)

Two ways to get started:
→ Tech-savvy? Use QUICKSTART.md
→ Prefer simplicity? Use NON_TECHNICAL_GUIDE.md

Questions? dm me
```

---

## After They Set Up

### First Run Help

**If analysis takes longer than 15 min:**
- Normal! First run loads the AI model (can take 10-15 min)
- Second run is much faster (7-10 min)

**If they get an error:**
- Check troubleshooting in NON_TECHNICAL_GUIDE.md
- Most issues: wrong API key, copy/paste correctly
- Contact you for help

### Weekly Automation

Once everyone has it working, set up weekly automation:
See [SCHEDULER.md](SCHEDULER.md) - runs every Monday 8 AM automatically.

### Customization

If they want to change what it analyzes (different denim styles, different competitors, etc.):
- You (or tech team) edit `src/prompts.py`
- They run the analysis again
- New customized report

---

## Troubleshooting Non-Technical Users

### "I got 'Python not found'"

**Solution:** They need to install Python
1. Go to https://www.python.org/downloads/
2. Download Python 3.10 or later
3. Run installer, **check "Add Python to PATH"** ✓
4. Try setup again

### "It says 'API key not found'"

**Solution:** Copy their key more carefully
1. Go back to Nebius or Tavily
2. Click to copy (don't select/paste, use copy button)
3. Paste into setup
4. Try again

### "I forgot my password!"

**Solution:** Tell them
- Nebius: Click "Forgot Password" on login page
- Tavily: Same

They'll reset it.

### "Can't find the report file"

**Solution:** Tell them
- Open file browser
- Find the `denim-trend-analyzer` folder
- Open `outputs` folder
- Look for `project_sent_denim_v1.md`

Or on Mac:
```bash
open outputs/project_sent_denim_v1.md
```

Or on Windows:
```bash
start outputs\project_sent_denim_v1.md
```

---

## Supporting Materials (Optional)

### Video Tutorial

Record a 5-minute YouTube video showing:
1. Getting API keys
2. Running setup.sh
3. First analysis
4. Viewing report

Share with team - cuts support questions in half.

### One-Page Cheat Sheet

Print this and give to non-technical users:

```
🧵 Denim Analyzer - Quick Reference

GET STARTED:
1. Run: bash setup.sh (Mac) or python setup.py (Windows)
2. Paste your API keys when asked
3. Wait for "Setup Complete!"

RUN ANALYSIS:
python denim_analyzer.py --full

FIND REPORT:
outputs/project_sent_denim_v1.md

HELP:
See NON_TECHNICAL_GUIDE.md
or ask [your name]
```

### Support Channel

Create a Slack/Teams channel `#denim-analyzer-help` for questions.

---

## Success Metrics

You've successfully onboarded non-technical users when:

✅ They can run `python denim_analyzer.py --full` without errors
✅ They understand where the report is
✅ They know how to interpret the report
✅ They can run it again next week
✅ They don't need to ask "how do I...?" questions

---

## Maintenance Notes

### When to Update Prompts

If users say "I wish it analyzed [something else]":
- Edit `src/prompts.py`
- They re-run analysis
- New customized reports

### When to Upgrade

Every few weeks:
```bash
uv sync
```

Gets latest LLM and tools.

### When Something Breaks

Check:
1. API keys still valid? (Tavily might have disabled free tier)
2. Internet connection?
3. Python still installed?
4. Dependencies fresh? (`uv sync` again)

---

## TL;DR - Super Short Version

**To onboard a non-technical user:**

1. **Send them:** `NON_TECHNICAL_GUIDE.md` + `setup.sh`/`setup.py`
2. **They run:** `bash setup.sh` or `python setup.py`
3. **Done!** They just answer 2 questions (API keys)
4. **Then:** `python denim_analyzer.py --full`

**That's it. No terminal knowledge needed.**

---

## Questions About This Guide?

See:
- **[NON_TECHNICAL_GUIDE.md](NON_TECHNICAL_GUIDE.md)** - For your non-technical users
- **[QUICKSTART.md](QUICKSTART.md)** - For tech-savvy users
- **[README.md](README.md)** - For decision makers
- **[SCHEDULER.md](SCHEDULER.md)** - For weekly automation
