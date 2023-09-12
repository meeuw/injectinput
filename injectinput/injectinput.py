import evdev
import sys
import time

translate_upper = {
    " ": evdev.ecodes.KEY_SPACE,
    "(": evdev.ecodes.KEY_9,
    ")": evdev.ecodes.KEY_0,
    "_": evdev.ecodes.KEY_MINUS,
}

translate_lower = {
    " ": evdev.ecodes.KEY_SPACE,
    "-": evdev.ecodes.KEY_MINUS,
    "[": evdev.ecodes.KEY_LEFTBRACE,
    "]": evdev.ecodes.KEY_RIGHTBRACE,
}

translate = {}
translate.update(translate_upper)
translate.update(translate_lower)

def write_string(ui, letters):
    escape = False
    for letter in letters:
        if letter in translate:
            key = translate[letter]
        elif letter == "\\":
            escape = True
            continue
        elif escape and letter == "r":
            escape = False
            key = evdev.ecodes.KEY_ENTER
        else:
            key = evdev.ecodes.ecodes["KEY_" + letter.upper()]
        if letter.isupper() or letter in translate_upper:
            ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 1)

        ui.write(evdev.ecodes.EV_KEY, key, 1)
        ui.write(evdev.ecodes.EV_KEY, key, 0)
        time.sleep(0.05)
        ui.syn()

        if letter.isupper() or letter in translate_upper:
            ui.write(evdev.ecodes.EV_KEY, evdev.ecodes.KEY_LEFTSHIFT, 0)
    ui.syn()

def main():
    with evdev.UInput(
        evdev.util.find_ecodes_by_regex(r"KEY_([A-Z0-9]|SPACE|LEFTSHIFT|ENTER|MINUS|LEFTBRACE|RIGHTBRACE)$")
    ) as ui:
        write_string(ui, sys.argv[1])
