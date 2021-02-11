from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume


# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get master volume

print(volume.GetMasterVolumeLevel())


def normalize_session(session):
    session = str(session).split(':')
    session = str(session[1]).split('.')
    session = session[0]
    print(session)


def get_master():
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    masterVolume = volume.GetMasterVolumeLevel()
    print(masterVolume)
    return masterVolume


def set_master(method, value):
    masterVolume = get_master()
    try:
        if method == 0:
            volume.SetMasterVolume(masterVolume - value, None)  # Set relative volume
        if method == 2:
            volume.SetMasterVolume(masterVolume - value, None)
        if method == 3:
            volume.SetMasterVolume(3, None)  # Set exact volume
    except Exception as e:
        print(f"Error setting master. {e}")


# Get all audio sessions
def get_sessions():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process:
            # print(f"{session} :%s" % volume.GetMasterVolume())
            normalize_session(session)


def set_session(session_name, value):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session in normalize_session(session):
            print(f"{session} :%s" % volume.GetMasterVolume())
            print(session.DisplayName)
            volume.SetMasterVolume(10, None)

def set_all_sessions():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        try: print(f"{session} :%s" % volume.GetMasterVolume())
        except: print("error getting session")
        print(session.DisplayName)
        volume.SetMasterVolume(0.06, None)

# get_sessions()
# get_master()
# set_master(3,20)
set_all_sessions()