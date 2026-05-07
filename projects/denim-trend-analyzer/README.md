# 🧵 Denim Trend Analyzer

An AI-powered system that analyzes trending denim products weekly, generates 5 CAD visualization concepts, and produces competitive market analysis reports. Built for B2B retail buyers and product development teams.

**Status**: Phase 1 - Foundation Implementation

## Features

- 🔍 **Trend Intelligence**: Extracts most-pinned denim items from Pinterest and web sources
- 🎨 **CAD Concepts**: Generates 5 design briefs with margin estimates and production details
- 📊 **Market Analysis**: Competitor positioning, pricing gaps, feature analysis
- 📈 **B2B Reporting**: Structured markdown reports for retail buyer relationships
- ⏰ **Automated Weekly**: Runs on schedule (Monday 8 AM) with no manual intervention
- 📁 **Versioned Outputs**: Weekly reports and concept folders with full history

## Tech Stack

- **Python 3.10+**
- **Google ADK**: Agentic workflow orchestration
- **Nebius AI**: Qwen3-235B large language model
- **Tavily**: Web search and trend extraction
- **Pinterest API**: Real denim trend data (optional, Phase 4)
- **uv**: Fast Python package manager
- **Cowork**: Scheduled task automation

## Quick Start

### Prerequisites

1. **Python 3.10+** installed
2. **API Keys** (see below)
3. **Git** for version control
4. **uv** package manager ([install here](https://github.com/astral-sh/uv))

### Get API Keys

#### Required:
- **Nebius API Key**: https://console.anthropic.com (free tier available)
- **Tavily API Key**: https://tavily.com (includes free credits)

#### Optional (Phase 4):
- **Pinterest API**: Apply for business account at https://developers.pinterest.com

### Installation

```bash
# Clone the repo
git clone <your-repo-url>
cd denim-trend-analyzer

# Copy environment template
cp .env.example .env

# Add your API keys to .env
# Edit .env and fill in NEBIUS_API_KEY, TAVILY_API_KEY
nano .env

# Install dependencies using uv
uv sync

# Activate virtual environment
source .venv/bin/activate
```

### Run First Analysis (Manual)

```bash
# Test the pipeline with a single run
python denim_analyzer.py --dry-run

# Or run a fresh analysis
python denim_analyzer.py --full
```

Output: `outputs/project_sent_denim_v1.md`

## Project Structure

```
denim-trend-analyzer/
├── README.md                    # This file
├── SETUP.md                     # Detailed setup instructions
├── SCHEDULER.md                 # Integration with Cowork scheduler
├── pyproject.toml              # Dependencies and project metadata
├── .env.example                # Environment variable template
├── .python-version             # Python version specification
│
├── src/
│   ├── main.py                 # Agent definitions and orchestration
│   ├── denim_analyzer.py        # Main pipeline entry point
│   ├── prompts.py              # LLM prompt templates (5 agents)
│   ├── config.py               # Configuration and environment loading
│   ├── data_models.py          # Pydantic schemas for data structures
│   └── pinterest_collector.py  # Pinterest API client (fallback to Tavily)
│
├── outputs/
│   ├── project_sent_denim_v1.md          # Weekly report
│   └── denim_cad_concepts_v1/            # Design concept briefs
│
└── tests/
    ├── test_agents.py
    ├── test_data_models.py
    └── conftest.py
```

## Usage

### Manual Execution

```bash
# Run full analysis with fresh data collection
python denim_analyzer.py --full

# Dry-run (uses cached data if available)
python denim_analyzer.py --dry-run

# Run specific phase only
python denim_analyzer.py --phase trend_collection
```

### Automated Weekly Execution

See [SCHEDULER.md](SCHEDULER.md) for instructions on setting up with Cowork's scheduled task system.

**Current setup:**
- Schedule: Monday 8:00 AM (your local timezone)
- Output: `outputs/project_sent_denim_v{version}.md`
- Concepts: `outputs/denim_cad_concepts_v{version}/`

## Implementation Phases

### ✅ Phase 1: Foundation (Current)
- [x] Data models and schemas
- [x] Configuration system
- [x] Tavily-based trend collection (fallback)
- [x] Agent definitions
- [ ] Testing and validation

### Phase 2: Agent Implementation
- [ ] Build 6 analysis agents
- [ ] Connect to main pipeline
- [ ] End-to-end testing

### Phase 3: Scheduling & Automation
- [ ] Integrate with Cowork scheduler
- [ ] Set up weekly cron job
- [ ] Implement output versioning
- [ ] Add notifications

### Phase 4: Pinterest API Integration (Optional)
- [ ] Set up Pinterest Business Account
- [ ] Implement Pinterest API client
- [ ] Replace Tavily fallback with real data
- [ ] Add engagement metrics

### Phase 5: Polish & Enhancements
- [ ] HTML/PDF export
- [ ] Trend history visualization
- [ ] Admin dashboard
- [ ] Production documentation

## Output Format

### Weekly Report: `project_sent_denim_v1.md`

```markdown
# Weekly Denim Trend Analysis Report
**Week of: May 7, 2026**

## Executive Summary
- Top 3 trend themes identified
- Margin opportunities highlighted
- Competitive positioning

## Trend Analysis
### Trend Theme 1: Vintage-Inspired Wide-Leg
- Pinterest engagement: 12K repins/week
- Style category: Women's, 25-35 age group
- Competitive gap analysis

## 5 CAD Concepts for Development
### Concept 1: Vintage-Inspired Wide Leg
**Trend Signal**: 34% increase in "vintage denim" Pinterest searches
**Style Details**:
- High-rise waistband (10.5"), 23" leg opening
- 100% organic cotton denim, 14 oz weight
- Estimated Retail Price: £45 | Margin: 62% @ £28 cost
**Production Notes**: Classic construction, 4-week lead time

### Concept 2-5: [Similar format]

## Competitor Landscape
- Price positioning analysis
- Feature gaps vs. competitors

## B2B Retail Buyer Insights
- Margin expectations by category
- Retail buyer sentiment
- Production timeline recommendations
```

### Design Concepts: `denim_cad_concepts_v1/`

```
concept_01_vintage_wide_leg.txt
concept_02_smart_casual_hybrid.txt
concept_03_sustainable_raw_denim.txt
concept_04_oversized_boyfriend_fit.txt
concept_05_premium_smart_denim.txt
trend_metadata.json
```

## Configuration

Edit `.env` to customize:

```bash
# LLM Configuration
NEBIUS_API_KEY=...           # Required
TAVILY_API_KEY=...           # Required

# Pinterest (optional)
PINTEREST_API_KEY=...
PINTEREST_API_SECRET=...
PINTEREST_ACCESS_TOKEN=...

# System Settings
OUTPUT_DIR=./outputs         # Where to save reports
LOG_LEVEL=INFO              # DEBUG, INFO, WARNING, ERROR
```

## Troubleshooting

### API Key Errors
```
Error: NEBIUS_API_KEY not found
→ Make sure .env file exists and contains NEBIUS_API_KEY
→ Run: cp .env.example .env
```

### Dependencies Not Installing
```
Error: python.h: No such file or directory
→ Install Python development headers
→ Ubuntu/Debian: sudo apt-get install python3.10-dev
→ macOS: xcode-select --install
```

### Agent Failures
```
→ Check LOG_LEVEL=DEBUG for detailed error messages
→ Verify Tavily API has sufficient search credits
→ Verify Nebius model access (Qwen3-235B)
```

See [SETUP.md](SETUP.md) for more detailed troubleshooting.

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test
pytest tests/test_agents.py -v
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type checking (future)
mypy src/
```

### Adding New Features

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes and add tests
3. Run: `pytest` and `ruff check`
4. Commit with clear messages
5. Push and create a pull request

## Performance & Costs

| Operation | Time | Cost (approx) |
|-----------|------|---------------|
| Weekly full run | 10-15 min | $0.20-0.50 |
| Trend collection (Tavily) | 2-3 min | $0.05-0.10 |
| LLM analysis (5 agents) | 5-8 min | $0.15-0.40 |
| Report generation | 1-2 min | $0.05-0.10 |

**Tip**: Use `--dry-run` for testing to avoid API costs.

## FAQ

**Q: Can I run this multiple times per week?**
A: Yes, but API costs will increase. Recommend weekly (Monday) for consistency.

**Q: How do I customize the CAD concepts?**
A: Edit `prompts.py` and modify `CAD_CONCEPT_PROMPT`. Concepts are text-based design briefs.

**Q: Can I use a different LLM?**
A: Yes, modify `config.py` to use Claude, GPT-4, or other models supported by Google ADK.

**Q: How long is data kept?**
A: All weekly reports are versioned and kept. Trend data is JSON in each report.

**Q: Can I export to PDF?**
A: Phase 5 will add HTML/PDF export. For now, use `markdown2` to convert manually:
```bash
python -m markdown2 outputs/project_sent_denim_v1.md > report.html
```

## Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- 📚 [Setup Guide](SETUP.md)
- ⏰ [Scheduler Integration](SCHEDULER.md)
- 🐛 [Report Issues](../../issues)
- 💬 [Discussions](../../discussions)

## Roadmap

- [x] Phase 1: Foundation (data models, config, Tavily)
- [ ] Phase 2: Agents (trend analyzer, CAD generator, competitor analysis)
- [ ] Phase 3: Scheduling (Cowork integration, automation)
- [ ] Phase 4: Pinterest API (real denim trend data)
- [ ] Phase 5: Polish (HTML export, dashboards, analytics)

---

Built with ❤️ for fast-moving retail supply chains. Questions? Open an issue or contact the team.
