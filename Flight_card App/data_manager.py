import requests
sheety_endpoint = "https://api.sheety.co/3ae30e0ff8f30ddafe69bdbd5c3471a7/flightData/workouts"
header = { "Authorization": "Bearer efghdtycvnkgohkp1"}
class DataManager:
    def __init__(self) -> None:
        
    #This class is responsible for talking to the Google Sheet.
        self.data ={}

    def prices(self):
        response = requests.get(sheety_endpoint,headers=header )
        result = response.json()
        self.data = result['workouts']
        return self.data
    
    def data_update(self):
        for city in self.data:
            new_data = { "workout": 
             {
                 "iataCode":city["iataCode"]

            }
             }
        response= requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data, headers=header)
        print(response.text)


        
   
