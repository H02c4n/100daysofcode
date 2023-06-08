import requests
import os
from twilio.rest import Client

API_KEY = "8fc495c975dc5f64690d2cfebc1b548e"
OWM_URL = "https://api.openweathermap.org/data/2.5/forecast"



parameters = {
    "lat": 37.872734,
    "lon": 32.4924376,
    "appid": API_KEY
}


response = requests.get(OWM_URL, params=parameters)
response.raise_for_status()

data = response.json()
data = data["list"][0]["weather"][0]["description"]

print(data)

account_sid = "AC08cd37f39672b4cf227609c0a8d3d198"
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)
message = client.messages.create(
  body=data,
  from_="+13613147512",
  to="+46762125153"
)
print(message.status)