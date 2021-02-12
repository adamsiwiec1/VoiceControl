import speech_recognition as sr
import pyaudio
import pyttsx3

from brightness import set_brightness, get_brightness
from requests import request
from googlesearch import search
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
# with SpotifyLocal as s:
#     pass

# Spotipy - full access to music data but dont think you can play. Possibly look up uri's?

#sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="1a1b29ec4ca0490d960ea3af156bf040",
 #                                               client_secret="324fc99174ed4f55a62fcc2f22409dac")
                                                # #redirect_uri="https://developer.spotify.com/dashboard/applications/1a1b#29ec4ca0490d960ea3af156bf040",
                                                # scope="user-library-read"))

# sp.current_user_saved_tracks()
#sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # this gives you all the kinds of voices
engine.setProperty('voice', voices[1].id)
engine.say('')

yesDict = ['yes', 'ya', 'yeah', 'sure']
noDict = ['no', 'nah', 'hell no']


def talk(text):
    engine.say(text)
    engine.runAndWait()  # need this to say it


def listen4_command():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'stupid' in command:
                return command
    # except AttributeError or Exception or sr.UnknownValueError as e:
    #     print(f"Encountered an error.. ({e})")
    #     pass
    except:
        pass
    # return command


def raw_command():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

def wait_for_response():
    print(f'listening...0')
    command = listen4_command()
    count = 0
    while command is None:
        count =+ 1
        print(f'listening...{1}')
        command = listen4_command()
    return command


def play_song(command):
#    print(s.get_current_status(s))
#   print(s.connect(s))
#    s.skip(s)
#    print(s.skip(s))
    song = command.replace('play', '')
    song2 = command.rsplit('play', 2)
    try:
        talk('playing' + song2[1])
    except IndexError:
        talk("Error playing song.")
        pass
    print(song)
    print(song2[1])


def google(command):
    resultList = []
    webbrowser.open("http://www.google.com")
    for j in search(command, tld='com', lang='en', num=3, stop=3, pause=0):
        webbrowser.open(j)


def run_alexa():
    # talk("sonny do you want a treat")
    # talk("Hello, my name is Log. I am here to serve you.")
    command = wait_for_response()
    print(command)
    if 'hi stoopid' in command:
        talk('hi how can i help you')
    elif 'google' in command:
        google(command)
        talk(f"Searching for {command}")
    elif 'play' in command:
        play_song(command)
    elif 'brightness' in command:
        get_brightness()
        talk("Would you like to set the brightness?")
        command = wait_for_response()
        if 'yes' in command:
            talk('Would you like to set it relatively or specifically?')
            command = wait_for_response()
            if 'specific' or "specifically" in command:
                talk("Specifically? Ok. What level?")
                command = raw_command()
                while command is None:
                    command = raw_command()
                set_brightness(0, command)
            if 'relative' in command:
                talk("Would you like to increase or decrease your brightness?")
                command = wait_for_response()
                if 'increase' in command:
                    talk("By how much? Please say a number")
                    command = raw_command()
                    while command is None:
                        command = raw_command()
                    set_brightness(1, int(command))
                if 'decrease' in command:
                    talk("By how much? Please say a number")
                    command = raw_command()
                    while command is None:
                        command = raw_command()
                    set_brightness(2, command)
        if 'no' in command:
            talk('Restarting')
            run_alexa()


if __name__ == "__main__":
    count = 0
    while True:
        count+=1
        run_alexa()


