#!/bin/bash
# Denim Trend Analyzer - Automated Setup Script
# For non-technical users: just run this script!

set -e

echo "🧵 Denim Trend Analyzer - Setup Wizard"
echo "======================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Python is installed
echo "⏳ Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found${NC}"
    echo "Please install Python 3.10+ from https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo -e "${GREEN}✅ Python $PYTHON_VERSION found${NC}"
echo ""

# Check if uv is installed
echo "⏳ Checking uv package manager..."
if ! command -v uv &> /dev/null; then
    echo -e "${YELLOW}⚠️  uv not found, installing...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$PATH:$HOME/.cargo/bin"
fi
echo -e "${GREEN}✅ uv ready${NC}"
echo ""

# Get API keys from user
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "🔑 API KEYS SETUP"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "You need 2 API keys to run this. Get them free from:"
echo "  1. Nebius: https://console.anthropic.com"
echo "  2. Tavily: https://tavily.com"
echo ""

read -p "Enter your Nebius API Key: " NEBIUS_KEY
if [ -z "$NEBIUS_KEY" ]; then
    echo -e "${RED}❌ Nebius API key is required${NC}"
    exit 1
fi

read -p "Enter your Tavily API Key: " TAVILY_KEY
if [ -z "$TAVILY_KEY" ]; then
    echo -e "${RED}❌ Tavily API key is required${NC}"
    exit 1
fi

echo -e "${GREEN}✅ API keys saved${NC}"
echo ""

# Create .env file
echo "⏳ Creating .env configuration file..."
cat > .env << EOF
NEBIUS_API_KEY=$NEBIUS_KEY
TAVILY_API_KEY=$TAVILY_KEY

OUTPUT_DIR=./outputs
LOG_LEVEL=INFO
EOF

chmod 600 .env  # Protect with restricted permissions
echo -e "${GREEN}✅ Configuration saved (.env file)${NC}"
echo ""

# Install dependencies
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "📦 INSTALLING DEPENDENCIES"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "This may take a few minutes..."
echo ""

uv sync

echo -e "${GREEN}✅ Dependencies installed${NC}"
echo ""

# Test run
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "🧪 TESTING INSTALLATION"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

source .venv/bin/activate

echo "Testing imports..."
python3 -c "from src.config import validate_config; validate_config(); print('✅ Configuration valid')" || {
    echo -e "${RED}❌ Configuration test failed${NC}"
    exit 1
}

echo ""
echo -e "${GREEN}✅ All tests passed!${NC}"
echo ""

# Success message
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🎉 SETUP COMPLETE!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Next steps:"
echo ""
echo "1️⃣  Run your first analysis:"
echo "   ${BLUE}python denim_analyzer.py --full${NC}"
echo ""
echo "2️⃣  Check the report:"
echo "   ${BLUE}cat outputs/project_sent_denim_v1.md${NC}"
echo ""
echo "3️⃣  For weekly automation:"
echo "   See: SCHEDULER.md"
echo ""
echo -e "${YELLOW}💡 Pro tip: You can edit the configuration anytime by editing the .env file${NC}"
echo ""
