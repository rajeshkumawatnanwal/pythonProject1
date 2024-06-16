import os
import webbrowser
import random
import re
import pyttsx3
import speech_recognition as sr
import subprocess
import time
import datetime
import pywhatkit

from googletrans import Translator
import threading
import wikipedia
import schedule
from datetime import date, timedelta
import smtplib
import requests
import socket
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
import pyautogui


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am Listening please say something ...")
        audio = recognizer.listen(source)

    try:
        print(" wait i am Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower(), True
    except Exception as e:
        print("Sorry, I couldn't understand. please repeat")
        return "", False


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def search_on_chrome(query):

    subprocess.Popen(
        ['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', f'https://www.google.com/search?q={query}'])

def take_screenshot(save_path='screenshot1.png'):

    screenshot = pyautogui.screenshot()


    screenshot.save(save_path)
    print(f"Screenshot saved as {save_path}")

def send_email(subject, body, reciver_email):
    sender_email = "rkn59762@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "rkn59762@gmail.com"
    password = "**** **** **** ****"

    try:

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = reciver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        server.sendmail(sender_email, reciver_email, msg.as_string())
        server.quit()

        print("Email sent successfully!")
        speak("Email sent successfully!")
    except socket.gaierror as e:
        print(f"Failed to send email due to network error: {e}")
        speak(f"Failed to send email due to network error: {e}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        speak(f"Failed to send email: {e}")


def get_current_time():
    now = datetime.now().strftime("%H:%M")
    speak(f"The time is {now}")
    print(f"The time is {now}")
def unit_conversion(conversion_type,value):

    if conversion_type == "miles to kilometers":
        result = value * 1.60934
    elif conversion_type == "kilometres to miles":
        result = value * 0.621371
    elif conversion_type == "kilometres to metres":
        result = value * 1000


    elif conversion_type == "metres to kilometres":
        result = value * 0.001
    elif conversion_type == "foot to meter":
        result = value * 0.3048

    elif conversion_type == "pounds to kilograms":
        result = value * 0.453592
    elif conversion_type == "kilograms to pounds":
        result = value * 2.20462
    else:
        return None
    print(f"your answer is {result}")
    speak(f"your answer is {result}")

quiz_assignments = {
    "Quiz 1": date(2024, 6, 10),
    "Quiz 2": date(2024, 6, 29),
    "Quiz 3": date(2024, 6, 30)
}


def remind_quiz_assignments():
    today = date.today()
    for assignment, due_date in quiz_assignments.items():
        if due_date == today:
            speak(f"Reminder: {assignment} is due today.")
        elif due_date == today + timedelta(days=1):
            speak(f"Reminder: {assignment} is due tomorrow.")
        elif due_date > today:
            days_until_due = (due_date - today).days
            speak(f"Don't forget! {assignment} is due in {days_until_due} days on {due_date.strftime('%Y-%m-%d')}")


def check_student(name, student_list):
    if name.lower() in [student.lower() for student in student_list]:
        return True
    else:
        return False


syllabus = {
    "Physics": ["Mechanics", "Electronics", "Modern physics"],
    "Biology": ["Human health", "Genetics"],
    "Mathematics": ["Vector and 3D", "Mathematical reasoning", "trignometry"]
}


def check_topic_in_syllabus(topic, syllabus):
    topic_lower = topic.lower()
    for subject, topics in syllabus.items():
        topics_lower = [t.lower() for t in topics]
        if topic_lower in topics_lower:
            return True, subject
    return False, None


syllabus = {
    "physics": ["Mechanics", "Electronics", "Modern physics"],
    "Biology": ["Human health", "Genetics"],
    "Mathematics": ["Vector and 3D", "Mathematical reasoning", "Trigonometry"]
}


def get_topics_by_subject(subject, syllabus):
    if subject in syllabus:
        return syllabus[subject]
    else:
        return None


syllabus = {
    "physics": ["Mechanics", "Electronics", "Modern physics"],
    "biology": ["Human health", "Genetics"],
    "mathematics": ["Vector and 3D", "Mathematical reasoning", "Trigonometry"]
}


def get_roll_number(student_name, student_roll_numbers):
    if student_name in student_roll_numbers:
        return student_roll_numbers[student_name]
    else:
        return None


student_roll_numbers = {
    'shyam': '101',
    'ram': '102',
    'rajesh': '103',
}


def search_wikipedia(command):
    try:
        results = wikipedia.summary(command, sentences=2)
        return results
    except wikipedia.exceptions.DisambiguationError as e:
        results = str(e)
    except wikipedia.exceptions.PageError as e:
        results = "No page found for the query."
    return results


def translate(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    print(f"Translated text: {translated.text}")
    return translated.text
def wish_user():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning")
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon !")
        speak("Good Afternoon !")
    else:
        print("Good Evening !")
        speak("Good Evening !")
    speak("i am your assistant , how can i help you")
def get_weather(city):
    api_key = "2990f9774af8c06be84c398f9cda0d60"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city},IN&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == "200":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        weather_description = weather["description"]
        weather_report = f"The temperature in {city} is {temperature} degrees Celsius with {weather_description}."
        speak(weather_report)
    else:
        speak("City not found. Please try again.")
def set_timer(seconds):
    print(f"Timer set for {seconds} seconds.")
    speak(f"Timer set for {seconds} seconds.")
    time.sleep(seconds)
    print("Time's up!")
    speak("Time's up!")
def start_stopwatch():
    start_time = time.time()
    print("Stopwatch started. Say 'ok' to stop the stopwatch.")
    speak("Stopwatch started. Say 'ok' to stop the stopwatch.")
    while True:
        command = listen()

        if "ok stop" in command:

            total_time = time.time() - start_time
            print(f"Stopwatch stopped. total time: {total_time :.2f} seconds")
            speak(f"Stopwatch stopped. total time: {total_time :.2f} seconds")
            break
        #     break
        # else:
        #     speak("if you want to stop stopwatch please say ok")


def main():
    print("Hello! Rajesh,  How can I help you today?")
    speak("Hello! Rajesh,  How can I help you today?")
    student_list = ["Rajesh", "Sorabh", "Suyansh", "Subhash", "Anchal"]

    while True:
        command, recognized = listen()

        if recognized:
            if "hello" in command:
                speak("Hello! Rajesh, how can I assist you?")
            if "reminder" in command:
                remind_quiz_assignments()
            if "wish me" in command:
                wish_user()
            if "unit conversion" in command:
                speak("tell me type of conversion")
                conversion_type, _ = listen()
                print(conversion_type)
                speak("tell me value ")
                value_str ,_= listen()

                value=int(value_str.split()[-1])
                print(value)



                result=unit_conversion(conversion_type, value)
            if 'wikipedia' in command:
                speak('Searching Wikipedia...')
                command = command.split("wikipedia")[-1].strip()
                results = search_wikipedia(command)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            if "timer" in command:
                try:
                    seconds = int(command.split()[-2])
                    set_timer(seconds)
                except ValueError:
                    print("Invalid command. Example usage: 'set timer for 10 seconds'")
            time.sleep(3)
            if "open google" in command:
                speak("opening google")
                webbrowser.open("google.com")

            if "translate" in command:
                speak("Please tell me the text you want to translate.")
                text_to_translate, recognized_text = listen()
                if recognized_text:
                    speak("Which language do you want to translate to?")
                    language, recognized_language = listen()
                    if recognized_language:
                        translated_text = translate(text_to_translate, language)
                        speak(translated_text)
                        time.sleep(2)
                        speak("anything else ")

            elif 'city' in command:


                speak("Which city's weather would you like to know?")
                city = listen()
                get_weather(city)

            elif "time" in command:
                get_current_time()
            elif "stopewatch" in command:
                start_stopwatch()

            elif "check syllabus" in command:
                topic = command.split("check syllabus")[-1].strip()
                if topic:
                    found, subject = check_topic_in_syllabus(topic, syllabus)
                    if found:
                        response = f"The topic '{topic}' is in the {subject} subject."
                    else:
                        response = f"The topic '{topic}' is not found in the syllabus."
                    print(response)
                    speak(response)

            elif "tell me topics" in command:
                subject_to_check = command.split("tell me topics of")[-1].strip().lower()
                topics = get_topics_by_subject(subject_to_check, syllabus)

                if topics:
                    speak(topics)
                    print(f"The topics covered under '{subject_to_check}' are: {', '.join(topics)}")
                else:

                    print(f"No topics found for the subject '{subject_to_check}'.")

            elif "roll number" in command:
                student_name = command.split("roll number of")[-1].strip()
                roll_number = get_roll_number(student_name, student_roll_numbers)
                if roll_number:
                    print(f"The roll number of {student_name} is {roll_number}.")
                    speak(f"The roll number of {student_name} is {roll_number}.")
                else:
                    print(f"Roll number not found for {student_name}.")
                    speak(f"Roll number not found for {student_name}.")

            elif 'price of' in command:
                query = command.replace('price of', '')
                query = "https://www.amazon.in/s?k=" + query[-1]
                webbrowser.open(query)

            elif 'open github' in command:
                speak("opening github")
                webbrowser.open("github.com")
                # elif "camera" or "take a photo" in command:
                #     ec.capture(0, "robo camera", "img.jpg")
            elif "shutdown" in command:
                os.system("shutdown /s /t 1")
            elif "restart" in command:
                os.system("shutdown /r /t 1")
            elif "log off" in command:
                os.system("shutdown -l")
            elif "tell my date of birth" in command:
                speak("Dear Rajesh Kumawat, your date of birth is 27 October 2003")
            elif "open youtube" in command:
                speak("Opening YouTube.")
                webbrowser.open("https://www.youtube.com")
            elif "open college web" in command:
                speak("Opening college website.")
                webbrowser.open("https://cet.iitp.ac.in/moodle/my/")
            if "send email" in command:
                while True:
                    speak("Please tell me the recipient's email address.")
                    reciver_em, _ = listen()
                    reciver_email_half = reciver_em.replace(" ", "")

                    reciver_email = reciver_email_half + "@gmail.com"
                    print(reciver_email)

                    speak(f"You said {reciver_email} . Is that correct?  ")
                    confirmation, _ = listen()
                    print(f"Confirmation received: '{confirmation}'")
                    if "yes" in confirmation:
                        break

                    else:
                        speak("Okay, let's try again.")

                speak("What is the subject of the email?")
                subject, _ = listen()
                speak("What is the body of the email?")
                body, _ = listen()

                send_email(subject, body, reciver_email)
                speak("Email has been sent. How else can I assist you?")










            elif "open calculator" in command:
                speak("Opening calculator.")
                os.system("calc")
            elif "screenshot" in command:
                take_screenshot("screenshot1.png")
                speak("screenshot saved")
            

            elif "open notepad" in command:
                speak("Opening notepad.")
                os.system("notepad")
            elif "open browser" in command:
                speak("Opening browser.")
                os.system("start chrome")
            elif "search on chrome" in command:
                query = command.split("search on chrome")[-1].strip()
                search_on_chrome(query)

            elif "open visual studio code" in command:

                os.startfile("C:\\Users\\rk093\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
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

        time.sleep(2)


if __name__ == "__main__":
    main()

