# 🔧 Detailed Setup Guide

Complete step-by-step instructions for getting the Denim Trend Analyzer running on your machine.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Get API Keys](#get-api-keys)
3. [Install Project](#install-project)
4. [Test Installation](#test-installation)
5. [Troubleshooting](#troubleshooting)

## System Requirements

### Operating System
- **macOS**: 10.14+ (Intel or Apple Silicon)
- **Linux**: Ubuntu 20.04+, Debian 11+, or equivalent
- **Windows**: Windows 10+ with WSL2 recommended

### Software
- **Python**: 3.10+ ([install here](https://www.python.org/downloads/))
- **Git**: 2.20+ ([install here](https://git-scm.com/downloads))
- **uv**: Latest ([install here](https://github.com/astral-sh/uv#installation))
- **Space**: ~500 MB for dependencies

### Check Your Setup

```bash
# Check Python version
python --version
# Expected: Python 3.10.x or higher

# Check Git version
git --version
# Expected: git version 2.20 or higher

# Check uv installation
uv --version
# Expected: uv 0.x.x
```

If any are missing, install them before proceeding.

## Get API Keys

### 1. Nebius AI (Required)

Nebius provides access to the Qwen3-235B language model.

```bash
# Step 1: Go to Nebius Console
# https://console.anthropic.com

# Step 2: Sign up or log in (free tier available)

# Step 3: Navigate to API Keys → Create New Key

# Step 4: Copy the API key
# Format: nebius_xxxxxxxxxxxxxxxxxxxxx

# Step 5: Save for later (don't share this!)
```

### 2. Tavily (Required)

Tavily powers web search and trend data extraction.

```bash
# Step 1: Go to Tavily
# https://tavily.com

# Step 2: Sign up (free tier: 1,000 searches/month)

# Step 3: Copy your API key from dashboard
# Format: tvly-xxxxxxxxxxxxxxxxxxxxx

# Step 4: Save for later
```

### 3. Pinterest API (Optional - Phase 4)

Only needed if you want real Pinterest trend data instead of web search fallback.

```bash
# Step 1: Create Pinterest Business Account
# https://business.pinterest.com

# Step 2: Apply for API access
# Go to: https://developers.pinterest.com
# Note: Approval may take 1-2 weeks

# Step 3: Create an OAuth app in Pinterest Developer Dashboard

# Step 4: Get credentials:
# - Client ID (API Key)
# - Client Secret
# - Access Token (generate after approval)

# Step 5: Save all three values
```

## Install Project

### Clone Repository

```bash
# Option A: If you have SSH key set up
git clone git@github.com:your-username/denim-trend-analyzer.git

# Option B: If using HTTPS
git clone https://github.com/your-username/denim-trend-analyzer.git

# Navigate to project
cd denim-trend-analyzer
```

### Configure Environment

```bash
# Copy the example .env file
cp .env.example .env

# Open .env in your editor
# macOS/Linux:
nano .env
# or use your editor: code .env, vim .env, etc.

# Windows:
notepad .env
```

### Fill in Your API Keys

Edit `.env` and add your keys:

```env
NEBIUS_API_KEY=nebius_YOUR_KEY_HERE
TAVILY_API_KEY=tvly_YOUR_KEY_HERE

# Leave Pinterest empty for now (Phase 4)
PINTEREST_API_KEY=
PINTEREST_API_SECRET=
PINTEREST_ACCESS_TOKEN=

OUTPUT_DIR=./outputs
LOG_LEVEL=INFO
```

**⚠️ Important**: Never commit `.env` to Git! It's in `.gitignore` for your safety.

### Install Dependencies

```bash
# Using uv (recommended, fast)
uv sync

# This will:
# 1. Create virtual environment (.venv)
# 2. Install all dependencies
# 3. Install development tools (pytest, black, etc.)

# If you get permission errors on macOS/Linux, try:
# chmod +x .venv/bin/activate
```

### Activate Virtual Environment

```bash
# macOS/Linux:
source .venv/bin/activate

# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Windows (Command Prompt):
.venv\Scripts\activate.bat

# You should see (.venv) at the start of your terminal prompt
```

## Test Installation

### Quick Health Check

```bash
# Verify all imports work
python -c "
import google.adk
import dotenv
import pydantic
from langchain_tavily import TavilySearch
print('✅ All imports successful!')
"
```

### Test API Connectivity

```bash
# Test Nebius connection
python -c "
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv

load_dotenv()
llm = LiteLlm(
    model='nebius/Qwen/Qwen3-235B-A22B-Instruct-2507',
    api_key=os.getenv('NEBIUS_API_KEY')
)
print('✅ Nebius connection successful!')
"

# Test Tavily connection
python -c "
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv()
tavily = TavilySearch(
    max_results=1,
    search_depth='basic'
)
result = tavily.run('denim fashion trends 2026')
print('✅ Tavily connection successful!')
print(f'Sample result: {result[:100]}...')
"
```

### Run First Analysis

```bash
# Dry-run (tests with minimal data)
python denim_analyzer.py --dry-run

# Expected output:
# → Analyzing denim trends...
# → Generating CAD concepts...
# → Creating report...
# ✅ Report saved to: outputs/project_sent_denim_v1.md

# Check the output file
cat outputs/project_sent_denim_v1.md
```

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'google.adk'"

**Problem**: Dependencies not installed correctly

**Solution**:
```bash
# Re-install dependencies
uv sync --force

# Or manually activate environment
source .venv/bin/activate
pip install google-adk langchain-tavily
```

### Error: "NEBIUS_API_KEY not found"

**Problem**: .env file not created or API key not set

**Solution**:
```bash
# Make sure .env exists
ls -la .env

# Make sure it contains NEBIUS_API_KEY
grep NEBIUS_API_KEY .env

# If not, edit .env and add it:
cp .env.example .env
# Then edit .env with your keys
```

### Error: "Tavily search failed: Unauthorized"

**Problem**: Invalid Tavily API key

**Solution**:
```bash
# Check Tavily API key is correct
# Go to: https://tavily.com/app/home
# Copy exact key from dashboard

# Update .env with correct key
nano .env

# Test again
python -c "
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv()
tavily = TavilySearch()
result = tavily.run('test')
print('✅ Working!')
"
```

### Error: "python: No such file or directory" (macOS)

**Problem**: Python not in PATH

**Solution**:
```bash
# Check if python3 exists
python3 --version

# If yes, use python3 instead:
python3 denim_analyzer.py --dry-run

# Or create alias:
alias python=python3
```

### Error: "Permission denied: .venv/bin/activate"

**Problem**: Virtual environment scripts not executable

**Solution**:
```bash
# Make executable
chmod +x .venv/bin/activate

# Or use:
. .venv/bin/activate  # Note the dot instead of source
```

### Error: "Qwen3 model not available"

**Problem**: Nebius account doesn't have access to Qwen3-235B

**Solution**:
```bash
# Check Nebius console for available models
# https://console.anthropic.com/models

# Edit config.py and try a different model:
# - "nebius/meta-llama/Llama-3.1-405B-Instruct"
# - Other available Nebius models

# Or use Claude API instead:
# Edit config.py: model="claude-3-opus-20250514"
```

### Error: "Connection timeout"

**Problem**: Network issue or API service down

**Solution**:
```bash
# Check internet connection
ping google.com

# Check API status:
# - Nebius: https://console.anthropic.com/status
# - Tavily: https://status.tavily.com

# Retry with longer timeout:
python denim_analyzer.py --timeout 60 --dry-run

# Check your firewall/VPN settings
```

## Next Steps

Once setup is complete:

1. **Read the README**: Back to [README.md](README.md) for overview
2. **Run Your First Analysis**: `python denim_analyzer.py --full`
3. **Set Up Scheduler**: See [SCHEDULER.md](SCHEDULER.md) for weekly automation
4. **Explore Output**: Check `outputs/project_sent_denim_v1.md`
5. **Customize**: Edit `prompts.py` to tune agent behavior

## Getting Help

- **Installation Issues**: Check [Troubleshooting](#troubleshooting) above
- **API Key Issues**: Revisit [Get API Keys](#get-api-keys)
- **Code Issues**: Check GitHub Issues or contact the team
- **Feature Requests**: Create a GitHub Discussion

## System-Specific Notes

### macOS (Apple Silicon M1/M2/M3)

```bash
# Ensure Python is ARM-native
python -c "import platform; print(platform.processor())"
# Expected: arm (not x86_64)

# If needed, use native Python installer from python.org
# NOT Homebrew (may install x86 version)
```

### Linux (Ubuntu/Debian)

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3.10 python3.10-venv python3.10-dev git

# Then follow the normal install steps
```

### Windows (WSL2 Recommended)

```bash
# Enable WSL2
wsl --install

# Install Ubuntu 22.04 from Microsoft Store
# Then follow Linux instructions inside WSL2

# Or use native Python:
# Download from https://www.python.org/downloads/
# Run installer, make sure to check "Add Python to PATH"
```

---

**Having trouble?** Open an issue with:
- Your operating system and Python version
- Full error message (including stack trace)
- Output of `python -c "import sys; print(sys.version)"`
