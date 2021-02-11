import speech_recognition as sr
import pyaudio
import pyttsx3
from brightness import set_brightness, get_brightness

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # this gives you all the kinds of voices
engine.setProperty('voice', voices[1].id)
engine.say('')

yesDict = ['yes', 'ya', 'yeah', 'sure']
noDict = ['no', 'nah', 'hell no', 'fuck you']



def talk(text):
    engine.say(text)
    engine.runAndWait()  # need this to say it

# def listen4_start():
#     try:
#         with sr.Microphone() as source:
#             print('waiting...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             while 'stop' not in command:
#                 if 'alexa' in command:
#                     print("running alexa...")
#                     run_alexa()
#     except:  # AttributeError or Exception as e:
#         # print(f"Encountered an error.. ({e})")
#         pass


def listen4_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'log' in command:
                return command
    # except AttributeError or Exception or sr.UnknownValueError as e:
    #     print(f"Encountered an error.. ({e})")
    #     pass
    except:
        pass
    # return command


def wait_for_response():
    command = listen4_command()
    while command is None:
        command = listen4_command()
    return command


def play_song(command):
    song = command.replace('play', '')
    song2 = command.rsplit('play', 2)
    talk('playing' + song2[1])
    print(song)
    print(song2[1])


# def google(command):


def run_alexa():
    talk("sonny do you want a treat")
    # talk("Hello, my name is Log. I am here to serve you.")
    command = wait_for_response()
    print(command)
    if 'play' in command:
        play_song(command)
    if 'brightness' in command:
        get_brightness()
        talk("Would you like to set the brightness?")
        command = wait_for_response()
        if 'yes' in command:
            talk('Would you like to set it relatively or specifically?')
            command = wait_for_response()
            if 'specific' in command:
                talk("Specifically? Ok. What level?")
                command = wait_for_response()
                set_brightness(0, command)
                # listen4_start()
            if 'relative' in command:
                talk("Would you like to increase or decrease your brightness?")
                command = wait_for_response()
                set_brightness(0, command)
                # listen4_start()
                if 'increase' in command:
                    talk("By how much? Please say a number")
                    command = wait_for_response()
                    set_brightness(1, int(command))
                    # listen4_start()
                if 'decrease' in command:
                    talk("By how much? Please say a number")
                    command = wait_for_response()
                    set_brightness(2, int(command))
                    # listen4_start()
        for no in noDict:
            if no in command:
                run_alexa()


if __name__ == "__main__":
    count = 0
    while True:
        count+=1
        run_alexa()
        print(count)
        talk(f"iteration {count}")


