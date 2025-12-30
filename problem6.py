# i have solved on the board
import requests
url = "https://randomuser.me/api/?results=10&nat=us"
response = requests.get(url)
response = response.json()
for n in response[0]:
    print(n)
    # for names in user
    #     print(names)


# print(response["results"][0:]["name"]["first"])
# print(response["results"][0::]["name"]["last"])

# with open("fake_users.csv", "w") as file:
