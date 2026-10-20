import requests

city = input("Enter city name: ")

try:
    # Find the city's coordinates
    url = "https://geocoding-api.open-meteo.com/v1/search"
    response = requests.get(
        url,
        params={"name": city, "count": 1},
        timeout=10
    )
    response.raise_for_status()
    places = response.json().get("results", [])

    if not places:
        print("City not found.")
    else:
        place = places[0]
        latitude = place["latitude"]
        longitude = place["longitude"]

        # Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"
        response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,weather_code"
            },
            timeout=10
        )
        response.raise_for_status()
        weather = response.json()["current"]

        print("City:", place["name"])
        print("Temperature:", weather["temperature_2m"], "°C")
        print("Humidity:", weather["relative_humidity_2m"], "%")
        print("Weather code:", weather["weather_code"])

except requests.RequestException:
    print("Unable to get weather. Check your internet connection.")