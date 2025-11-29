from google.adk.agents import LlmAgent
from tools.weather_api_tool import get_weather
from agents.alert_agent import alert_agent

weather_agent = LlmAgent(
    name="weather_agent",
    instructions="""
You summarize weather data in simple English.
Return short, friendly and clear responses.
"""
)

def process_weather(city: str):
    weather = get_weather(city)

    if "error" in weather:
        return {
            "summary": f"Could not fetch weather for {city}: {weather['error']}",
            "alert": "No alert available."
        }

    # Weather summary
    summary = weather_agent.run(
        inputs={
            "message": f"Summarize this weather: {weather}"
        }
    ).text

    # Safety alert
    alert = alert_agent.run(
        inputs={
            "message": f"Generate alert for this weather: {weather}"
        }
    ).text

    return {
        "summary": summary,
        "alert": alert
    }

