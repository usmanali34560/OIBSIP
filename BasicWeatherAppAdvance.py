import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For displaying weather icons

# Function to get weather data from API
def get_weather(city_name, api_key, units='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': units
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", "City not found!")
        return None

# Function to update weather info in the GUI
def update_weather():
    city_name = city_entry.get()
    unit = "metric" if unit_var.get() == "Celsius" else "imperial"
    weather_data = get_weather(city_name, api_key, units=unit)
    
    if weather_data:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        condition = weather_data['weather'][0]['description'].capitalize()
        icon_id = weather_data['weather'][0]['icon']
        
        # Display the weather data
        temp_label.config(text=f"Temperature: {temp}°{unit_var.get()[0]}")
        humidity_label.config(text=f"Humidity: {humidity}%")
        condition_label.config(text=f"Condition: {condition}")
        
        # Update the weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
        icon_image = Image.open(requests.get(icon_url, stream=True).raw)
        icon_image = icon_image.resize((100, 100), Image.ANTIALIAS)
        weather_icon = ImageTk.PhotoImage(icon_image)
        icon_label.config(image=weather_icon)
        icon_label.image = weather_icon

# Main GUI window
app = tk.Tk()
app.title("Weather App")

# API Key (Replace with your own key)
api_key = 'your_api_key_here'

# City Input
city_label = tk.Label(app, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

# Temperature Unit Selection
unit_var = tk.StringVar(value="Celsius")
unit_frame = tk.Frame(app)
unit_frame.pack()

celsius_button = tk.Radiobutton(unit_frame, text="Celsius", variable=unit_var, value="Celsius")
fahrenheit_button = tk.Radiobutton(unit_frame, text="Fahrenheit", variable=unit_var, value="Fahrenheit")

celsius_button.pack(side="left")
fahrenheit_button.pack(side="left")

# Weather Data Display
temp_label = tk.Label(app, text="Temperature: ")
temp_label.pack()

humidity_label = tk.Label(app, text="Humidity: ")
humidity_label.pack()

condition_label = tk.Label(app, text="Condition: ")
condition_label.pack()

# Weather Icon Display
icon_label = tk.Label(app)
icon_label.pack()

# Button to get weather
get_weather_button = tk.Button(app, text="Get Weather", command=update_weather)
get_weather_button.pack()

# Run the Tkinter loop
app.mainloop()
