# 📁 Project Structure

Complete overview of the Denim Trend Analyzer project structure and file purposes.

## Directory Layout

```
denim-trend-analyzer/
├── README.md                    ← Start here! Project overview
├── QUICKSTART.md                ← 5-minute setup guide
├── SETUP.md                     ← Detailed installation & troubleshooting
├── SCHEDULER.md                 ← Weekly automation setup
├── LICENSE                      ← MIT License
│
├── pyproject.toml              ← Dependencies & project metadata
├── .python-version             ← Python version specification (3.10)
├── .env.example                ← Environment variables template
├── .gitignore                  ← Git ignore rules
│
├── src/                        ← Python source code
│   ├── __init__.py             ← Package init
│   ├── config.py               ← Configuration & API setup
│   ├── data_models.py          ← Pydantic schemas
│   ├── prompts.py              ← LLM agent prompts (5 agents)
│   ├── main.py                 ← Agent definitions & pipeline
│   ├── denim_analyzer.py       ← CLI entry point (main execution)
│   └── pinterest_collector.py  ← Data collection (Tavily/Pinterest)
│
├── tests/                      ← Test suite (Phase 2+)
│   └── __init__.py
│
└── outputs/                    ← Generated reports & concepts (auto-created)
    ├── project_sent_denim_v1.md           ← Weekly report
    ├── denim_cad_concepts_v1/             ← Design concepts
    │   ├── concept_01_vintage_wide_leg.txt
    │   ├── concept_02_smart_casual_hybrid.txt
    │   └── ...
    └── analysis_metadata_v1.json          ← Run metadata
```

## File Purposes

### Documentation

| File | Purpose |
|------|---------|
| `README.md` | Main project documentation, features, usage |
| `QUICKSTART.md` | 5-minute setup guide for first-time users |
| `SETUP.md` | Detailed installation, troubleshooting, system requirements |
| `SCHEDULER.md` | Integration with Cowork's weekly scheduler |
| `PROJECT_STRUCTURE.md` | This file - complete project layout |

### Configuration

| File | Purpose |
|------|---------|
| `pyproject.toml` | Dependencies, Python version, project metadata |
| `.python-version` | Specifies Python 3.10.12 |
| `.env.example` | Template for environment variables (copy to `.env`) |
| `.env` | **Your actual API keys (NOT in git, ignored by .gitignore)** |
| `.gitignore` | Files to exclude from git (outputs/, .env, __pycache__, etc.) |

### Source Code (`src/`)

| File | Purpose | Phase |
|------|---------|-------|
| `__init__.py` | Package initialization | 1 ✅ |
| `config.py` | Load environment, validate API keys | 1 ✅ |
| `data_models.py` | Pydantic schemas (TrendPin, CADConcept, etc.) | 1 ✅ |
| `prompts.py` | LLM prompt templates for 5 agents | 1 ✅ |
| `main.py` | Agent definitions & sequential pipeline | 1 ✅ |
| `denim_analyzer.py` | CLI entry point, report generation | 1 ✅ |
| `pinterest_collector.py` | Data collection (Tavily now, Pinterest later) | 1 ✅ |

### Tests (`tests/`)

| File | Purpose | Phase |
|------|---------|-------|
| `__init__.py` | Test package initialization | 1 ✅ |
| `test_data_models.py` | Validate Pydantic schemas | 2 |
| `test_agents.py` | Test agent execution | 2 |
| `test_pipeline.py` | Integration tests | 2 |

### Outputs (`outputs/`)

Auto-created after first run:

| File | Purpose |
|------|---------|
| `project_sent_denim_v1.md` | Weekly trend analysis report |
| `denim_cad_concepts_v1/` | 5 design concept briefs (numbered) |
| `analysis_metadata_v1.json` | Run summary (timestamp, counts) |
| `project_sent_denim_v2.md` | Previous week (auto-rotated) |
| `denim_cad_concepts_v2/` | Previous concepts |

## Phase Progress

### ✅ Phase 1: Foundation (COMPLETE)
- [x] `config.py` - Configuration & validation
- [x] `data_models.py` - Data structure schemas
- [x] `prompts.py` - Agent prompt templates (5 prompts)
- [x] `main.py` - Agent definitions & pipeline
- [x] `denim_analyzer.py` - CLI entry point
- [x] `pinterest_collector.py` - Data collection (Tavily fallback)
- [x] `pyproject.toml` - Dependencies
- [x] `.env.example` - API key template
- [x] `README.md` - Main documentation
- [x] `SETUP.md` - Detailed setup guide
- [x] `SCHEDULER.md` - Automation guide
- [x] `QUICKSTART.md` - 5-minute start
- [x] `.gitignore` - Git configuration

