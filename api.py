import os
import sys

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))  # noqa: E402

from agents import MeetingPrepAgents  # noqa: E402
from crewai import Crew  # noqa: E402
from tasks import MeetingPrepTask  # noqa: E402
from utils.logging import get_logger, setup_logging  # noqa: E402

load_dotenv()

# Setup logging
logger = setup_logging("smart_marketing_api")
logger.info("Starting Smart Marketing Assistant API")

app = FastAPI(title="Smart Marketing Assistant", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MeetingRequest(BaseModel):
    participants: str
    context: str
    objective: str


@app.post("/api/prepare-meeting")
async def prepare_meeting(request: MeetingRequest):
    try:
        logger.info(
            f"Received meeting preparation request from participants: {request.participants}"
        )

        # Create instances
        tasks = MeetingPrepTask()
        agents = MeetingPrepAgents()

        logger.debug("Initializing agents...")
        # Create agents
        research_agent = agents.research_agent()
        industry_analysis_agent = agents.industry_analysis_agent()
        meeting_strategy_agent = agents.meeting_strategy_agent()
        summary_and_briefing_agent = agents.summary_and_briefing_agent()

        logger.debug("Creating tasks...")
        # Create tasks
        research_task = tasks.research_task(
            research_agent, request.participants, request.context
        )
        industry_analysis_task = tasks.industry_analysis_task(
            industry_analysis_agent, request.participants, request.context
        )
        meeting_strategy_task = tasks.meeting_strategy_task(
            meeting_strategy_agent, request.context, request.objective
        )
        summary_and_briefing_task = tasks.summary_and_briefing_task(
            summary_and_briefing_agent, request.context, request.objective
        )

        # Set context dependencies
        meeting_strategy_task.context = [research_task, industry_analysis_task]
        summary_and_briefing_task.context = [
            research_task,
            industry_analysis_task,
            meeting_strategy_task,
        ]

        # Create crew
        crew = Crew(
            agents=[
                research_agent,
                industry_analysis_agent,
                meeting_strategy_agent,
                summary_and_briefing_agent,
            ],
            tasks=[
                research_task,
                industry_analysis_task,
                meeting_strategy_task,
                summary_and_briefing_task,
            ],
        )

        logger.info("Starting crew execution...")
        # Execute
        result = crew.kickoff()

        logger.info("Crew execution completed successfully")
        return {"success": True, "result": str(result)}

    except Exception as e:
        logger.error(f"Error in meeting preparation: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
def health():
    logger.debug("Health check requested")
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
