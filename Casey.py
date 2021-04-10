import googletrans
import gtts
import playsound
import pyaudio
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import cv2
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup
import pyautogui
import numpy as np
import random
import math
import sys
from twilio.rest import Client
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from caseyUi import Ui_Casey
import screen_brightness_control as sbc
import wolframalpha
from googletrans import Translator
import pywhatkit
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import date


wfapp = wolframalpha.Client("Your-ID")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello! Good morning! I am Casey. Please tell me how may I help you")
        print("Hello! Good morning! I am Casey. Please tell me how may I help you")

    elif hour >= 12 and hour < 18:
        speak("Hello! Good afternoon! I am Casey. Please tell me how may I help you")
        print("Hello! Good afternoon! I am Casey. Please tell me how may I help you")

    else:
        speak("Hello! Good evening! I am Casey. Please tell me how may I help you")
        print("Hello! Good evening! I am Casey. Please tell me how may I help you")


def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your-email-id', 'your-password')
        server.sendmail('your-email-id', to, content)
        server.quit()
    except Exception:
        speak("Could not send email")
        pass


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.runCasey()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            r.pause_threshold = 1
            r.phrase_threshold = 0.290
            r.energy_threshold = 368
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            query= query.lower()
            print(f"User said: {query}\n")

        except Exception as e:
            return "none"
        return query


    def runCasey(self):
        wishMe()
        while True:
            self.query = self.takeCommand()

            if 'wikipedia' in self.query:
                speak('Searching in Wikipedia...')
                print('Searching in Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print("According to Wikipedia")
                speak(results)
                print(results)

            elif 'play song' in self.query or 'song' in self.query:
                speak("Which song I should play")
                song = self.takeCommand()
                song_result = "playing ", song
                speak(song_result)
                print(song_result)
                pywhatkit.playonyt(song)

            elif 'screenshot' in self.query:
                image = pyautogui.screenshot()
                digits = [i for i in range(0, 10)]
                imageName= ""
                for i in range(6):
                    index = math.floor(random.random() * 10)
                    imageName += str(digits[index])
                image.save("C:\\Users\\vijin\\Pictures\\Screenshots\\"+imageName+".png")
                os.startfile("C:\\Users\\vijin\\Pictures\\Screenshots\\"+imageName+".png")

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif 'open facebook' in self.query:
                webbrowser.open("facebook.com")

            elif 'open instagram' in self.query:
                webbrowser.open("instagram.com")

            elif 'open wikipedia' in self.query:
                webbrowser.open("wikipedia.com")

            elif 'increase volume' in self.query:
                pyautogui.press("volumeup")
                speak("Volume increased")
                print("Volume increased")

            elif 'decrease volume' in self.query:
                pyautogui.press("volumedown")
                speak("Volume decreased")
                print("Volume decreased")

            elif 'close chrome' in self.query:
                os.system("taskkill /f /im " + "chrome.exe")
                speak("Closed Chrome Browser")
                print("Closed Chrome")

            elif 'take photo' in self.query or 'photo' in self.query:
                cam = cv2.VideoCapture(0)

                cv2.namedWindow("test")
                speak("Press Space Bar to click photo and Escape button for closing the window")

                img_counter = 0

                while True:
                    ret, frame = cam.read()
                    if not ret:
                        print("failed to grab frame")
                        break
                    cv2.imshow("test", frame)

                    k = cv2.waitKey(1)
                    if k % 256 == 27:
                        speak("Closing Camera")
                        print("Escape hit, closing...")
                        break
                    elif k % 256 == 32:
                        img_name = "opencv_frame_{}.png".format(img_counter)
                        cv2.imwrite(img_name, frame)
                        speak("Taking Photo")
                        print("Taking photo")
                        print("{} written!".format(img_name))
                        speak("Took Photo")
                        print("Took Photo")
                        img_counter += 1

                cam.release()

                cv2.destroyAllWindows()

            elif 'record video' in self.query or 'video' in self.query:
                speak("The video will be recorded automatically, press the q button in keyboard to stop recording")
                cap = cv2.VideoCapture(0)
                out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), 30, (640, 480))
                while (cap.isOpened()):
                    ret, frame = cap.read()
                    if ret:

                        out.write(frame)

                        cv2.imshow('frame', frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    else:
                        break
                cap.release()
                out.release()
                cv2.destroyAllWindows()

            elif 'mute' in self.query:
                pyautogui.press("volumemute")

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                print(strTime)

            elif 'date' in self.query:
                strDate = str(datetime.date.today())
                todayDate = "Today's date is " ,strDate
                speak(todayDate)
                print(todayDate)

            elif 'open visual studio' in self.query:
                speak("Opening VS Code")
                print("Opening VS code")
                codePath = "C:\\Users\\vijin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open word' in self.query:
                speak("Opening Microsoft Word")
                print("Opening Microsoft Word")
                wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007"
                os.startfile(wordPath)

            elif 'open excel' in self.query:
                speak("Opening Microsoft Excel")
                print("Opening Microsoft Excel")
                excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007"
                os.startfile(excelPath)

            elif 'open media player' in self.query:
                speak("Opening VLC Media Player")
                print("Opening VLC Media Player")
                vlcPath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VideoLAN\\VLC media player"
                os.startfile(vlcPath)

            elif 'email' in self.query:
                contacts = {"vijin": "hai@gmail.com", "joker": "joker@gmail.com"}
                print("To whom should I send the email")
                speak("To whom should I send the email")
                to = self.takeCommand()
                to = to.replace(" ", "")
                print(to)
                x = 0
                for key, value in contacts.items():
                    if key == to:
                        to = value
                        print("What Message should I send")
                        speak("What message should I send")
                        message = self.takeCommand()
                        sendEmail(to, message)
                        x = x + 1

                if x > 0:
                    print("Email send successfully")
                else:
                    print("Couldn't find the contact")

            elif 'increase brightness' in self.query:
                current_brightness = sbc.get_brightness()
                if current_brightness > 90:
                    speak("Brightness is at it's highest level. Can't increase brightness")
                    print("Brightness is at it's highest level. Can't increase brightness")
                else:
                    new_brightness = current_brightness+10
                    print(new_brightness)
                    sbc.set_brightness(new_brightness)
                    updated_brightness = "Brightness increased to " , new_brightness
                    print(updated_brightness)
                    speak(updated_brightness)

            elif 'decrease brightness' in self.query:
                current_brightness = sbc.get_brightness()
                if current_brightness < 10:
                    speak("Brightness is at its lowest level. Can't decrease brightness")
                    print("Brightness is at its lowest level. Can't decrease brightness")
                else:
                    new_brightness = current_brightness-10
                    print(new_brightness)
                    sbc.set_brightness(new_brightness)
                    updated_brightness = "Brightness decreased to " , new_brightness
                    print(updated_brightness)
                    speak(updated_brightness)

            elif 'shut down' in self.query:
                speak("shutting down")
                print("Shutting down")
                os.system('shutdown -s -t 0')

            elif 'sleep' in self.query:
                speak("Hibernating system")
                print("Hibernating system")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif 'weather' in self.query or 'temperature' in self.query:
                speak("which city's temperature do you want to look")
                city = self.takeCommand()
                q = "Temperature of ", city
                res = wfapp.query(q)
                print(next(res.results).text)
                speak(next(res.results).text)

            elif 'mathematics' in self.query or 'calculation' in self.query:
                speak("Tell me the problem")
                question = self.takeCommand()
                res = wfapp.query(question)
                print(next(res.results).text)
                speak(next(res.results).text)

            elif 'translate' in self.query:
                languages = {"hindi": "hi", "english": "en", "malayalam": "ml", "tamil": "ta"}
                dest_lang = ""
                x = 0
                try:
                    speak("In which language do you want me to translate")
                    lang = self.takeCommand()
                    for key, value in languages.items():
                        if key == lang:
                            x = x + 1
                            dest_lang = value
                            break
                    if x > 0:
                        speak("What do you want me to translate")
                        text = self.takeCommand()
                        translator = googletrans.Translator()
                        result = translator.translate(text, dest_lang)
                        print(result.text)
                        translated_audio = gtts.gTTS(result.text, lang=dest_lang)
                        translated_audio.save('audio.mp3')
                        playsound.playsound('audio.mp3')
                    else:
                        speak("Couldn't find language")
                except Exception:
                    speak("Couldn't translate")

            elif 'internet speed' in self.query:
                import speedtest
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                dl_speed = "download speed=", dl, " bits per second"
                up_speed = "upload speed=", up, " bits per second"
                print(dl_speed)
                print(up_speed)
                speak(dl_speed)
                speak(up_speed)

            elif 'joke' in self.query:
                import pyjokes
                jokes = pyjokes.get_jokes(language="en", category="all")
                r1 = random.randint(0, 100)
                joke = jokes[r1]
                speak(joke)
                print(joke, sep="\n")

            elif 'send message' in self.query:
                account_sid = 'your sid'
                auth_token = 'your auth_token'
                client = Client(account_sid, auth_token)
                speak("What do you want me to send?")
                print("What do you want me to send?")
                body = self.takeCommand()

                message = client.messages \
                    .create(
                    body = body,
                    from_='from number',
                    to ='to number'
                )
                print(message.sid)
                speak("Message sent")
                print("Message sent")

            elif 'news' in self.query or 'headlines' in self.query:
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = soup(xml_page, "xml")
                news_list = soup_page.findAll("item")
                for i in range(1, 10):
                    print(news_list[i].title.text)
                    speak(news_list[i].title.text)
                    print(news_list[i].pubDate.text)


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Casey()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("background.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser_4.setText(label_date)
        self.ui.textBrowser.setText(label_time)


app = QApplication(sys.argv)
casey = Main()
casey.show()
sys.exit(app.exec_())








