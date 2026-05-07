#!/usr/bin/env python3
"""
Denim Trend Analyzer - Interactive Setup Wizard
For non-technical users: just run this and answer the questions!
"""

import os
import sys
import subprocess
from pathlib import Path

class Colors:
    """ANSI color codes for terminal output."""
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    """Print a fancy header."""
    print(f"\n{Colors.BLUE}{'='*50}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BLUE}{'='*50}{Colors.END}\n")

def print_success(text):
    """Print success message."""
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text):
    """Print error message."""
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_info(text):
    """Print info message."""
    print(f"{Colors.YELLOW}ℹ️  {text}{Colors.END}")

def check_python():
    """Check if Python is installed."""
    print_header("🧵 Denim Trend Analyzer - Setup")

    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print_error(f"Python 3.10+ required (you have {version.major}.{version.minor})")
        print_info("Download from: https://www.python.org/downloads/")
        return False

    print_success(f"Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def get_api_keys():
    """Get API keys from user interactively."""
    print_header("🔑 API Keys Setup")
    print("You need 2 free API keys:\n")

    print(f"{Colors.BOLD}1. Nebius API Key{Colors.END}")
    print("   Get it from: https://console.anthropic.com")
    print("   (It looks like: nebius_xxxxxxxxxxxxx)\n")

    nebius_key = input("Paste your Nebius API Key: ").strip()
    if not nebius_key:
        print_error("Nebius API key is required")
        return None, None

    print(f"\n{Colors.BOLD}2. Tavily API Key{Colors.END}")
    print("   Get it from: https://tavily.com")
    print("   (It looks like: tvly_xxxxxxxxxxxxx)\n")

    tavily_key = input("Paste your Tavily API Key: ").strip()
    if not tavily_key:
        print_error("Tavily API key is required")
        return None, None

    print_success("API keys saved")
    return nebius_key, tavily_key

def create_env_file(nebius_key, tavily_key):
    """Create .env configuration file."""
    env_content = f"""NEBIUS_API_KEY={nebius_key}
TAVILY_API_KEY={tavily_key}

OUTPUT_DIR=./outputs
LOG_LEVEL=INFO
"""

    with open('.env', 'w') as f:
        f.write(env_content)

    # Protect the file
    os.chmod('.env', 0o600)
    print_success("Configuration file created (.env)")

def install_dependencies():
    """Install Python dependencies."""
    print_header("📦 Installing Dependencies")
    print("This may take a few minutes...\n")

    try:
        # Check if uv is available
        subprocess.run(['uv', '--version'], capture_output=True, check=True)
        print_info("Using uv package manager")
        subprocess.run(['uv', 'sync'], check=True)
    except FileNotFoundError:
        print_info("Installing with pip (uv not found)")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)

        requirements = [
            'google-adk>=0.1.0',
            'langchain-tavily>=0.1.0',
            'python-dotenv>=1.0.0',
            'pydantic>=2.0.0',
            'requests>=2.31.0',
            'markdown2>=2.4.11',
        ]

        for req in requirements:
            subprocess.run([sys.executable, '-m', 'pip', 'install', req], check=True)

    print_success("Dependencies installed")

def test_installation():
    """Test that everything works."""
    print_header("🧪 Testing Installation")

    try:
        print("Testing configuration...")
        from src.config import validate_config
        validate_config()
        print_success("Configuration valid")

        print("Testing imports...")
        import src.main
        import src.data_models
        print_success("All imports successful")

        return True
    except Exception as e:
        print_error(f"Test failed: {e}")
        return False

def main():
    """Main setup wizard."""
    # Check Python version
    if not check_python():
        return 1

    # Check if .env already exists
    if Path('.env').exists():
        response = input("\n.env file already exists. Overwrite? (y/n): ").strip().lower()
        if response != 'y':
            print_info("Skipping .env creation")
            # Still test though
            if test_installation():
                print_success_summary()
                return 0
            else:
                return 1

    # Get API keys
    nebius_key, tavily_key = get_api_keys()
    if not nebius_key or not tavily_key:
        return 1

    # Create .env file
    create_env_file(nebius_key, tavily_key)

    # Install dependencies
    try:
        install_dependencies()
    except subprocess.CalledProcessError as e:
        print_error(f"Installation failed: {e}")
        print_info("Try running: pip install -r requirements.txt")
        return 1

    # Test installation
    if not test_installation():
        return 1

    # Success!
    print_success_summary()
    return 0

def print_success_summary():
    """Print final success message."""
    print_header("🎉 Setup Complete!")
    print(f"{Colors.BOLD}You're ready to analyze denim trends!{Colors.END}\n")

    print("Next steps:\n")
    print(f"1️⃣  Run your first analysis:")
    print(f"   {Colors.BLUE}python denim_analyzer.py --full{Colors.END}\n")

    print(f"2️⃣  Check the report:")
    print(f"   {Colors.BLUE}cat outputs/project_sent_denim_v1.md{Colors.END}\n")

    print(f"3️⃣  For weekly automation:")
    print(f"   See: {Colors.BLUE}SCHEDULER.md{Colors.END}\n")

    print(f"{Colors.YELLOW}💡 Tip: Edit .env anytime to change API keys{Colors.END}\n")

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print_error("\nSetup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)
