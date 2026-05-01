import os
from crewai import Agent
from crewai.llm import LLM
from textwrap import dedent
from tools import ExaSearchToolSet


class MeetingPrepAgents:

    def _get_llm(self):
        return LLM(
            model=os.environ.get("OPENROUTER_MODEL", "openrouter/openai/gpt-3.5-turbo"),
            api_key=os.environ.get("OPENROUTER_API_KEY"),
        )

    def research_agent(self):
        return Agent(
            role="Research Specialist",
            goal="Conduct thorough research on all relevant topics, stakeholders, and resources for the planning objective.",
            tools=ExaSearchToolSet.tools(),
            llm=self._get_llm(),
            backstory=dedent("""\
                As a Research Specialist, your mission is to uncover detailed information
                about the people, organizations, and resources involved in the planning process.
                Your insights will lay the groundwork for effective and informed planning."""),
            verbose=True,
        )

    def industry_analysis_agent(self):
        return Agent(
            role="Context Analyst",
            goal="Analyze the current context, trends, challenges, and opportunities related to the planning objective.",
            tools=ExaSearchToolSet.tools(),
            llm=self._get_llm(),
            backstory=dedent("""\
                As a Context Analyst, your analysis will identify key trends,
                challenges, and opportunities that could impact the planning process.
                Your findings will help shape a robust and adaptive plan."""),
            verbose=True,
        )

    def meeting_strategy_agent(self):
        return Agent(
            role="Planning Strategy Advisor",
            goal="Develop strategies, action steps, and recommendations to achieve the planning objective.",
            llm=self._get_llm(),
            backstory=dedent("""\
                As a Planning Strategy Advisor, your expertise will guide the development of
                strategies, action steps, and recommendations to ensure the planning goals are met efficiently and effectively."""),
            verbose=True,
        )

    def summary_and_briefing_agent(self):
        return Agent(
            role="Briefing Coordinator",
            goal="Compile all gathered information into a concise, informative planning briefing document.",
            llm=self._get_llm(),
            backstory=dedent("""\
                As the Briefing Coordinator, your role is to consolidate the research,
                analysis, and strategic insights into a clear and actionable planning summary."""),
            verbose=True,
        )