### Phase 2: Agent Implementation (NEXT)
- [ ] Implement DenimTrendCollectorAgent
- [ ] Implement TrendSynthesizerAgent
- [ ] Implement CADConceptGeneratorAgent
- [ ] Implement DenimCompetitorAnalyzerAgent
- [ ] Implement B2BReportGeneratorAgent
- [ ] Create test suite (`tests/test_agents.py`)
- [ ] Integration testing

### Phase 3: Scheduling & Automation
- [ ] Cowork scheduler integration
- [ ] Weekly cron setup (Monday 8 AM)
- [ ] Output versioning
- [ ] Notification system

### Phase 4: Pinterest API Integration (Optional)
- [ ] Pinterest Business Account setup
- [ ] API credential management
- [ ] Pinterest API client implementation
- [ ] Engagement metrics extraction

### Phase 5: Polish & Enhancements
- [ ] HTML/PDF export
- [ ] Trend history visualization
- [ ] Admin dashboard
- [ ] Email/Slack integration

## Dependencies

See `pyproject.toml` for complete list. Key packages:

```toml
google-adk>=0.1.0              # Agentic workflows
nebius (via google-adk)        # Qwen3-235B LLM
langchain-tavily>=0.1.0        # Web search
pydantic>=2.0.0                # Data validation
python-dotenv>=1.0.0           # Environment config
```

## How to Run

### Manual Execution

```bash
# Activate environment
source .venv/bin/activate

# Full analysis
python denim_analyzer.py --full

# Dry-run (test)
python denim_analyzer.py --dry-run

# Verbose output
python denim_analyzer.py --full --verbose
```

### Automated (Weekly)

See [SCHEDULER.md](SCHEDULER.md) for setup with Cowork.

## Git Workflow

```bash
# Initial setup
git init
git add .
git commit -m "feat: Phase 1 - Foundation for denim trend analyzer"

# Don't commit .env!
git update-index --assume-unchanged .env

# Make changes
git checkout -b feature/phase-2-agents
# ... make changes ...
git add src/
git commit -m "feat: Phase 2 - Implement analysis agents"
git push origin feature/phase-2-agents

# Create PR on GitHub
```

## Key Design Decisions

1. **Text-based CAD briefs** - Practical for B2B, not AI-generated images
2. **Tavily fallback** - Web search while Pinterest API approval pending
3. **Pydantic schemas** - Type safety & validation
4. **Sequential agents** - Clear workflow, easy to understand
5. **Weekly automation** - Consistent intel without manual work
6. **Modular structure** - Easy to modify prompts, add agents

## Common Commands

```bash
# Check Python version
python --version

# Validate configuration
python -c "from src.config import validate_config; validate_config()"

# Test imports
python -c "import src.main; print('✅ Imports OK')"

# Run analysis
python denim_analyzer.py --full

# View report
cat outputs/project_sent_denim_v1.md

# Check structure
tree -L 3 -I '__pycache__|*.egg-info'
```

## Environment Variables

See `.env.example` for template. Required for execution:

```env
# Required
NEBIUS_API_KEY=nebius_...
TAVILY_API_KEY=tvly_...

# Optional (Phase 4)
PINTEREST_API_KEY=...
PINTEREST_API_SECRET=...
PINTEREST_ACCESS_TOKEN=...

# System
OUTPUT_DIR=./outputs
LOG_LEVEL=INFO
```

## Performance

- **Full run**: 10-15 minutes
- **First run**: Slower (LLM initialization)
- **Subsequent runs**: 7-10 minutes
- **API costs**: ~$0.20-0.50 per week
- **Storage**: ~2 MB per weekly report

## Next Steps for Others

1. **Clone**: `git clone <url>`
2. **Setup**: Follow [QUICKSTART.md](QUICKSTART.md) (5 min)
3. **Verify**: Run `python denim_analyzer.py --dry-run`
4. **Deploy**: Follow [SCHEDULER.md](SCHEDULER.md) for weekly runs
5. **Customize**: Edit `src/prompts.py` to tune behavior

---

**Questions?** See the respective `.md` files:
- How do I run it? → [QUICKSTART.md](QUICKSTART.md)
- How do I install? → [SETUP.md](SETUP.md)
- How do I automate? → [SCHEDULER.md](SCHEDULER.md)
- What is this project? → [README.md](README.md)
