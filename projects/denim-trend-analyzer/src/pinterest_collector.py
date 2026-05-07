"""Pinterest and web data collection for denim trends."""

import os
from typing import List, Dict, Any
from langchain_tavily import TavilySearch
from src.data_models import TrendPin
from src.config import TAVILY_API_KEY
from datetime import datetime

class PinterestCollector:
    """Collects denim trend data from Pinterest API or web sources."""

    def __init__(self):
        """Initialize the collector."""
        self.tavily = TavilySearch(
            max_results=10,
            search_depth="basic",
            include_answer=True,
            include_raw_content=False,
            include_images=False,
        )

    def collect_denim_trends(self) -> List[TrendPin]:
        """
        Collect trending denim products.

        Phase 1 (current): Uses Tavily web search as fallback
        Phase 4: Will switch to Pinterest API

        Returns:
            List of TrendPin objects
        """
        trends = []

        # Search for trending denim products
        search_queries = [
            "most popular denim trends 2026",
            "trending vintage denim styles",
            "sustainable denim products",
            "oversized jeans fashion trend",
            "smart casual denim styling",
        ]

        for query in search_queries:
            try:
                results = self.tavily.run(query)
                pins = self._parse_tavily_results(results, query)
                trends.extend(pins)
            except Exception as e:
                print(f"⚠️  Error searching '{query}': {e}")
                continue

        # Remove duplicates based on title
        seen_titles = set()
        unique_trends = []
        for trend in trends:
            if trend.title not in seen_titles:
                seen_titles.add(trend.title)
                unique_trends.append(trend)

        return unique_trends[:20]  # Return top 20 trends

    def _parse_tavily_results(self, results: str, query: str) -> List[TrendPin]:
        """
        Parse Tavily search results into TrendPin objects.

        Args:
            results: Raw search results from Tavily
            query: Original search query

        Returns:
            List of parsed TrendPin objects
        """
        pins = []

        # Simple heuristic parsing (Phase 1)
        # In production, could use more sophisticated parsing

        lines = results.split('\n')
        for line in lines:
            if line.strip() and len(line) > 20:
                # Create a trend pin from the line
                pin = TrendPin(
                    title=line[:80],
                    description=line,
                    engagement_score=self._estimate_engagement(line),
                    source="web",
                    category=self._infer_category(line),
                    trend_keywords=self._extract_keywords(line, query),
                    collected_at=datetime.now()
                )
                pins.append(pin)

        return pins

    def _estimate_engagement(self, text: str) -> float:
        """Estimate engagement score from text mentions."""
        score = 50.0  # Base score

        # Boost for high-engagement keywords
        boosters = {
            "trending": 15,
            "popular": 12,
            "viral": 20,
            "best-selling": 15,
            "must-have": 10,
            "sustainable": 8,
        }

        for keyword, boost in boosters.items():
            if keyword.lower() in text.lower():
                score += boost

        return min(score, 100)  # Cap at 100

    def _infer_category(self, text: str) -> str:
        """Infer denim style category from text."""
        text_lower = text.lower()

        categories = {
            "vintage": ["vintage", "retro", "90s", "80s"],
            "oversized": ["oversized", "baggy", "boyfriend", "wide"],
            "skinny": ["skinny", "slim", "tight", "fitted"],
            "smart-casual": ["smart", "business", "professional"],
            "sustainable": ["sustainable", "eco", "organic", "recycled"],
            "distressed": ["ripped", "distressed", "shredded", "torn"],
            "raw-denim": ["raw", "unwashed", "selvedge", "indigo"],
        }

        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return category

        return "classic"

    def _extract_keywords(self, text: str, query: str) -> List[str]:
        """Extract relevant keywords from text."""
        keywords = []

        # Include original query words
        keywords.extend(query.split()[:3])

        # Add common denim-related keywords if found
        denim_keywords = [
            "denim", "jeans", "jeans trend", "vintage", "sustainable",
            "oversized", "distressed", "high-rise", "mid-rise"
        ]

        for keyword in denim_keywords:
            if keyword.lower() in text.lower():
                keywords.append(keyword)

        return list(set(keywords))[:5]  # Return top 5 unique keywords

    def collect_from_pinterest_api(self) -> List[TrendPin]:
        """
        Collect from Pinterest API (Phase 4).

        This is a placeholder for Phase 4 implementation when
        Pinterest API credentials are obtained.

        Returns:
            Empty list (Phase 1 fallback)
        """
        # TODO: Implement Pinterest API integration
        # Requires: PINTEREST_ACCESS_TOKEN
        # Steps:
        #   1. Authenticate with Pinterest API
        #   2. Search for pins: "denim", "jeans", "denim trends"
        #   3. Extract engagement metrics (repins, saves)
        #   4. Filter by date (last 7 days)
        #   5. Parse description and tags
        return []

def collect_denim_trends() -> List[TrendPin]:
    """
    Convenience function to collect denim trends.

    Returns:
        List of TrendPin objects
    """
    collector = PinterestCollector()
    return collector.collect_denim_trends()

if __name__ == "__main__":
    print("Testing PinterestCollector...")
    collector = PinterestCollector()
    trends = collector.collect_denim_trends()
    print(f"✅ Collected {len(trends)} trends")
    for trend in trends[:3]:
        print(f"  - {trend.title} (engagement: {trend.engagement_score})")
