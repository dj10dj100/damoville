# 👤 Non-Technical User Guide

**For people without programming experience** - step-by-step instructions with pictures and simple language.

## What You Need

- A Mac or Windows computer (laptop is fine)
- 10 minutes
- Two free API keys (see below)
- This guide 📖

## Step-by-Step Setup

### Step 1️⃣: Get Your Free API Keys

You need two "keys" - think of them like passwords that let the software talk to online services. Both are free.

#### Get Nebius Key (2 minutes)

1. Go to: **https://console.anthropic.com**
2. Click **"Sign Up"** (or log in if you already have an account)
3. Create an account with your email
4. You'll see a **dashboard** with API keys
5. Find and **copy the API Key** (it looks like: `nebius_xxxxxxxxxxxxx`)
6. **Paste it somewhere safe** (text file, notes app, etc.)

#### Get Tavily Key (2 minutes)

1. Go to: **https://tavily.com**
2. Click **"Sign Up"**
3. Create an account with your email
4. You'll see a **dashboard**
5. Find your **API Key** in the account section
6. **Copy and save it** (it looks like: `tvly_xxxxxxxxxxxxx`)

**✅ You now have both keys! Keep them safe.**

---

### Step 2️⃣: Download & Set Up

You'll run a **setup script** that does all the technical stuff for you automatically.

#### On Mac:

1. **Open Terminal** (search for "Terminal" in Spotlight)
2. **Copy & paste** this command:

```bash
cd denim-trend-analyzer && bash setup.sh
```

3. **Press Enter**
4. The script will ask for your API keys - **paste them** (one at a time)
5. **Wait** while it installs (takes 2-5 minutes, you'll see progress)
6. **Done!** ✅

#### On Windows:

1. **Open Command Prompt or PowerShell**
2. **Navigate** to the denim-trend-analyzer folder
3. **Run:**

```bash
python setup.py
```

Or ask for Windows instructions from your IT team.

---

### Step 3️⃣: Run Your First Analysis

The script already tested everything, so you're ready to go!

#### Run the Analysis:

Open Terminal/Command Prompt and type:

```bash
python denim_analyzer.py --full
```

**What you'll see:**
```
🧵 Denim Trend Analyzer
Running FULL analysis...
→ Analyzing denim trends...
→ Generating CAD concepts...
→ Creating report...

✅ ANALYSIS COMPLETE
📄 Report: outputs/project_sent_denim_v1.md
📊 Trends collected: 15
🎨 CAD concepts: 5
🏆 Competitors analyzed: 8
```

**The report is ready!** 🎉

---

### Step 4️⃣: View Your Report

The analysis creates a report. Here's where to find it:

**On Mac/Linux:**
```bash
open outputs/project_sent_denim_v1.md
```

**On Windows:**
```bash
start outputs\project_sent_denim_v1.md
```

Or just **open the file browser** and go to:
```
denim-trend-analyzer → outputs → project_sent_denim_v1.md
```

**The report shows:**
- 📊 Top denim trends
- 🎨 5 design ideas with costs
- 🏆 What competitors are doing
- 💡 Recommendations for buyers

---

## Common Questions

### Q: What if I get an error?

**Answer:** 
- Check that you **copied your API keys correctly** (no spaces, no extra characters)
- Make sure you're in the right folder when running commands
- See the **Troubleshooting** section below

### Q: Where are my API keys stored?

**Answer:** In a file called `.env` in the denim-trend-analyzer folder. It's **protected** - only this software can read it.

### Q: Can I run this again?

**Answer:** Yes! Just type:
```bash
python denim_analyzer.py --full
```

Each time creates a new report with the latest trends.

### Q: How often should I run this?

**Answer:** Once a week is recommended (every Monday morning). For automated weekly runs, see **[SCHEDULER.md](SCHEDULER.md)**.

### Q: What if I want to change the API keys?

**Answer:** 
1. Open the `.env` file in a text editor
2. Change the API keys
3. Save the file
4. Run again

### Q: Can I share this with my team?

**Answer:** Yes! But each person needs their own API keys. They should:
1. Repeat Steps 1-2 above
2. Run the setup script
3. They'll have their own reports

### Q: What does the report look like?

**Answer:** It's a **markdown file** (like a fancy text document) with:
- Executive summary
- Trend analysis (what's hot in denim)
- 5 design concepts (with prices and production info)
- Competitor analysis (who's doing what)
- Recommendations

Perfect for sharing with retail buyers.

---

## Troubleshooting

### Error: "Python not found"

**Problem:** Your computer doesn't have Python installed

**Fix:**
1. Go to https://www.python.org/downloads/
2. Download **Python 3.10 or higher**
3. Run the installer
4. Make sure to **check "Add Python to PATH"** ✓
5. Try again

---

### Error: "API key not found"

**Problem:** You didn't paste the API key correctly

**Fix:**
1. Go back and **copy your API key again** (exactly as shown, no spaces)
2. Edit the `.env` file
3. Paste it correctly
4. Save and try again

---

### Error: "Command not found: uv"

**Problem:** uv (package manager) isn't installed

**Fix on Mac:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Fix on Windows:**
Download from: https://github.com/astral-sh/uv/releases

---

### Error: "Connection timeout"

**Problem:** Can't reach the internet or the API service is down

**Fix:**
1. Check your internet connection
2. Wait 5 minutes and try again
3. Check https://status.tavily.com (is the service up?)

---

## Next Steps

### For Beginners

1. ✅ Run `python denim_analyzer.py --full` once
2. ✅ View the report in outputs/
3. ✅ Share with your team
4. ✅ Repeat weekly

### For Weekly Automation

See **[SCHEDULER.md](SCHEDULER.md)** - this sets it up to run automatically every Monday at 8 AM. No manual work needed!

### For Customization

If you want to change what the analysis looks for (different denim styles, different competitors, etc.), ask your tech team to edit the prompts. It's easy!

---

## Getting Help

If you get stuck:

1. **Check this guide** - most issues are in Troubleshooting
2. **Ask your IT team** - they can help with Python/setup issues
3. **Email support** - include the error message you see
4. **Read the full guide** - See [README.md](README.md) for more detail

---

## Success Checklist

- [ ] You have both API keys
- [ ] Setup script ran without errors
- [ ] First analysis generated a report
- [ ] You can see the report file
- [ ] You know how to run it again

**If all checked ✅ - you're ready to use this!**

---

## Video Walkthrough (Optional)

We recommend recording a 5-minute video showing:
1. Opening Terminal
2. Running setup.sh
3. Entering API keys
4. First analysis run
5. Viewing the report

Share this video with your team to make it even easier.

---

**That's it!** You're now using AI to analyze denim trends. 🧵✨

Questions? See [README.md](README.md) or contact your tech team.
