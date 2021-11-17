import requests
import config

APP_ID = config.APP_ID
APP_KEY = config.APP_KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}
body = {
    "query": input("What exercises did you do? ")
}

response = requests.post(url=exercise_endpoint, headers=headers, json=body)
print(response.json())
