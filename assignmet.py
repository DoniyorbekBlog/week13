import requests
country = input("Enter city/country: ")
url = "https://api.openweathermap.org/data/2.5/weather"
api = "72a95da9e15a516a15624a1f439306f5"
parametr = {
    "q": country,
    "appid": api
}
response = requests.get(url, parametr)
if response.status_code==200:
    response=response.json()
    print("All information about "+response["name"])
    print(f"Lantitude: {response["coord"]["lat"]}")
    print(f"Longtitude: {response["coord"]["lon"]}")
    print("Weather:")
    print(f"    Main: {response['weather'][0]['main']}")
    print(f"    Description: {response['weather'][0]['description']}")
    print("Wind: ")
    print(f"    Degree: {response['wind'] ['deg']}")
    print(f"    Speed: {response['wind']['speed']}")
else:
    print("No information about " + country)