from agents.weather_agent import process_weather

def run_agent():
    city = input("Enter a city name: ")

    result = process_weather(city)

    print("\n========== WEATHER REPORT ==========")
    print(result["summary"])
    print("\n============== ALERT ===============")
    print(result["alert"])
    print("====================================\n")


if __name__ == "__main__":
    run_agent()

