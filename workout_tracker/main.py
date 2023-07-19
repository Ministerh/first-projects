import requests
from datetime import datetime

APP_ID = "a28439e0"
APP_KEY = "2b93470c6e87f61ba27dc1ee75e898a7"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
header= {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,    
}


exercsie_params = {
    "query": input("Tell me which exercise you did "),
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 1.8,
    "age": 21

}

response = requests.post(url=exercise_endpoint, json=exercsie_params, headers=header)
result =response.json()['exercises']

sheety_endpoint = 'https://api.sheety.co/3ae30e0ff8f30ddafe69bdbd5c3471a7/workoutTracking/workouts'
date_now = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")
#author_header = ("mminister","v#wg4ac@66jt1%gjh")
author_header =("minister", "gjdkashiaewu")



for exercise in result:
    adjusted_parameter = {
        "workout":
        {
            "date": date_now,
            "time": time_now,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calorie": exercise['nf_calories']


        }

    }
sheet_response = requests.post(url=sheety_endpoint, json=adjusted_parameter, auth=author_header)
print(sheet_response.text)

