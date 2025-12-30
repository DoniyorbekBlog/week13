import requests
print("Connecting to ISS satellite...")
url = "http://api.open-notify.org/iss-now.json"
response = requests.get("http://api.open-notify.org/iss-now.json")
message = ''
latitude = 0
longitude = 0
if response.status_code==200:
    response = response.json()
    message = response["message"]
    latitude = response["iss_position"]["latitude"]
    longitude = response["iss_position"]["longitude"]
print(f"Connection {message}!")
print("Current Location:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")