# Denim Trend Analyzer Skill

**AI-powered weekly denim product analysis and CAD concept generation for B2B retail.**

## Metadata

```yaml
name: "Denim Trend Analyzer"
id: "denim-trend-analyzer"
version: "0.1.0"
category: "product-development"
tags:
  - denim
  - fashion
  - trends
  - product-development
  - market-analysis
  - cad-concepts
author: "Damo Ventures"
license: "MIT"
```

## What This Skill Does

Automatically analyzes trending denim products and generates:
- 📊 **Trend Analysis**: Top 3-5 denim trends with demand signals
- 🎨 **5 CAD Concepts**: Design briefs with specs, costs, and margins
- 🏆 **Competitor Analysis**: Market landscape and positioning gaps
- 📈 **B2B Insights**: Retail buyer recommendations and margins
- 📁 **Weekly Reports**: Markdown reports ready to share

Perfect for **fashion product developers, B2B retail buyers, and supply chain professionals**.

## Features

✅ **Automated Trend Collection** - Finds trending denim from web + Pinterest  
✅ **Smart Analysis** - AI synthesizes trends into actionable concepts  
✅ **Cost-Aware Design** - Each concept includes margin estimates  
✅ **Competitive Intelligence** - Identifies market gaps vs. competitors  
✅ **Weekly Automation** - Integrates with Cowork scheduler  
✅ **Easy Setup** - Works on Mac, Windows, Linux  
✅ **Non-Technical Friendly** - Setup wizard for all skill levels  

## Quick Start

### 1. Set Up (First Time)

```bash
cd denim-trend-analyzer

# Mac users
bash setup.sh

# Windows users
python setup.py

# You'll be asked for 2 free API keys:
# - Nebius (https://console.anthropic.com)
# - Tavily (https://tavily.com)
```

### 2. Run Analysis

```bash
python denim_analyzer.py --full
```

**Output:**
- `outputs/project_sent_denim_v1.md` - Full report
- `outputs/denim_cad_concepts_v1/` - 5 design concepts
- `outputs/analysis_metadata_v1.json` - Run info

### 3. Weekly Automation (Optional)

In Cowork:
```
Create Scheduled Task
├── Schedule: "0 8 * * 1" (Monday 8 AM)
├── Command: "python denim_analyzer.py --full"
└── Notifications: On completion
```

See [SCHEDULER.md](./SCHEDULER.md) for details.

## System Requirements

- **Python**: 3.10+
- **OS**: Mac, Windows, or Linux
- **API Keys**: 2 free accounts (Nebius + Tavily)
- **Time**: 10 minutes setup, 1 minute weekly

## Installation

### Option 1: Automated Setup (Recommended)

```bash
# Mac
bash setup.sh

# Windows
python setup.py
```

Guides through everything automatically.

### Option 2: Manual Setup

```bash
# Clone/download project
cp .env.example .env
nano .env  # Add API keys

# Install
uv sync

# Run
python denim_analyzer.py --full
```

See [SETUP.md](./SETUP.md) for troubleshooting.

## Usage

### Basic Analysis

```bash
# Full analysis with fresh data
python denim_analyzer.py --full

# Test run (minimal data)
python denim_analyzer.py --dry-run

# Verbose output
python denim_analyzer.py --full --verbose
```

### Weekly Automation

In Cowork scheduled tasks:
```
Task Name: Weekly Denim Analysis
Schedule: Every Monday 8:00 AM
Command: python denim_analyzer.py --full
Notify: On completion
```

See [SCHEDULER.md](./SCHEDULER.md) for step-by-step setup.

### Customization

Edit `src/prompts.py` to change:
- Denim style categories analyzed
- Competitor focus
- Report format
- Design concept themes

Re-run analysis to see changes immediately.

## Output Example

### Report Structure

```markdown
# Weekly Denim Trend Analysis Report
**Week of: May 7, 2026**

## Executive Summary
Top 3 trends identified, margin opportunities, positioning insights

## Trend Analysis
### Trend 1: Vintage-Inspired Wide-Leg
- Demand signal: 76%
- Target: Women 25-35
- Retail range: £35-55

## 5 CAD Concepts
### Concept 1: Vintage-Inspired Wide Leg
- Silhouette: High-rise, 23" leg opening
- Fabric: 100% organic cotton, 14 oz
- Estimated margin: 62%
- Lead time: 4 weeks

### Concept 2-5: [Similar format]

## Competitor Landscape
- Key competitors analyzed
- Feature gaps identified
- Whitespace opportunities

## B2B Retail Insights
- Margin expectations
- Buyer sentiment
- Production recommendations
```

## API Keys & Costs

### Nebius (Required)
- **Cost**: Free tier generous (100+ requests)
- **Get it**: https://console.anthropic.com
- **Uses**: Qwen3-235B AI model for analysis

