import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take user voice input and convert to text
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)
            query = query.lower()
            print(f"User said: {query}")
            return query
    except Exception as e:
        print("Sorry, I could not understand. Please say that again.")
        return None

# Basic voice assistant functionality
def basic_assistant():
    speak("Hello! How can I assist you?")
    while True:
        query = take_command()

        if query is None:
            continue
        
        if 'hello' in query:
            speak("Hi there!")
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif 'date' in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")
        elif 'search' in query:
            speak("What should I search for?")
            search_query = take_command()
            if search_query:
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                speak(f"Searching for {search_query}")
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

# Run the assistant
basic_assistant()
