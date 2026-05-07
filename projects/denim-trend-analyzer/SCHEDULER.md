# ⏰ Scheduler Integration Guide

Instructions for setting up automatic weekly execution of the Denim Trend Analyzer using Cowork's scheduled task system.

## Overview

The Denim Trend Analyzer is designed to run automatically every Monday at 8:00 AM using Cowork's `scheduled-tasks` feature. This guide shows you how to set it up.

## Quick Setup (5 minutes)

### 1. Create the Scheduled Task

```python
# In your Cowork environment, create a new scheduled task:

from cowork import create_scheduled_task

create_scheduled_task(
    taskId="weekly-denim-analysis",
    description="Generate weekly denim trend analysis and CAD concepts",
    cronExpression="0 8 * * 1",  # Monday 8 AM
    prompt="""
    Run the weekly denim trend analysis pipeline.
    
    Instructions:
    1. Navigate to the denim-trend-analyzer project directory
    2. Activate the virtual environment: source .venv/bin/activate
    3. Run the analysis: python denim_analyzer.py --full
    4. The report will be saved to: outputs/project_sent_denim_v1.md
    5. Design concepts will be in: outputs/denim_cad_concepts_v1/
    """
)
```

### 2. Manual Test Run

Before automating, test it manually:

```bash
# Activate environment
source .venv/bin/activate

# Run a full analysis
python denim_analyzer.py --full

# Check output
ls -la outputs/
cat outputs/project_sent_denim_v1.md
```

### 3. Enable Notifications (Optional)

Get a notification when the weekly run completes:

```python
create_scheduled_task(
    taskId="weekly-denim-analysis",
    # ... other settings ...
    notifyOnCompletion=True,  # Sends notification when done
)
```

## Schedule Reference

The task uses **5-field cron format** in your local timezone:

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
│ │ │ │ │
* * * * *
```

### Common Schedules

| Schedule | Cron | Description |
|----------|------|-------------|
| Monday 8 AM (default) | `0 8 * * 1` | Weekly on Monday morning |
| Every day 9 AM | `0 9 * * *` | Daily morning run |
| Tuesday 6 PM | `0 18 * * 2` | Weekly evening |
| Multiple times/week | `0 8 * * 1,3,5` | Monday, Wed, Friday 8 AM |
| First of month 9 AM | `0 9 1 * *` | Monthly report |

## Full Setup Instructions

### Step 1: Prepare the Project

Make sure your project is set up and tested:

```bash
# Navigate to project
cd /path/to/denim-trend-analyzer

# Install dependencies
uv sync

# Test with dry-run
source .venv/bin/activate
python denim_analyzer.py --dry-run

# Verify output looks good
cat outputs/project_sent_denim_v1.md
```

### Step 2: Create Wrapper Script (Optional)

Create a simple wrapper script for Cowork to call:

**File: `run_weekly_analysis.sh`**
```bash
#!/bin/bash
set -e

# Setup
cd /path/to/denim-trend-analyzer
source .venv/bin/activate

# Run analysis
echo "🧵 Starting weekly denim trend analysis..."
python denim_analyzer.py --full

# Log success
echo "✅ Analysis complete at $(date)"
echo "📁 Report: outputs/project_sent_denim_v1.md"

# Optional: Upload to cloud storage, send email, etc.
# aws s3 cp outputs/project_sent_denim_v1.md s3://my-bucket/denim-reports/
```

Make it executable:
```bash
chmod +x run_weekly_analysis.sh
```

### Step 3: Register with Cowork Scheduler

In Cowork or via the Cowork CLI:

```python
# Pseudo-code for Cowork dashboard/CLI

task = ScheduledTask(
    id="weekly-denim-analysis",
    name="Weekly Denim Trend Analysis",
    description="Analyzes trending denim products and generates CAD concepts",
    
    # When to run
    schedule="cron",
    cronExpression="0 8 * * 1",  # Monday 8 AM local time
    
    # What to run
    scriptPath="/path/to/denim-trend-analyzer/run_weekly_analysis.sh",
    # OR directly via Python:
    pythonScript="""
    import subprocess
    import os
    
    os.chdir('/path/to/denim-trend-analyzer')
    subprocess.run(['python', 'denim_analyzer.py', '--full'], check=True)
    """,
    
    # Notifications
    notifyOnCompletion=True,
    notifyOnFailure=True,
    notificationEmail="dan@daniel-jenkins.com",
    
    # Resource limits
    timeout=1800,  # 30 minutes max
    maxConcurrent=1,  # Only one run at a time
)

task.save()
```

### Step 4: Verify Scheduling

Check that the task is registered:

```bash
# List all scheduled tasks
cowork tasks list

# Check specific task
cowork tasks show weekly-denim-analysis

# View recent runs
cowork tasks logs weekly-denim-analysis --lines 20
```

### Step 5: Monitor First Run

Monitor the first scheduled run:

```bash
# Watch logs in real-time
cowork tasks logs weekly-denim-analysis --follow

