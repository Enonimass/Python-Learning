import requests

pixel_endpoint = "https://pixe.la/v1/users"
TOKEN = "12345678"
USERNAME = "parsddsssdk"
graph_endpoint =  f"https://pixe.la/v1/users/{USERNAME}/graphs"

params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}



headers = {
    "X-USER-TOKEN": TOKEN
}



graph_params ={
    "id": "test-graph",
    "name": "pushups",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

pixel_params = {
    "date": "",
    "quantity": ""
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)


response =requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)