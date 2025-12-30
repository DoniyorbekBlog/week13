import requests
import csv
from pprint import pprint
dic = {}
url = "https://open.er-api.com/v6/latest/USD"
response = requests.get(url).json()
look_up = response['rates']
with open("expenses.csv", "r") as file:
    smth = csv.reader(file)
    print(smth)