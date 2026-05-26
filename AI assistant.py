import speech_recognition as sr # type: ignore # convert speech to text
import pyttsx3 # type: ignore # convert text to speech
import webbrowser
import datetime
import os
import wikipedia # type: ignore

# Voice setup
engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    if "Samantha" in voice.name:
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150)

# Speak function
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        speak("Sorry, I could not understand")
        return ""

# Main assistant
speak("Hello Rithika. I am your AI assistant.")

while True:

    command = take_command()

    # Open websites
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail")

    elif "open chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT")

    # Open Mac apps
    elif "open calculator" in command:
        os.system("open -a Calculator")

    elif "open notes" in command:
        os.system("open -a Notes")

    elif "open safari" in command:
        os.system("open -a Safari")

    elif "open vscode" in command:
        os.system("open -a 'Visual Studio Code'")

    elif "open whatsapp" in command:
        os.system("open -a WhatsApp")

    elif "open spotify" in command:
        os.system("open -a Spotify")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Wikipedia search
    elif "search wikipedia" in command:

        speak("What should I search?")

        topic = take_command()

        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)

        except:
            speak("No results found")

    # Search Google
    elif "search" in command:

        search_term = command.replace("search", "")

        webbrowser.open(f"https://www.google.com/search?q={search_term}")

        speak(f"Searching for {search_term}")

    # Exit
    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        break

    else:
        speak("Command not recognized")