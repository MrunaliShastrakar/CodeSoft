import requests

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == 200:
        weather_info = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        print(f"Weather: {weather_info}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or API error")

if __name__ == "__main__":
    api_key = "4e1e299dcc6a6c4ee4c29ee061f79d00"
    city = input("Enter a city name: ")
    weather_data = get_weather_data(api_key, city)
    display_weather(weather_data)
