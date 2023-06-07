import requests


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_pos = (longitude, latitude)

# print(iss_pos)

parameters = {
    "lat":51.507351,
    "lng":-0.127758,
    "formatted":0
}

res = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
res.raise_for_status()
data = res.json()

sunrise = data['results']['sunrise']
sunrise = sunrise.split("T")[1]
sunset = data['results']['sunset']
sunset = sunset.split("T")[1]

print(f"({sunrise}, {sunset})")
