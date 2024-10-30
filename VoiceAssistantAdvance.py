import smtplib
import requests

# Example of an advanced feature: Sending emails
def send_email(to_address, subject, body):
    # Add your email configuration here
    sender_email = "youremail@gmail.com"
    password = "yourpassword"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        email_message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, to_address, email_message)
        server.close()
        speak("Email has been sent successfully.")
    except Exception as e:
        speak(f"Failed to send email due to {str(e)}")

# Fetching weather updates from an API
def get_weather(city):
    api_key = "your_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url).json()
    
    if response["cod"] != "404":
        weather_data = response["main"]
        temperature = weather_data["temp"]
        description = response["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature} degrees Celsius with {description}.")
    else:
        speak("City not found.")

# Enhanced Assistant with advanced tasks
def advanced_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        query = take_command()

        if query is None:
            continue
        
        if 'email' in query:
            speak("Who would you like to send the email to?")
            to_address = take_command()
            speak("What is the subject?")
            subject = take_command()
            speak("What is the message?")
            body = take_command()
            send_email(to_address, subject, body)
        elif 'weather' in query:
            speak("Which city do you want the weather for?")
            city = take_command()
            get_weather(city)
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

# Run the advanced assistant
advanced_assistant()
