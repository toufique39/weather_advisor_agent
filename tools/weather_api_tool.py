
import requests

def get_weather(city: str):
    """
    Fetch weather using wttr.in public API.
    No auth needed.
    """
    try:
        url = f"https://wttr.in/{city}?format=j1"
        data = requests.get(url, timeout=10).json()

        current = data["current_condition"][0]

        return {
            "city": city,
            "temp_C": current["temp_C"],
            "humidity": current["humidity"],
            "weather": current["weatherDesc"][0]["value"]
        }
    except Exception as e:
        return {"error": str(e)}
