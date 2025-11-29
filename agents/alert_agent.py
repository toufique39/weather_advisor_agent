from google.adk.agents import LlmAgent

alert_agent = LlmAgent(
    name="alert_agent",
    instructions="""
You generate short weather safety alerts.
Be direct, simple and helpful.
Only 1–2 sentences. No extra text.
"""
)

