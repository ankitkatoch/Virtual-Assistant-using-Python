import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import random
from colorama import init, Fore, Back, Style
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

init(convert=True)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# assistant_voice = 0
engine.setProperty('voice', voices[0].id)
assistant_name = "DAVID"
# print(assistant_voice)
# if "DAVID" in voices[assistant_voice].id:
#     assistant_name = "DAVID"
# else:
#     assistant_name = "ZIRA"
# print(assistant_name)
# speak(f"My name is {assistant_name}")
# print(voices[0].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour < 12:
        speak('Good morning')
    elif hour >= 12 and hour < 18:
        speak('Good afternoon')
    else:
        speak('Good evening')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print(Fore.YELLOW+"Listening...")
        speak("Listening...")
        audio = r.listen(source)
        try:
            print(Fore.MAGENTA+"Recognising...")
            speak("Recognising...")
            query = r.recognize_google(audio, language="en-in")
            print(Fore.GREEN+f"You said : {query}" + Style.RESET_ALL)
            # print(Style.RESET_ALL)
        except Exception as e:
            speak(
                'I did not recognise your voice. Please check your Internet connection..')
            # query = take_command().lower()
            return "None"
    return query


def open_browser(search_query, link):
    driver = webdriver.Firefox(
        executable_path="D:\projects\Akshu - Virtual Assistant\driver\geckodriver.exe")
    try:
        driver.set_page_load_timeout(50)
        wait = WebDriverWait(driver, 3)
        visible = EC.visibility_of_element_located
        driver.get(link + search_query)
        if "https://www.youtube.com/results?search_query=" in link:
            wait.until(visible((By.ID, "video-title")))
            driver.find_element_by_id("video-title").click()
    except Exception as e:
        speak("Your Internet connection is weak. Please check your Internet connection.")


if __name__ == "__main__":
    wish_me()
    speak(
        f"Hello Ankit sir, My name is {assistant_name} I am your Virtual assistant...")
    print(Fore.LIGHTMAGENTA_EX +
          "Press 1 to start the David...\nPress any other key to exit..")
    # speak("Press 1 to start the David...\nPress any other key to exit..")
    print(Fore.LIGHTCYAN_EX)
    start = int(input("Enter your option : "))
    print(Style.RESET_ALL)
    if start == 1:
        starting_message = "Let's start "
        speak(starting_message)
    else:
        exit()
    a = 1
    while a:
        query = take_command().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            search_query = query.replace("wikipedia", "")
            results = wikipedia.summary(search_query, sentences=2)
            print(results)
            speak(results)

        if "youtube" in query:
            search_query = query.replace("youtube", "")
            link = "https://www.youtube.com/results?search_query="
            open_browser(search_query, link)

        elif "google" in query:
            search_query = query.replace("google", "")
            link = "https://www.google.com/search?client=firefox-b-d&q="
            open_browser(search_query, link)

        elif "play music" in query:
            music_dir = 'D:\music1\music'
            songs = os.listdir(music_dir)
            l = list(range(0, len(songs)))
            music_choice = random.choice(l)
            os.startfile(os.path.join(music_dir, songs[music_choice]))

        elif "play video songs" in query:
            music_dir = 'D:\\video songs'
            video_songs = os.listdir(music_dir)
            l = list(range(0, len(video_songs)))
            music_choice = random.choice(l)
            os.startfile(os.path.join(music_dir, video_songs[music_choice]))

        elif "play god music" in query:
            music_dir = 'D:\music1\god music'
            songs = os.listdir(music_dir)
            l = list(range(0, len(songs)))
            music_choice = random.choice(l)
            os.startfile(os.path.join(music_dir, songs[music_choice]))

        elif "open code" in query:
            os.startfile(
                "C:\\Users\\Ankit\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe")

        elif "shutdown computer" in query:
            os.system("shutdown /s /t 1")

        elif "restart computer" in query:
            os.system("shutdown /r /t 1")

        elif "open photos" in query:
            os.startfile("D:\Pictures")

        elif "open movies" in query:
            os.startfile("D:\movies")

        elif "your name" in query:
            speak(f"My name is {assistant_name}")

        elif "made you" in query:
            speak("Sir Ankit made me")

        elif "birth place" in query:
            speak("My birth place is Bhota. District - Hamirpur, Himachal Pradesh")

        print(Fore.YELLOW)
        print("Press 1 to continue with Virtual Assistant...\nPress 2 for help menu\nPress any other key to exit it")
        print(Fore.CYAN)
        a = int(input("Enter your Choice : "))
        if a == 2:
            print(
                Fore.MAGENTA + "\nSay the following code to me       -                    I will do this for you")
            print(Fore.GREEN)
            print(
                "wikipedia <query-name>             -                    Search query on Wikipedia")
            print(
                "youtube   <query-name>             -                    Serach query on YouTube and play video")
            print(
                "google    <query-name>             -                    Search query on Google")
            print(
                "open code                          -                    Open Visual Studio Code")
            print(
                "play music                         -                    Play random music")
            print(
                "play god music                     -                    Play random god songs")
            print(
                "play video songs                   -                    Play random video songs")
            print(
                "open photos                        -                    Open Photos folder")
            print(
                "open movies                        -                    Open movies folder")
            print("your name                          -                    My name")
            print(
                "birth place                        -                    My birth place")
            print(
                "made you                           -                    My creater's name")
            print(
                "shutdown computer                  -                    Shutdown the computer")
            print(
                "restart computer                   -                    Restart the computer\n")
            time.sleep(7)
        elif a != 1:
            speak(
                "Bye Bye Ankit sir, I hope you enjoyed this interactive session. ")
            exit()
        # if a == 2:
        #     print(
        #         "Press 1 to change username\nPress 2 for male voice \nPress 3 for female voice\n")
        #     b = int(input("Enter your Choice : "))
        #     if b == 1:
        #         speak("Enter new username")
        #         new_username = input("Enter new username : ")
        #         speak("Are you male")
        #         sex = input("Are you male - y/n : ")
        #         if sex == 'y':
        #             username = new_username + "sir"
        #         else:
        #             username = new_username + "madam"
        #         speak(f"{username}")
            # elif b == 2:
            #     engine.setProperty('voice', voices[1].id)
            #     assistant_voice = 1
            #     assistant_name = "DAVID"

            # elif b == 3:
            #     engine.setProperty('voice', voices[0].id)
            #     assistant_voice = 0
            #     assistant_voice = "ZIRA"
