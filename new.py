import requests

# Replace with your actual WeatherAPI key
API_KEY = "24b13d0c2c844a92b3b183105250903"

# Take user input for city
CITY = input("Enter your city: ")

# API URL with user-inputted city
URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days=7&aqi=no&alerts=no"

# Make a request to the WeatherAPI
response = requests.get(URL)
data = response.json()

# Check if the request was successful
if "forecast" in data:
    print(f"\n3-Day Weather Forecast for {CITY}:\n")
    for day in data["forecast"]["forecastday"]:
        date = day["date"]
        temp = day["day"]["avgtemp_c"]  # Average temperature in Celsius
        humidity = day["day"]["avghumidity"]  # Average humidity
        rainfall = day["day"]["totalprecip_mm"]  # Total precipitation in mm
        print(f"Date: {date}, Temp: {temp}°C, Humidity: {humidity}%, Rainfall: {rainfall}mm")
else:
    print("Error: Unable to fetch weather data. Please check your city name or API key.")
