import requests

# Function to get weather data
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Change to 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Extracting necessary information
        main = data['main']
        weather = data['weather'][0]
        
        # Printing weather details
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Condition: {weather['description'].capitalize()}")
    else:
        print("City not found. Please check the name and try again.")

# Main function
if __name__ == "__main__":
    api_key = 'your_api_key_here'  # Replace with your actual API key
    city_name = input("Enter city name: ")
    get_weather(city_name, api_key)
