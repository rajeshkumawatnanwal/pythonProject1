import os
import webbrowser
import random
import pyttsx3
import speech_recognition as sr
import subprocess
import time
import pywhatkit
import threading


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower(), True  # Return the recognized query and a flag indicating successful recognition
    except Exception as e:
        print("Sorry, I couldn't understand. Can you repeat?")
        return "", False  # Return an empty string and a flag indicating unsuccessful recognition


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def search_on_chrome(query):
    subprocess.Popen(
        ['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', f'https://www.google.com/search?q={query}'])
def check_student(name, student_list):
    if name.lower() in [student.lower() for student in  student_list]:
        return True
    else:
        return False

def main():
    print("Hello! Rajesh, I am your assistant. How can I help you today?")
    speak("Hello! Rajesh, I am your assistant. How can I help you today?")
    student_list = ["Rajesh", "Sorabh", "Suyansh", "Subhash", "Anchal"]
    while True:
        command, recognized = listen()

        if recognized:  # Check if the command was successfully recognized
            if "hello" in command:
                speak("Hello! Rajesh, how can I assist you?")
            elif "tell my date of birth" in command:
                speak("Dear Rajesh Kumawat, your date of birth is 27 October 2003")
            elif "open youtube" in command:
                speak("Opening YouTube.")
                webbrowser.open("https://www.youtube.com")
            elif "open college web" in command:
                speak("Opening college website.")
                webbrowser.open("https://cet.iitp.ac.in/moodle/my/")
            elif "open calculator" in command:
                speak("Opening calculator.")
                os.system("calc")
            elif "open notepad" in command:
                speak("Opening notepad.")
                os.system("notepad")
            elif "open browser" in command:
                speak("Opening browser.")
                os.system("start chrome")
            elif "search on chrome" in command:
                query = command.split("search on chrome")[-1].strip()
                search_on_chrome(query)
            elif "check student" in command:
                name = command.split("check student")[-1].strip()
                if check_student(name, student_list):
                    speak(f"Yes, {name} is in the student list.")
                else:
                    speak(f"No, {name} is not in the student list.")
            elif "play music" in command:
                song = command.split("play music")[-1].strip()
                speak(f"Playing {song} on YouTube.")
                pywhatkit.playonyt(song)
            elif "exit" in command:
                speak("Goodbye!")
                exit()
            elif "ok thanks" in command:
                speak("Goodbye! Have a great day!")
                break
            else:
                speak("Sorry, I didn't catch that. Can you repeat?")

        # Add a short delay after each command execution
        time.sleep(1)


if __name__ == "__main__":
    main()
