import requests
from datetime import datetime
import config

APP_ID = config.APP_ID
APP_KEY = config.APP_KEY
TOKEN = config.TOKEN

date = datetime.now().strftime("%m/%d/%Y")
time = datetime.now().strftime("%H:%M:%S")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/workoutTracking/workouts"

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}
nutrition_body = {
    "query": "i jogged 5 mins and did yoga for 10 mins"
}

response = requests.post(url=nutrition_endpoint, headers=nutrition_headers, json=nutrition_body)
data = response.json()["exercises"]

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {TOKEN}'
}

for exercise in data:
    sheety_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    res = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_headers)