### Tavily (Required)
- **Cost**: Free tier 1,000 searches/month
- **Get it**: https://tavily.com
- **Uses**: Web search for trend data

### Pinterest (Optional - Phase 4)
- **Cost**: Free API access
- **Get it**: https://developers.pinterest.com
- **Uses**: Real denim trend data (future enhancement)

**Total weekly cost**: ~$0.20-0.50 (minimal)

## Performance

| Task | Time | Notes |
|------|------|-------|
| First run | 15-20 min | LLM model loads |
| Subsequent runs | 8-12 min | Faster after initial |
| Weekly automated | Auto | Runs while you sleep |
| Report generation | 2-5 min | Included in above |

## Troubleshooting

### "Python not found"
→ Install from https://www.python.org/downloads/

### "API key error"
→ Re-copy your API key (no spaces, exact value)

### "Command not found: uv"
→ See SETUP.md for pip installation

### Analysis running slow
→ Normal first time! Subsequent runs are faster.

## Documentation

| Document | For | Purpose |
|----------|-----|---------|
| [NON_TECHNICAL_GUIDE.md](./NON_TECHNICAL_GUIDE.md) | Non-technical users | Step-by-step in plain English |
| [QUICKSTART.md](./QUICKSTART.md) | Tech-savvy users | 5-minute setup |
| [SETUP.md](./SETUP.md) | Everyone | Detailed troubleshooting |
| [SCHEDULER.md](./SCHEDULER.md) | DevOps/Automation | Weekly scheduling |
| [HOW_TO_SHARE.md](./HOW_TO_SHARE.md) | Team leads | Distribution & onboarding |
| [README.md](./README.md) | Decision makers | Full project overview |

## Roadmap

### ✅ Phase 1: Foundation (Complete)
- Configuration system
- Data models
- Agent prompts
- CLI interface
- Documentation

### Phase 2: Agent Implementation
- Implement 5 analysis agents
- Test end-to-end
- Optimize performance

### Phase 3: Cowork Integration
- Scheduler setup
- Notification system
- Output versioning

### Phase 4: Pinterest API
- Real Pinterest data
- Engagement metrics
- Trend validation

### Phase 5: Polish
- HTML/PDF export
- Trend dashboards
- Email/Slack integration

## For Cowork Users

### Discovery

This skill helps you:
- 📊 Analyze trending denim products automatically
- 🎨 Generate 5 design concepts with margin estimates
- 🏆 Understand competitive landscape
- 📈 Make data-driven product decisions
- ⏰ Run weekly analysis on schedule

### Installation in Cowork

1. **Enable the skill** in Cowork settings
2. **Run setup**: See Quick Start section above
3. **Add API keys** (Nebius + Tavily, both free)
4. **First run**: `python denim_analyzer.py --full`
5. **Weekly automation**: Follow SCHEDULER.md

### Integration with Cowork Tasks

The skill works seamlessly with Cowork's task system:
- Create scheduled tasks that run weekly
- Track analysis runs in session history
- Store reports in Cowork file system
- Share outputs with team

## Use Cases

### Product Development Teams
Generate weekly denim design concepts based on real trends.

### B2B Retail Buyers
Understand denim trends and competitive gaps before buying meetings.

### Supply Chain Managers
Plan production timelines and material sourcing based on demand signals.

### Fashion Analysts
Track trend velocity and market movements week-over-week.

### Fashion Import Businesses
Stay ahead of retail buyer expectations with automated trend intelligence.

## Contributing

To improve this skill:

1. Fork the repository
2. Create a feature branch
3. Make changes and test
4. Submit a pull request

Areas for contribution:
- Phase 2: Implement agent logic
- Phase 4: Pinterest API integration
- Phase 5: Additional features
- Documentation improvements
- Bug fixes

## Support

- **Non-technical help**: See NON_TECHNICAL_GUIDE.md
- **Technical help**: See SETUP.md
- **Questions**: Check README.md FAQ
- **Issues**: GitHub issues
- **Discussions**: GitHub discussions

## License

MIT License - Free to use and modify. See [LICENSE](./LICENSE)

## Author

**Damo Ventures** - B2B clothing import business using AI for competitive advantage.

---

## Getting Started Right Now

Pick your path:

**👤 Non-technical?**
→ Read [NON_TECHNICAL_GUIDE.md](./NON_TECHNICAL_GUIDE.md)

**⚡ Tech-savvy?**
→ Read [QUICKSTART.md](./QUICKSTART.md)

**🤖 Want automation?**
→ Read [SCHEDULER.md](./SCHEDULER.md)

**📚 Want details?**
→ Read [README.md](./README.md)

---

**Start analyzing denim trends now!** 🧵✨
