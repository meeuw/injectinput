import evdev
import sys
import time

def main():
    with evdev.UInput() as ui:
        escape = False
        for letter in sys.argv[1]:
            if letter == ' ':
                key = evdev.ecodes.KEY_SPACE
            elif letter == '\\':
                escape = True
                continue
            elif escape and letter == 'r':
                escape = False
                key = evdev.ecodes.KEY_ENTER
            else:
                key = evdev.ecodes.ecodes['KEY_'+letter.upper()]
            if letter.isupper():
                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 1)

            ui.write(evdev.ecodes.EV_KEY, key, 1)
            ui.write(evdev.ecodes.EV_KEY, key, 0)
            time.sleep(.05)
            ui.syn()

            if letter.isupper():
                ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 0)
        ui.syn()
