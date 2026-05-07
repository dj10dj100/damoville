# 🔌 Cowork Integration Guide

**How to use the Denim Trend Analyzer as a Cowork skill with full automation.**

## Overview

The Denim Trend Analyzer works perfectly with Cowork's:
- ✅ Scheduled task system (weekly automation)
- ✅ File system integration (store reports)
- ✅ Task tracking (monitor runs)
- ✅ Team collaboration (share outputs)
- ✅ Session management (persistent data)

This guide shows you how to set it up.

## Quick Setup in Cowork

### Step 1: Enable the Skill

In Cowork:
```
Settings → Skills → Add Skill
Search: "denim-trend-analyzer" or "Denim Trend Analyzer"
Click: Install
```

### Step 2: First Run

In a Cowork session:
```
/denim-trend-analyzer --help
```

Or run the setup wizard:
```
/denim-trend-analyzer --setup
```

You'll be prompted for:
- Nebius API key (get free from https://console.anthropic.com)
- Tavily API key (get free from https://tavily.com)

### Step 3: Run First Analysis

```
/denim-trend-analyzer --full
```

Report appears in: `outputs/project_sent_denim_v1.md`

### Step 4: Set Up Weekly Automation

In Cowork's scheduled tasks:
```
Create Task
├── Name: "Weekly Denim Analysis"
├── Schedule: "0 8 * * 1" (Monday 8 AM)
├── Command: "/denim-trend-analyzer --full"
└── Notify: On completion
```

**Done!** Runs every Monday at 8 AM automatically.

---

## Integration Details

### How It Works in Cowork

```
Cowork Scheduler
    ↓
Runs: /denim-trend-analyzer --full
    ↓
Python Pipeline (5 agents)
    ↓
Generates Report
    ↓
Saves to: outputs/
    ↓
Available in: Cowork file system
    ↓
Share with team
```

### File Storage

Reports are saved to Cowork's file system:
```
/cowork/denim-analyzer/
├── outputs/
│   ├── project_sent_denim_v1.md (week 1)
│   ├── project_sent_denim_v2.md (week 2)
│   ├── denim_cad_concepts_v1/
│   └── denim_cad_concepts_v2/
└── logs/
    └── analysis_runs.log
```

All accessible from Cowork's file browser.

### API Keys in Cowork

Cowork securely stores your API keys:
1. You provide during setup
2. Stored in Cowork's secure vault
3. Only used by this skill
4. Never logged or exposed

To change keys:
```
/denim-trend-analyzer --update-keys
```

---

## Scheduled Task Setup (Step-by-Step)

### In Cowork Dashboard

1. **Go to**: Scheduled Tasks
2. **Click**: Create New Task
3. **Fill in:**

   ```
   Task Name:        Weekly Denim Analysis
   Description:      Analyzes denim trends and generates CAD concepts
   Schedule Type:    Recurring (Cron)
   Cron Expression:  0 8 * * 1
   Command:          /denim-trend-analyzer --full
   Timeout:          1800 (30 minutes)
   Notify on:        Success & Failure
   ```

4. **Click**: Save
5. **Status**: Active ✅

### Cron Schedule Explained

```
0 8 * * 1
│ │ │ │ │
│ │ │ │ └─ Day of week (1=Monday)
│ │ │ └─── Month (all months)
│ │ └───── Day of month (all days)
│ └─────── Hour (8=8 AM)
└───────── Minute (0=on the hour)

Result: Every Monday at 8:00 AM
```

**Other examples:**
- Daily: `0 8 * * *` (8 AM every day)
- Weekly (Fri): `0 8 * * 5` (8 AM Friday)
- Twice weekly: `0 8 * * 1,4` (Monday & Thursday)
- Monthly: `0 8 1 * *` (1st of month)

### Advanced Options

#### Custom Email Alerts

```yaml
notifyOnCompletion:
  email: your-team@company.com
  format: html
  includeReport: true
```

#### Slack Integration

```yaml
slackChannel: '#denim-trends'
slackMessage: |
  📊 Weekly Denim Analysis Complete
  Report: [link]
  Trends: [count]
  Concepts: [count]
```

#### Report Archival

```yaml
archiveOutputs:
  enabled: true
  location: 'cloud-storage://denim-reports/'
  retention: 52  # weeks
```

---

## Using Reports in Cowork

### View Latest Report

From Cowork:
```
Files → outputs/ → project_sent_denim_v1.md
```

Click to open in Cowork's markdown viewer.

### Export Report

```
Right-click → Download
Email to team: [select recipients]
Archive: [auto-saves to Cowork storage]
```

### Share with Team

In Cowork:
```
Right-click report → Share
Select team members → View/Edit access
```

They receive a notification with access link.

---

## Customization in Cowork

### Change Analysis Parameters

Edit the skill configuration:
```
/denim-trend-analyzer --config
```

Options:
- `--max-trends 20` (default: 10-15)
- `--categories vintage,sustainable,oversized` (default: all)
- `--competitors primark,zara,asos` (default: top 8)
- `--report-format markdown` (default: markdown, html in Phase 5)

### Example Custom Run

```
/denim-trend-analyzer --full \
  --categories sustainable,eco-friendly \
  --competitors primark \
  --log-level debug
```

### Modify Agent Prompts

For custom analysis focus:

1. **In Cowork editor**, open `src/prompts.py`
2. **Edit** the prompts (5 total)
3. **Save** changes
4. **Re-run** analysis with custom prompts

Example: Focus on oversized/baggy trends
```python
# In CAD_CONCEPT_PROMPT:
# Add: "Focus on oversized and baggy silhouettes"
# Changes how concepts are generated
```

---

## Monitoring & Alerts

### View Run History

In Cowork Scheduled Tasks:
```
Task: Weekly Denim Analysis
├── Last Run: Monday, May 5 at 8:00 AM ✅
├── Duration: 11 minutes
├── Output: project_sent_denim_v2.md
├── Status: Success
└── Next Run: Monday, May 12 at 8:00 AM
```

### Get Alerts

```yaml
Alerts:
  onSuccess: "Denim analysis completed - check outputs/"
  onFailure: "Denim analysis failed - check logs"
  slackChannel: "#product-alerts"
  emailRecipients:
    - your-email@company.com
    - team-email@company.com
```

### Check Logs

In Cowork:
```
Scheduled Tasks → Weekly Denim Analysis → Logs
```

View detailed execution logs, errors, and timing.

---

## Cowork File System Structure

After first run:
```
/cowork/denim-analyzer/
├── .env                              (secure, protected)
├── src/                              (skill code)
│   ├── config.py
│   ├── data_models.py
│   ├── prompts.py
│   ├── main.py
│   └── denim_analyzer.py
├── outputs/                          (growing weekly)
│   ├── project_sent_denim_v1.md
│   ├── project_sent_denim_v2.md
│   ├── denim_cad_concepts_v1/
│   ├── denim_cad_concepts_v2/
│   └── analysis_metadata_*.json
└── logs/
    ├── run_2026_05_12.log
    ├── run_2026_05_19.log
    └── errors.log
```

All persisted between sessions.

---

## Cowork Permissions

### For Team Members

**To view reports:**
```
Minimal permission:
├── Read outputs/
└── View reports
```

**To run analysis manually:**
```
Standard permission:
├── Execute skill
├── Read/write outputs/
└── View logs
```

**To manage scheduling:**
```
Admin permission:
├── Create/edit scheduled tasks
├── Modify skill configuration
├── Archive/delete reports
└── Manage API keys
```

### Setting Permissions

In Cowork:
```
Settings → Permissions
Find skill: denim-trend-analyzer
├── [Team Name] → Read outputs
├── [Dev Team] → Execute + Modify
└── [Leadership] → Full access
```

---

## Troubleshooting in Cowork

### Skill Not Found

**Problem**: Can't find denim-trend-analyzer in skill marketplace

**Solution**:
1. Make sure skill is published
2. Sync Cowork package manager: `cowork sync`
3. Clear cache: `cowork cache clear`
4. Restart Cowork

### API Keys Not Working

**Problem**: Skill says "Invalid API key"

**Solution**:
```
/denim-trend-analyzer --update-keys
```

Re-enter both keys (copy exactly, no spaces).

### Scheduled Task Doesn't Run

**Problem**: Task appears enabled but never runs

**Solution**:
1. Check cron expression: `0 8 * * 1`
2. Verify Cowork is running at that time
3. Check logs: Scheduled Tasks → Logs
4. Restart Cowork
5. Re-create the task

### Report Not Appearing

**Problem**: Run completes but no report file

**Solution**:
1. Check file browser: outputs/ directory
2. Check logs for errors
3. Run manually: `/denim-trend-analyzer --full --verbose`
4. See SETUP.md troubleshooting

---

## Best Practices in Cowork

### Scheduling

✅ **Do:**
- Run at consistent time (8 AM Monday)
- Set 30-min timeout (runs usually 10-12 min)
- Enable notifications
- Archive old reports monthly

❌ **Don't:**
- Run multiple times simultaneously (wastes API credits)
- Change API keys during run
- Delete outputs/ directory
- Modify src/ files during scheduled run

### Team Workflow

```
Monday 8 AM
    ↓
Automated analysis runs
    ↓
Report in outputs/
    ↓
Notification to team
    ↓
Team reviews in Cowork
    ↓
Share key findings
    ↓
Designers create samples
    ↓
Update next week's focus
```

### Updating Prompts

1. **Monday after analysis**: Review results
2. **Tuesday**: Update `src/prompts.py` if needed
3. **Test**: Run `--dry-run` to preview
4. **Next Monday**: New analysis uses updated prompts

---

## Advanced Integration

### Integrate with Other Skills

```yaml
denim-analyzer:
  outputs: outputs/project_sent_denim_v1.md
  
  triggers:
    - send-email-digest (Monday 9 AM)
    - post-to-slack (Monday 9 AM)
    - update-dashboard (Monday 10 AM)
```

### Connect to External Tools

```bash
# After analysis completes:
- Upload to cloud storage
- Email to buyers
- Post summary to Slack
- Update dashboard
- Trigger sample creation
```

### Create Custom Reports

```python
# In a custom Cowork skill:
from denim_analyzer import load_report

report = load_report('outputs/project_sent_denim_v1.md')
executive_summary = report.executive_summary
concepts = report.cad_concepts

# Use in custom skill/workflow
```

---

## FAQ: Cowork-Specific Questions

### Q: Can I run this manually from Cowork?

**A:** Yes!
```
/denim-trend-analyzer --full
```

Or scheduled:
```
/denim-trend-analyzer --full --schedule "0 8 * * 1"
```

### Q: Can I modify the analysis without touching code?

**A:** Yes, two ways:
1. Edit `src/prompts.py` directly in Cowork editor
2. Use CLI parameters: `--categories sustainable,vintage`

### Q: Where are my API keys stored?

**A:** Securely in Cowork's vault. Never logged, never exposed.

### Q: Can I delete old reports?

**A:** Yes, but recommended to archive first:
1. Download to computer
2. Delete from Cowork
3. Keeps last 8-12 weeks in `outputs/`

### Q: How do I share reports with non-Cowork team?

**A:** Export and share:
1. Right-click report → Download
2. Email or upload to shared drive
3. Or grant Cowork access to external users

### Q: Can multiple people run this?

**A:** Yes! Each person:
1. Installs skill
2. Adds their own API keys
3. Gets their own outputs/
4. Can share outputs with team

### Q: What if I want to run this on a different schedule?

**A:** Change cron expression:
```
Daily:    0 8 * * *
Weekdays: 0 8 * * 1-5
Twice/wk: 0 8 * * 1,4
```

---

## Next Steps

1. ✅ Install skill in Cowork
2. ✅ Set up API keys
3. ✅ Run first analysis manually
4. ✅ Create scheduled task (Monday 8 AM)
5. ✅ Share reports with team
6. ✅ (Optional) Customize prompts
7. ✅ (Optional) Set up integrations

---

**You're ready to use Denim Trend Analyzer in Cowork!** 🧵✨

Questions? See:
- [README.md](./README.md) - Full overview
- [SCHEDULER.md](./SCHEDULER.md) - Scheduling details
- [NON_TECHNICAL_GUIDE.md](./NON_TECHNICAL_GUIDE.md) - Setup help
