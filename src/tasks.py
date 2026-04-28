from textwrap import dedent
from crewai import Task


class MeetingPrepTask():
    
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description = dedent(f"""\
                Conduct in-depth marketing research for the upcoming campaign. Gather
                audience insights, competitor positioning, product strengths, and market
                dynamics that will help shape a compelling campaign strategy.
                
                Campaign Stakeholders: {meeting_participants}
                Marketing Context: {meeting_context}"""),
            expected_output = dedent(f"""\
                A structured marketing research report using markdown headings. Include:
                - Audience insights
                - Competitor analysis
                - Market opportunity summary
                - Key brand/product advantages
                - Strategic implications for campaign planning"""),
            agent = agent,
            async_execution=True
        )

    def industry_analysis_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description = dedent(f"""\
                Analyze the current marketing landscape relative to the campaign.
                Identify emerging trends, channel opportunities, competitive threats, and
                high-value growth spaces.
                
                Campaign Stakeholders: {meeting_participants}
                Marketing Context: {meeting_context}"""),
            expected_output = dedent(f"""\
                An analytical marketing report using markdown headings. Include:
                - Trend overview
                - Opportunity and risk analysis
                - Recommended channels and tactics
                - Priority focus areas for the campaign"""),
            agent = agent,
            async_execution=True
        )

    def meeting_strategy_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description = dedent(f"""\
                Create a complete marketing strategy based on the research and analysis.
                Build a practical campaign plan that outlines objectives, target audience,
                messaging, channels, and success metrics.
                
                Marketing Context: {meeting_context}
                Campaign Objective: {meeting_objective}"""),
            expected_output = dedent(f"""\
                A polished marketing strategy plan using markdown headings. Include:
                - Campaign overview
                - Objectives and KPIs
                - Target audience and positioning
                - Messaging framework
                - Channel strategy and activation ideas
                - Measurement and next steps"""),
            agent = agent
        )

    def summary_and_briefing_task(self, agent, meeting_context, meeting_objective):
        return Task(
            description = dedent(f"""\
                Compile the research, analysis, and strategy into a high-impact marketing brief.
                Make it easy for stakeholders to understand the campaign direction, rationale,
                and action plan.
                
                Marketing Context: {meeting_context}
                Campaign Objective: {meeting_objective}"""),
            expected_output = dedent(f"""\
                A compelling marketing briefing document using markdown headings. Include:
                - Executive summary
                - Campaign goal summary
                - Audience and opportunity insights
                - Core strategy and creative direction
                - Tactical plan and timeline
                - Success metrics and next steps"""),
            agent = agent
        )