# Check output files
ls -la outputs/
tail -50 outputs/project_sent_denim_v1.md
```

## Output & Artifacts

After each weekly run:

```
outputs/
├── project_sent_denim_v1.md              # Main report
├── denim_cad_concepts_v1/                # Design briefs
│   ├── concept_01_vintage_wide_leg.txt
│   ├── concept_02_smart_casual_hybrid.txt
│   ├── concept_03_sustainable_raw_denim.txt
│   ├── concept_04_oversized_boyfriend_fit.txt
│   ├── concept_05_premium_smart_denim.txt
│   └── trend_metadata.json
├── project_sent_denim_v2.md              # Previous week (auto-rotated)
├── denim_cad_concepts_v2/
└── ...
```

### Version Rotation

Outputs are automatically versioned weekly:
- **First Monday**: v1
- **Second Monday**: v2
- **Third Monday**: v3
- ...backs up to ~52 weeks of history

To keep a specific week's report:

```bash
# Archive and protect
mkdir -p archived_reports
cp -r outputs/project_sent_denim_v5.md archived_reports/denim_report_week_of_may_7.md
```

## Troubleshooting Scheduled Runs

### Task Doesn't Run

**Check**: Is the task enabled?

```bash
# Enable if disabled
cowork tasks enable weekly-denim-analysis
```

**Check**: Does the cron expression make sense?

```bash
# Test cron syntax
# Use: https://crontab.guru
# Enter: 0 8 * * 1
# Result: "At 08:00 on Monday"
```

**Check**: Are API keys available to the scheduler?

```bash
# Make sure .env is readable and contains all keys
cat .env | grep NEBIUS_API_KEY
cat .env | grep TAVILY_API_KEY
```

### Task Runs but Fails

**Check output logs**:
```bash
cowork tasks logs weekly-denim-analysis --lines 100
```

**Common issues**:
- Missing API keys → Update .env
- Python not found → Check PATH in scheduler environment
- Working directory wrong → Use absolute paths in script
- Dependencies missing → Run `uv sync` again

**Debug run**:
```bash
# Run manually with verbose output
python denim_analyzer.py --full --verbose --log-level=DEBUG
```

### Task Runs Slowly

**Check execution time**:
```bash
# See duration of last run
cowork tasks logs weekly-denim-analysis | grep Duration
```

**Optimize**:
- First run takes longer (model loading)
- Subsequent runs faster (cached models)
- Tavily searches take 2-3 min (network dependent)
- LLM analysis takes 5-8 min (depends on model size)

### Modify Schedule

**Change to a different day/time**:

```bash
# Update cron expression
cowork tasks update weekly-denim-analysis \
  --cron "0 14 * * 2"  # Tuesday 2 PM instead

# Or run multiple times per week
cowork tasks update weekly-denim-analysis \
  --cron "0 8 * * 1,3,5"  # Monday, Wednesday, Friday 8 AM
```

## Integration with Other Systems

### Email Notification (Manual)

Add to `denim_analyzer.py`:

```python
import smtplib
from email.mime.text import MIMEText

def send_report_email(report_path, recipient):
    with open(report_path, 'r') as f:
        content = f.read()
    
    msg = MIMEText(content)
    msg['Subject'] = f"Weekly Denim Analysis - {date.today()}"
    msg['From'] = "denim-bot@company.com"
    msg['To'] = recipient
    
    smtp = smtplib.SMTP('localhost')
    smtp.send_message(msg)
    smtp.quit()

# In main: after generating report
if __name__ == "__main__":
    report = run_analysis()
    send_report_email("outputs/project_sent_denim_v1.md", "team@company.com")
```

### Slack Integration (Phase 5)

```python
from slack_sdk import WebClient

def post_to_slack(report_path):
    client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
    
    with open(report_path) as f:
        content = f.read()
    
    client.chat_postMessage(
        channel="#product-dev",
        text=f"📊 Weekly Denim Analysis\n```{content}```"
    )
```

### Cloud Storage (Phase 5)

```python
import boto3

def backup_to_s3():
    s3 = boto3.client('s3')
    s3.upload_file(
        'outputs/project_sent_denim_v1.md',
        'my-bucket',
        'denim-reports/latest.md'
    )
```

## FAQ

**Q: What if the run takes longer than expected?**
A: Increase the timeout setting (default 30 min). Check logs for bottlenecks.

**Q: Can I run multiple times per week?**
A: Yes, change cron to `0 8 * * 1,3,5` for Mon/Wed/Fri.

**Q: What timezone is used?**
A: Your local timezone. The cron expression is evaluated on your system time.

**Q: Can I skip a week?**
A: Temporarily disable with `cowork tasks disable weekly-denim-analysis`, then re-enable.

**Q: How do I change which LLM is used?**
A: Edit `config.py` before scheduling. Changes apply to next run.

**Q: Can I test the schedule without running?**
A: Yes, use the manual execution: `python denim_analyzer.py --dry-run`

## Monitoring & Alerts

### Set up monitoring:

```bash
# Check last 5 runs
cowork tasks logs weekly-denim-analysis --lines 5

# Alert if no report for 2+ weeks
# Add to a monitoring dashboard or use cron to check:
crontab -e
# Add: 0 10 * * 2  if [ ! -f outputs/project_sent_denim_v$(date +%V).md ]; then alert; fi
```

## Next Steps

1. ✅ Set up the scheduled task (above)
2. Test the first manual run
3. Monitor the first scheduled execution
4. Fine-tune schedule based on results
5. Integrate with email/Slack (Phase 5)
6. Set up report archival/backup

---

For more help, see:
- [README.md](README.md) - Project overview
- [SETUP.md](SETUP.md) - Installation guide
- Cowork documentation - Scheduler API reference
