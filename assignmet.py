import requests
weather_api = "72a95da9e15a516a15624a1f439306f5"
flag_api = "YKQVsxgJYprMRikXEdifuA==NNEvm3Xz8mFGzGkQ"

weather_url = "https://api.openweathermap.org/data/2.5/weather"
flag_url = "https://api.api-ninjas.com/v1/countryflag"

def get_weather_data(city):
    params = {
        "q": city,
        "appid": weather_api,
        "units": "metric"
    }
    try:
        response = requests.get(weather_url, params=params)
        return response.json()
    except Exception as e:
        return f"❌ Error: {e}"

def get_country_flag(country_name):
    headers = {
        "X-Api-Key": flag_api
    }
    params = {
        "country": country_name
    }

    try:
        response = requests.get(flag_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['rectangle_image_url']

        else:
            return "Flag not available"

    except Exception as e:
        return "Flag not available" + e

def process_weather_data(data):
    temperature = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    city_name = data["name"]
    country_code = data["sys"]["country"]

    if temperature < 5:
        temp_category = "Cold ☃️ "
    elif temperature < 25:
        temp_category = "Mild ⛅️ "
    else:
        temp_category = "Hot ☀️ "

    if wind_speed > 10:
        wind_status = "Strong wind ⚡️ "
    else:
        wind_status = "Normal wind 💨"

    flag_url = get_country_flag(country_code)
    dic = {
        "city": city_name,
        "country": country_code,
        "temperature": temperature,
        "temp_category": temp_category,
        "wind_speed": wind_speed,
        "wind_status": wind_status,
        "flag_url": flag_url
    }
    return dic


def display_weather(result):
    print("\n===== WEATHER REPORT =====")
    print(f"City: {result['city']} ({result['country']})")
    print(f"Temperature: {result['temperature']} °C ({result['temp_category']})")
    print(f"Wind Speed: {result['wind_speed']} m/s ({result['wind_status']})")
    print(f"Country Flag URL: {result['flag_url']}")


def save_to_file(result):
    with open("weather_report.txt", "a") as file:
        file.write("\n==================\n")
        file.write("  WEATHER REPORT  \n")
        file.write("==================\n")
        file.write(f"City: {result['city']} ({result['country']})\n")
        file.write(f"Temperature: {result['temperature']} °C ({result['temp_category']})\n")
        file.write(f"Wind Speed: {result['wind_speed']} m/s ({result['wind_status']})\n")
        file.write(f"Flag URL: {result['flag_url']}\n")


def main():
    city = input("Enter a city name: ")
    if city == "":
        return "❌ Invalid city name."

    weather_data = get_weather_data(city)

    if weather_data==None or weather_data.get("cod") != 200:
        return "❌ No weather information found."

    processed_data = process_weather_data(weather_data)
    display_weather(processed_data)
    save_to_file(processed_data)
    print("\n✅ Weather report saved to weather_report.txt")

main()