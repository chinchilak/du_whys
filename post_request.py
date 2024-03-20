import httpx
import json

URL = "http://127.0.0.1:8000/import/"
FILE = "test_data.json"

with open(FILE, "r") as file:
    data = json.load(file)

response = httpx.post(URL, json=data)
print("Response:", response, response.content)
