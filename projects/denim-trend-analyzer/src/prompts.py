"""LLM Prompts for Denim Trend Analyzer agents."""

# Phase 2: These prompts will be filled in during implementation
# For now, here are the prompt templates:

DENIM_TREND_COLLECTION_PROMPT = """
You are an expert denim trend analyst. You have access to recent search results about trending denim products.

Search Results:
{search_results}

Your task:
1. Extract the TOP DENIM TRENDS from the search results
2. Identify style categories (vintage-inspired, smart-casual, sustainable, oversized, premium, etc.)
3. Estimate demand signals based on mentions, social engagement proxies, and market signals
4. Group products by style theme

Return a JSON structure with:
{{
    "trends": [
        {{
            "title": "trend name",
            "description": "detailed description",
            "category": "style category",
            "engagement_score": <0-100>,
            "demand_keywords": ["keyword1", "keyword2"],
            "price_range": {{"min": 30, "max": 80}},
            "target_demographic": "age/gender group"
        }}
    ],
    "analysis_timestamp": "ISO timestamp",
    "data_quality": "high/medium/low"
}}

Be specific, data-driven, and focus on commercially viable trends that B2B buyers (Primark, Zara, ASOS) would be interested in.
"""

TREND_SYNTHESIS_PROMPT = """
You are a fashion trend strategist. You have collected {trend_count} denim trend signals.

Collected Trends:
{trends_json}

Your task:
1. IDENTIFY 3-5 CORE TREND THEMES from the individual trends
2. Group related trends together
3. Estimate demand strength for each theme (0-100)
4. Identify target demographics for each theme
5. Estimate retail price positioning

Return JSON with:
{{
    "themes": [
        {{
            "name": "Theme Name",
            "description": "Why this is a trend",
            "trend_count": 3,
            "demand_signal": 75,
            "target_demographic": "Women 25-35",
            "retail_price_range": {{"min": 35, "max": 55}},
            "key_keywords": ["keyword1", "keyword2"]
        }}
    ],
    "insights": "2-3 sentence market insight"
}}

Focus on themes that represent genuine market demand, not fleeting fads. These will become design concepts.
"""

CAD_CONCEPT_PROMPT = """
You are a denim product developer. You have identified the following trend themes:

Trend Themes:
{themes_json}

Your task:
CREATE 5 DESIGN CONCEPTS inspired by the top trend themes.

For EACH concept, provide:
{{
    "concept_number": 1,
    "theme_name": "Which trend inspired this",
    "style_name": "Catchy design name",
    "silhouette": "High-rise, oversized, skinny, etc.",
    "fabric": "Material, weight (oz), construction (sanforized, etc.)",
    "key_features": ["distressed knees", "raw hem", "sustainable cotton"],
    "estimated_retail_price": 45,
    "estimated_production_cost": 18,
    "margin_at_retail": 60,
    "production_lead_time_weeks": 4,
    "production_notes": "Requires skilled distressing, standard construction",
    "trend_signal": "Strong",
    "competitive_gap": "Primark carries basic vintage, but no organic options"
}}

CRITICAL: Each concept must:
- Have realistic cost/margin for B2B retail (2.5-3x markup typical)
- Be producible in 4-6 weeks (standard timeframe)
- Address a specific competitive gap
- Include construction/fabric specifics that matter to manufacturers

Output: JSON array of 5 concepts, each complete with all fields.
"""

DENIM_COMPETITOR_PROMPT = """
You are a denim market analyst. You are analyzing the competitive landscape for new denim products.

Trend Themes to Compete Against:
{themes_json}

Design Concepts We're Considering:
{concepts_json}

Your task:
1. IDENTIFY 5-8 key competitors in the denim space (Primark, Zara, ASOS, Topshop, etc.)
2. Analyze their product positioning, pricing, and feature gaps
3. Assess SWOT for each competitor
4. Identify WHITE SPACE where our concepts can win

For each competitor, return:
{{
    "competitor_name": "Brand Name",
    "market_position": "Premium/Mid-market/Fast-fashion",
    "similar_products": ["vintage jeans", "distressed styles"],
    "price_range": {{"min": 30, "max": 60}},
    "strengths": ["Fast turnover", "Affordable pricing"],
    "weaknesses": ["Limited sustainable options", "Basic design"],
    "market_share_estimate": 8,
    "whitespace_opportunities": ["Eco-friendly vintage", "Larger size ranges"]
}}

ALSO PROVIDE:
{{
    "market_insights": "2-3 sentences on denim market trends",
    "our_positioning": "Where we can win against these competitors",
    "margin_analysis": "Typical margins in denim by price point"
}}

Be realistic about competitive dynamics. These are established retailers with scale advantages.
"""

B2B_REPORT_PROMPT = """
You are a B2B retail intelligence analyst. You have completed a full denim trend analysis.

Analysis Summary:
- Trends: {theme_count} core themes identified
- Concepts: 5 design options generated
- Competitors: {competitor_count} analyzed
- Target Segment: {target_segment}

Your task:
CREATE A RETAIL-FOCUSED REPORT that includes:

1. EXECUTIVE SUMMARY (2-3 sentences)
   - What are the top 3 trends?
   - Why should Primark/Zara/ASOS buyers care?

2. TREND ANALYSIS
   - Each theme with demand signal
   - Why it matters for volume retail

3. FIVE CAD CONCEPTS
   - Style name, specs, estimated margin
   - Production timeline
   - Competitive positioning

4. COMPETITOR LANDSCAPE
   - Who's doing what
   - Where the gaps are
   - Our opportunities

5. B2B BUYER INSIGHTS
   - Margin expectations by price point
   - Buyer sentiment on each trend
   - Risk factors
   - Production timeline recommendations

6. NEXT STEPS
   - Sample production recommendations
   - Key metrics to watch
   - Validation steps

Return as markdown-formatted report suitable for sharing with retail buyers.

TONE: Professional, data-driven, focused on commercial viability and margins.
      Include specific numbers (prices, margins, timelines).
      Highlight competitive gaps and white space.
"""

if __name__ == "__main__":
    print("Denim Trend Analyzer - Agent Prompts")
    print(f"Total prompts defined: 5")
    print("  1. DENIM_TREND_COLLECTION_PROMPT")
    print("  2. TREND_SYNTHESIS_PROMPT")
    print("  3. CAD_CONCEPT_PROMPT")
    print("  4. DENIM_COMPETITOR_PROMPT")
    print("  5. B2B_REPORT_PROMPT")
