"""Agent definitions for Denim Trend Analyzer."""

import os
import asyncio
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from langchain_tavily import TavilySearch
from google.adk.tools.langchain_tool import LangchainTool

import src.prompts as prompts
from src.config import NEBIUS_API_KEY, NEBIUS_MODEL, TAVILY_API_KEY

# Initialize LLM
NEBIUS_LLM = LiteLlm(
    model=NEBIUS_MODEL,
    api_key=NEBIUS_API_KEY
)

# Initialize search tool
tavily_tool_instance = TavilySearch(
    max_results=5,
    search_depth="basic",
    include_answer=True,
    include_raw_content=False,
    include_images=False,
)

tavily_search = LangchainTool(tool=tavily_tool_instance)

# ============================================================================
# Phase 2: Agents (to be implemented)
# ============================================================================

# PLACEHOLDER AGENTS
# These will be fully implemented in Phase 2

denim_trend_collector_agent = LlmAgent(
    name="DenimTrendCollectorAgent",
    model=NEBIUS_LLM,
    instruction=prompts.DENIM_TREND_COLLECTION_PROMPT,
    description="Collects trending denim items from web and Pinterest sources",
    tools=[tavily_search],
    output_key="trend_collection"
)

trend_synthesizer_agent = LlmAgent(
    name="TrendSynthesizerAgent",
    model=NEBIUS_LLM,
    instruction=prompts.TREND_SYNTHESIS_PROMPT,
    description="Synthesizes individual trends into 3-5 core themes",
    output_key="theme_synthesis"
)

cad_concept_generator_agent = LlmAgent(
    name="CADConceptGeneratorAgent",
    model=NEBIUS_LLM,
    instruction=prompts.CAD_CONCEPT_PROMPT,
    description="Generates 5 CAD visualization briefs from trend themes",
    output_key="cad_concepts"
)

denim_competitor_analyzer_agent = LlmAgent(
    name="DenimCompetitorAnalyzerAgent",
    model=NEBIUS_LLM,
    instruction=prompts.DENIM_COMPETITOR_PROMPT,
    description="Analyzes competitive landscape and identifies opportunities",
    tools=[tavily_search],
    output_key="competitor_analysis"
)

b2b_report_generator_agent = LlmAgent(
    name="B2BReportGeneratorAgent",
    model=NEBIUS_LLM,
    instruction=prompts.B2B_REPORT_PROMPT,
    description="Synthesizes all findings into a B2B-focused retail report",
    output_key="validation_report"
)

# ============================================================================
# Sequential Agent Pipeline
# ============================================================================

denim_analysis_pipeline = SequentialAgent(
    name="DenimAnalysisPipeline",
    sub_agents=[
        denim_trend_collector_agent,
        trend_synthesizer_agent,
        cad_concept_generator_agent,
        denim_competitor_analyzer_agent,
        b2b_report_generator_agent
    ],
    description="Complete pipeline for weekly denim trend analysis and CAD concept generation"
)

# ============================================================================
# Pipeline Execution
# ============================================================================

APP_NAME = "denim_trend_analyzer"
USER_ID = "damo_ventures"
SESSION_ID = "weekly_analysis_session"

async def run_denim_analysis(analysis_input: str = "Analyze trending denim products for this week"):
    """
    Run the complete denim analysis pipeline.

    Args:
        analysis_input: Initial prompt for the pipeline

    Returns:
        Complete analysis results from all agents
    """
    print(f"🧵 Starting denim trend analysis pipeline...")

    # Initialize session
    initial_state = {"analysis_request": analysis_input}
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
    )

    # Run pipeline
    runner = Runner(
        agent=denim_analysis_pipeline,
        app_name=APP_NAME,
        session_service=session_service
    )

    content = types.Content(role="user", parts=[types.Part(text=analysis_input)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    # Collect results
    final_output = None
    for event in events:
        if event.is_final_response():
            final_output = event.content.parts[0].text
            print(final_output)

    # Get session state with all agent outputs
    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    return {
        "final_output": final_output,
        "session_state": session.state,
        "trend_collection": session.state.get("trend_collection"),
        "theme_synthesis": session.state.get("theme_synthesis"),
        "cad_concepts": session.state.get("cad_concepts"),
        "competitor_analysis": session.state.get("competitor_analysis"),
        "report": session.state.get("validation_report"),
    }

if __name__ == "__main__":
    print("✅ Agents initialized successfully")
    print("\nAgent Pipeline:")
    print("  1. DenimTrendCollectorAgent")
    print("  2. TrendSynthesizerAgent")
    print("  3. CADConceptGeneratorAgent")
    print("  4. DenimCompetitorAnalyzerAgent")
    print("  5. B2BReportGeneratorAgent")
    print("\nTo run analysis: python denim_analyzer.py")
