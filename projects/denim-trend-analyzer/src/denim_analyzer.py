#!/usr/bin/env python3
"""Main entry point for Denim Trend Analyzer."""

import asyncio
import argparse
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

from src.config import OUTPUT_DIR, LOG_LEVEL, validate_config
from src.main import run_denim_analysis

# Setup logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def generate_report_filename(version: int = 1) -> str:
    """Generate report filename following project convention."""
    return f"project_sent_denim_v{version}.md"

def find_next_version() -> int:
    """Find the next available version number."""
    version = 1
    while (OUTPUT_DIR / generate_report_filename(version)).exists():
        version += 1
    return version

def save_report(content: str, filename: Optional[str] = None) -> Path:
    """
    Save report to output directory.

    Args:
        content: Report content as markdown
        filename: Custom filename (defaults to project_sent_denim_vX.md)

    Returns:
        Path to saved file
    """
    if filename is None:
        filename = generate_report_filename(find_next_version())

    filepath = OUTPUT_DIR / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, 'w') as f:
        f.write(content)

    logger.info(f"✅ Report saved to {filepath}")
    return filepath

def run_full_analysis(dry_run: bool = False) -> dict:
    """
    Run the complete analysis pipeline.

    Args:
        dry_run: If True, uses cached/minimal data

    Returns:
        Analysis results
    """
    try:
        # Validate configuration
        validate_config()
        logger.info("✅ Configuration validated")

        # Run analysis
        logger.info("🧵 Starting denim trend analysis...")

        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(
            run_denim_analysis("Analyze trending denim products for this week")
        )

        # Parse and save results
        final_output = results.get("final_output", "")

        if final_output:
            # Save report
            report_path = save_report(final_output)

            # Also save raw results as JSON
            results_json = {
                "timestamp": datetime.now().isoformat(),
                "report_file": str(report_path),
                "analysis_summary": {
                    "trends_collected": len(results.get("trend_collection", [])),
                    "themes_identified": len(results.get("theme_synthesis", [])),
                    "cad_concepts": len(results.get("cad_concepts", [])),
                    "competitors_analyzed": len(results.get("competitor_analysis", [])),
                }
            }

            # Save JSON metadata
            json_path = OUTPUT_DIR / f"analysis_metadata_v{find_next_version()-1}.json"
            with open(json_path, 'w') as f:
                json.dump(results_json, f, indent=2, default=str)

            logger.info(f"📊 Analysis metadata: {json_path}")

        logger.info("✅ Analysis complete!")
        return results

    except Exception as e:
        logger.error(f"❌ Analysis failed: {e}", exc_info=True)
        raise

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Denim Trend Analyzer - Weekly denim product analysis"
    )

    parser.add_argument(
        "--full",
        action="store_true",
        help="Run full analysis with fresh data collection"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Test run with minimal data"
    )

    parser.add_argument(
        "--phase",
        choices=["trend_collection", "synthesis", "cad_generation", "competitor_analysis", "report"],
        help="Run specific phase only"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output"
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Logging level"
    )

    args = parser.parse_args()

    # Set logging level
    if args.verbose or args.log_level == "DEBUG":
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        logger.info("🧵 Denim Trend Analyzer")
        logger.info(f"   Output dir: {OUTPUT_DIR}")
        logger.info(f"   Timestamp: {datetime.now()}")

        if args.full or not args.dry_run:
            logger.info("Running FULL analysis...")
            results = run_full_analysis(dry_run=False)
        elif args.dry_run:
            logger.info("Running DRY-RUN (minimal data)...")
            results = run_full_analysis(dry_run=True)

        # Print summary
        print("\n" + "="*60)
        print("✅ ANALYSIS COMPLETE")
        print("="*60)

        if results:
            if "report_file" in results:
                print(f"📄 Report: {results['report_file']}")
            print(f"📊 Trends collected: {len(results.get('trend_collection', []))}")
            print(f"🎨 CAD concepts: {len(results.get('cad_concepts', []))}")
            print(f"🏆 Competitors analyzed: {len(results.get('competitor_analysis', []))}")

        print("="*60 + "\n")

        return 0

    except KeyboardInterrupt:
        logger.warning("⚠️  Analysis interrupted by user")
        return 1
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
