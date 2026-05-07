# ⚡ Quick Start (5 minutes)

Get the Denim Trend Analyzer running in less than 5 minutes.

## 1. Clone & Setup

```bash
# Clone the repo
git clone <your-repo-url>
cd denim-trend-analyzer

# Copy environment template
cp .env.example .env
```

## 2. Add API Keys

Edit `.env` and add your keys:

```bash
# Open in your editor
nano .env
```

Add these two (required):
```env
NEBIUS_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

Get keys from:
- **Nebius**: https://console.anthropic.com
- **Tavily**: https://tavily.com

## 3. Install & Run

```bash
# Install dependencies (uses uv)
uv sync

# Activate environment
source .venv/bin/activate

# Run first analysis
python denim_analyzer.py --dry-run
```

## Expected Output

```
🧵 Denim Trend Analyzer
✅ Analysis complete!

📄 Report: outputs/project_sent_denim_v1.md
📊 Trends collected: 15
🎨 CAD concepts: 5
🏆 Competitors analyzed: 8
```

Check the report:
```bash
cat outputs/project_sent_denim_v1.md
```

## Next Steps

- **Full Analysis**: `python denim_analyzer.py --full`
- **Setup Scheduler**: See [SCHEDULER.md](SCHEDULER.md)
- **Detailed Setup**: See [SETUP.md](SETUP.md)
- **Troubleshoot**: See [README.md](README.md#troubleshooting)

## Troubleshooting Quick Fixes

| Issue | Fix |
|-------|-----|
| `NEBIUS_API_KEY not found` | Run `cp .env.example .env` and edit |
| `ModuleNotFoundError` | Run `uv sync` again |
| `Permission denied` | Run `chmod +x .venv/bin/activate` |
| Slow first run | Normal - LLM is initializing |

## Common Commands

```bash
# Test installation
python -c "import src.config; src.config.validate_config()"

# Run full analysis
python denim_analyzer.py --full

# Show help
python denim_analyzer.py --help

# Enable debug logging
python denim_analyzer.py --full --verbose
```

---

**Full docs**: See [README.md](README.md) and [SETUP.md](SETUP.md)
