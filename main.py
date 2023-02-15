import requests
from datetime import *
from requests.auth import HTTPBasicAuth
import os

APP_ID = os.environ["APP_ID"]
APP_KEY =  os.environ["APP_KEY"]
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
WORKOUT_API = "https://api.sheety.co/73cf0def7618587a0018adff7fde48af/workoutTracking/workouts"
USERNAME =  os.environ["USERNAME"]
PASSWORD =  os.environ["PASSWORD"]
BASIC = HTTPBasicAuth(USERNAME, PASSWORD)

bearer_headers = {
"Authorization": "Bearer 0630"
}

headers = {
  "x-app-id": APP_ID,
  "x-app-key": APP_KEY,
}

exercise_text = input("Tell me which exercise you did: ")

user_params = {
  "query": exercise_text,
  "gender": 'male',
  "weight_kg": 65,
  'height_cm': 170,
  'age': 21,
}

#basic
#response = requests.post(url=URL, json=user_params, headers=headers, auth=BASIC)

#bearer
response = requests.post(url=URL, json=user_params, headers=headers)
response.raise_for_status()
data = response.json()

# record_data = {
#   "workout": {
#   "date": datetime.today().strftime("%m/%d/%Y"),
#   "time": datetime.now().strftime("%I:%M%p"),
#   "exercise": data['exercises'][0]['name'].title,
#   "duration": data['exercises'][0]['duration_min'],
#   "calories": data['exercises'][0]['nf_calories']
# }}
#
# response2 = requests.post(url=WORKOUT_API, json=record_data)
# response2.raise_for_status()
# print(response2.text)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    #Basic Auth
    #sheet_response = requests.post(WORKOUT_API, json=sheet_inputs, auth=BASIC)
    
    #Bearer
    sheet_response = requests.post(WORKOUT_API, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
