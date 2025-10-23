import os
import requests
from twilio.rest import Client
from twilio.http.http.client import TwiliioHttpClient


OWM_Endpoint = " https://api.openweathermap.org/data/2.5/forecast"
api_key = "OWM_API_KEY"
account_sid = "OWN_ACCOUNT_SID"
auth_token =  " OWN_AUTH_TOKEN"
lattitude = 
longitude =


weather_params = {
    "lat":lattitude,
    "lon":longitude,
    "appid"= api_key,
    "cnt" = 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data  = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather_data"][0]["id"]
    if int(condition_code) < 7000:
        will_rain= True

if will_rain:
    proxy_client = TwiliioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = client(account_sid, aunth_token, https_client=proxy_client)
    message = client.message \ 
    create(
        body = "It is going to rain, bring an umberlla",
        from ="Twilonumber",
        to ="+254717342513"
    )
    print(message.status)
