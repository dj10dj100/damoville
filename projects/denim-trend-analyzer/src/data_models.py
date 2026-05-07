"""Data models for Denim Trend Analyzer."""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class TrendPin(BaseModel):
    """Represents a trending denim pin from Pinterest or web."""
    title: str = Field(..., description="Pin/item title")
    description: str = Field(..., description="Detailed description")
    engagement_score: float = Field(..., ge=0, description="Engagement metric (0-100)")
    source: str = Field(..., description="Source (pinterest, web, instagram)")
    category: str = Field(..., description="Denim category (skinny, wide, vintage, smart, etc.)")
    image_url: Optional[str] = Field(None, description="Image URL if available")
    trend_keywords: List[str] = Field(default_factory=list, description="Associated keywords")
    collected_at: datetime = Field(default_factory=datetime.now)

class TrendTheme(BaseModel):
    """Represents a synthesized trend theme."""
    name: str = Field(..., description="Theme name (e.g., 'Vintage-Inspired Wide-Leg')")
    description: str = Field(..., description="Theme description")
    pins: List[TrendPin] = Field(default_factory=list, description="Associated pins")
    demand_signal: float = Field(..., ge=0, le=100, description="Estimated demand percentage")
    target_demographic: str = Field(..., description="Target customer (e.g., 'Women 25-35')")
    retail_price_range: tuple = Field(..., description="Min/max retail price tuple")

class CADConcept(BaseModel):
    """Represents a design concept brief."""
    concept_number: int = Field(..., ge=1, le=5, description="Concept 1-5")
    theme_name: str = Field(..., description="Based on which trend theme")
    style_name: str = Field(..., description="Design name (e.g., 'Vintage Wide Leg')")
    silhouette: str = Field(..., description="Cut and fit description")
    fabric_details: str = Field(..., description="Material, weight, construction")
    key_features: List[str] = Field(..., description="Distressing, raw hem, etc.")
    estimated_retail_price: float = Field(..., gt=0, description="Suggested retail price")
    estimated_cost: float = Field(..., gt=0, description="Estimated production cost")
    margin_percentage: float = Field(..., ge=0, le=100, description="Profit margin %")
    production_lead_time_weeks: int = Field(..., ge=1, description="Weeks to produce")
    production_notes: str = Field(..., description="Manufacturing considerations")
    trend_signal_strength: str = Field(..., description="Strong/Medium/Emerging")

class CompetitorData(BaseModel):
    """Represents competitor analysis."""
    competitor_name: str = Field(..., description="Company name")
    market_position: str = Field(..., description="Premium/Mid-market/Fast-fashion")
    similar_products: List[str] = Field(default_factory=list, description="Similar styles they offer")
    price_range: tuple = Field(..., description="Min/max price tuple")
    strengths: List[str] = Field(default_factory=list, description="Competitive advantages")
    weaknesses: List[str] = Field(default_factory=list, description="Market gaps")
    market_share_estimate: Optional[float] = Field(None, ge=0, le=100, description="Estimated %")

class DenimMarketAnalysis(BaseModel):
    """Represents market analysis findings."""
    total_addressable_market: str = Field(..., description="TAM description")
    serviceable_available_market: str = Field(..., description="SAM description")
    serviceable_obtainable_market: str = Field(..., description="SOM description")
    target_segments: List[str] = Field(..., description="Customer segments")
    margin_expectations_by_segment: Dict[str, float] = Field(..., description="Segment -> margin %")
    key_trends: List[str] = Field(..., description="Industry trends")
    growth_opportunities: List[str] = Field(..., description="Market opportunities")

class DenimReport(BaseModel):
    """Complete denim trend analysis report."""
    report_week: str = Field(..., description="Week of YYYY-MM-DD")
    executive_summary: str = Field(..., description="1-2 paragraph summary")

    trend_themes: List[TrendTheme] = Field(default_factory=list, description="Top 3-5 themes")
    cad_concepts: List[CADConcept] = Field(default_factory=list, description="5 design concepts")

    competitors: List[CompetitorData] = Field(default_factory=list, description="Competitor analysis")
    market_analysis: Optional[DenimMarketAnalysis] = Field(None, description="Market insights")

    b2b_insights: str = Field(..., description="Retail buyer perspective")
    recommendations: List[str] = Field(default_factory=list, description="Next steps")

    raw_trend_data: List[TrendPin] = Field(default_factory=list, description="All collected pins")

    generated_at: datetime = Field(default_factory=datetime.now)
    version: int = Field(default=1, description="Report version number")

# Type hints for agent outputs
TrendCollectionResult = Dict[str, List[TrendPin]]
ThemeSynthesisResult = List[TrendTheme]
CADGenerationResult = List[CADConcept]
CompetitorAnalysisResult = List[CompetitorData]
ReportGenerationResult = DenimReport
