import requests
from datetime import datetime

USERNAME = "minister"
TOKEN ="asdihikduri2g1s3"
# HTTP get post requests using pixela
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "notMinor": "yes",
    "agreeTermsOfService": "yes"
}

# To make a post request you use the post method this will help to create an account

# response =requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#graph part
graph_endpoint  = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "python code",
    "unit": "commit",
    "type": "int",
    "color": "sora",    
}#the use  of this parameter helps to secure the key

header = {
    "X-USER-TOKEN": TOKEN
}
# response =requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)

#step 4
today = datetime.now()


entry_endpoinnt = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

entry_params  = {
    #this will format  the  date according to how we want it to be
    "date":  today.strftime("%Y%m%d"),
    "quantity":"2"
}
# response = requests.post(url=entry_endpoinnt, json=entry_params, headers=header)
# print(response.text)

# how to update usnng  http request

update_endpoint = f"https://pixe.la/v1/users/{USERNAME}"

update_token_params = {
    "newToken" : "asdihikduri2g1s3",
}
update_pixel_endpoinnt =f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
update_pixel_params ={
    "quantity": "4",    
}
# to update pixel
# response = requests.put(url=update_pixel_endpoinnt, json=update_pixel_params, headers=header)
# print(response.text)


# response = requests.put(update_endpoint, json=update_token_params, headers=header)
# print(response.text)

#To delete a pixel


response =requests.delete(url=update_pixel_endpoinnt, headers=header)
print(response.text)