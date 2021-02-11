import screen_brightness_control as sbc
import wmi
import pyttsx3

# The package currently has a bug - this only supports one screen. Will uncomment other methods when bug fix.
engine = pyttsx3.init()


def get_brightness():
    primary_display_brightness = sbc.get_brightness(display=1)
    engine.say(f"Your brightness level is {primary_display_brightness}")


def set_brightness(case, value):
    try:
        value = int(value)
    except TypeError or ValueError:
        case = 3
    if case == 0:  # Set absolute brightness
        sbc.set_brightness(value)
    elif case == 1:  # Set relative brightness (1&2)
        sbc.set_brightness(f'+{str(value)}')
    elif case == 2:
        sbc.set_brightness(f'-{str(value)}')
    elif case == 3:
        engine.say("Sorry, I had trouble setting your brightness. Try again.")
    if case != 3:
        brightness = sbc.get_brightness(display=1)
        engine.say(f"Your new brightness level is {brightness}")

# get_brightness()
# set_brightness(0, 20)


# Multiple screens

# def get_allbrightness():
#     all_screens_brightness = sbc.get_brightness()
#     print(all_screens_brightness)
# get_brightness()


# def set_all(level):
#     screen_count = len(sbc.get_brightness())
#     for num in range(screen_count):
#         sbc.set_brightness(level, display=1)
# set_all(0)




# monitorList = sbc.list_monitors()  # List monitor names
# for monitor in monitorList:
#     sbc.set_brightness(display=1, 100, 100,100)
#     m = sbc.windows.Monitor(monitor)
#     print(m.serial)
#     print(m.name)
# monitor = sbc.windows.Monitor('Unknown AUS2421')
# print(monitor.serial)  # Print model of the one you want
#
# try:
#     sbc.set_brightness(50)
# except sbc.ScreenBrightnessError as error:
#     print(error)



# #increase brightness by 25%
# sbc.set_brightness('+25')
#
# #fade brightness from the current brightness to 50%
# sbc.fade_brightness(50)
#
# #fade the brightness from 25% to 75%
# sbc.fade_brightness(75, start=25)
#
# #fade the brightness from the current value to 100% in steps of 10%
# sbc.fade_brightness(100, increment=10)
#
# #fade the brightness from 100% to 90% with time intervals of 0.1 seconds
# sbc.fade_brightness(90, start=100, interval=0.1)
#
# #fade the brightness to 100% in a new thread
# sbc.fade_brightness(100, blocking=False)