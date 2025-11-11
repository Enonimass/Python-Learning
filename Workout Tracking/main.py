from dotenv import load_dotenv
import os
import requests
from datetime import *

#Personal data. USed by Nutritionnix to calculate calories
GENDER = 'Male'
WEIGHT_KG = 63
HEIGHT_CM = 170
AGE = 22


API_ID= 'd524b06e'
API_KEY='afeef10dcf63bfc41332bbbf8f6cb2b4'

sheety_endpoint = "https://api.sheety.co/72ca5d6e43dbffca64a86b27e4085755/myWorkouts/workouts"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

load_dotenv()  # reads the .env file

exercise_input = input("What exercises did you do?")


headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response =  requests.post(exercise_endpoint, json=parameters, headers=headers)
results = response.json()
print(f"Nutritionix API call : \n {results} \n")

# Add day and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time =  datetime.now().strftime("%X")

#Sheety Project API
GOOGLE_SHEET_NAME = "My Workouts"
sheety_endpoint = sheety_endpoint

# Sheety API Call and Authentication
for exercise in results["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #NO Authentication
    sheet_response = requests.post(sheety_endpoint, json = sheet_inputs)













