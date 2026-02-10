import pyttsx3
import datetime

# -------- Text to Speech --------
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# -------- Text Input (Voice Simulated) --------
def listen():
    command = input("Type your command: ")
    return command.lower()

# -------- Features --------
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")
    print("Time:", time)

def set_reminder():
    speak("What should I remind you about?")
    reminder = listen()
    speak("Reminder noted")
    print("Reminder:", reminder)

def check_weather():
    speak("Checking weather")
    print("Weather: Demo mode")
    speak("Weather feature is in demo mode")

def read_news():
    speak("Reading news")
    print("News: Demo mode")
    speak("News feature is in demo mode")

# -------- Main Assistant --------
speak("Hello, I am your personal assistant")

while True:
    command = listen()

    if "time" in command:
        tell_time()

    elif "reminder" in command:
        set_reminder()

    elif "weather" in command:
        check_weather()

    elif "news" in command:
        read_news()

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        print("Assistant stopped.")
        break

    elif command != "":
        speak("Sorry, I did not understand")
        print("Unknown command")
