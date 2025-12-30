import requests 
url = "http://universities.hipolabs.com/search"
country = input("Enter a country to search: ")
parametr = {
    "country": country
}
response = requests.get(url, parametr)
if response.status_code==200:
    response = response.json()
    if len(response)==0:
        print(f"No universities found for {country}.")
    else:
        print(f"Found {len(response)} universities in {country}.")
        print("Here are the first 5:")
        result = response[0:5]
        print("1. " + result[0]['name'])
        print("2. " + result[1]['name'])
        print("3. " + result[2]['name'])
        print("4. " + result[3]['name'])
        print("5. " + result[4]['name'])
    
    
    
