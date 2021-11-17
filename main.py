import requests
from datetime import datetime
import config

APP_ID = config.APP_ID
APP_KEY = config.APP_KEY

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/workoutTracking/workouts"

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}
nutrition_body = {
    "query": "i ran 5 miles"
}

response = requests.post(url=nutrition_endpoint, headers=nutrition_headers, json=nutrition_body)
data = response.json()["exercises"][0]
duration = data["duration_min"]
exercise = data["name"].title()
calories = data["nf_calories"]

date = datetime.now().strftime("%m/%d/%Y")
time = datetime.now().strftime("%H:%M:%S")

sheety_headers = {
    "Content-Type": "application/json"
}
sheety_body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

res = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_headers)
print(res.text)
