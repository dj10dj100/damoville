"""Configuration management for Denim Trend Analyzer."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project root
PROJECT_ROOT = Path(__file__).parent.parent

# API Keys
NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
PINTEREST_API_KEY = os.getenv("PINTEREST_API_KEY")
PINTEREST_API_SECRET = os.getenv("PINTEREST_API_SECRET")
PINTEREST_ACCESS_TOKEN = os.getenv("PINTEREST_ACCESS_TOKEN")

# Model Configuration
NEBIUS_MODEL = "nebius/Qwen/Qwen3-235B-A22B-Instruct-2507"

# Tavily Configuration
TAVILY_MAX_RESULTS = 3
TAVILY_SEARCH_DEPTH = "basic"
TAVILY_INCLUDE_ANSWER = True

# Output Configuration
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "./outputs"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Validation
def validate_config():
    """Validate that all required configuration is present."""
    errors = []

    if not NEBIUS_API_KEY:
        errors.append("NEBIUS_API_KEY is not set in .env")
    if not TAVILY_API_KEY:
        errors.append("TAVILY_API_KEY is not set in .env")

    if errors:
        raise ValueError("Configuration errors:\n" + "\n".join(f"  - {e}" for e in errors))

    return True

# API Configuration Objects
class APIConfig:
    """Container for API configuration."""
    nebius_key = NEBIUS_API_KEY
    tavily_key = TAVILY_API_KEY
    pinterest_key = PINTEREST_API_KEY
    pinterest_secret = PINTEREST_API_SECRET
    pinterest_token = PINTEREST_ACCESS_TOKEN

if __name__ == "__main__":
    # Test configuration
    try:
        validate_config()
        print("✅ Configuration is valid")
        print(f"   Output directory: {OUTPUT_DIR}")
        print(f"   Log level: {LOG_LEVEL}")
        print(f"   Model: {NEBIUS_MODEL}")
    except ValueError as e:
        print(f"❌ Configuration error:\n{e}")
        exit(1)
