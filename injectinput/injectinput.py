"""
Inject argument as virtual keypresses
"""
import sys
import time
import evdev

translate_upper = {
    " ": evdev.ecodes.ecodes["KEY_SPACE"],
    "(": evdev.ecodes.ecodes["KEY_9"],
    ")": evdev.ecodes.ecodes["KEY_0"],
    "_": evdev.ecodes.ecodes["KEY_MINUS"],
    "+": evdev.ecodes.ecodes["KEY_EQUAL"],
}

translate_lower = {
    " ": evdev.ecodes.ecodes["KEY_SPACE"],
    "-": evdev.ecodes.ecodes["KEY_MINUS"],
    "[": evdev.ecodes.ecodes["KEY_LEFTBRACE"],
    "]": evdev.ecodes.ecodes["KEY_RIGHTBRACE"],
    "=": evdev.ecodes.ecodes["KEY_EQUAL"],
}

translate = {}
translate.update(translate_upper)
translate.update(translate_lower)


def write_characters(uinput, characters):
    """
    Write characters to uinput
    """
    escape = False
    for character in characters:
        if character in translate:
            key = translate[character]
        elif character == "\\":
            escape = True
            continue
        elif escape and character == "r":
            escape = False
            key = evdev.ecodes.ecodes["KEY_ENTER"]
        else:
            key = evdev.ecodes.ecodes["KEY_" + character.upper()]
        if character.isupper() or character in translate_upper:
            uinput.write(
                evdev.ecodes.ecodes["EV_KEY"], evdev.ecodes.ecodes["KEY_LEFTSHIFT"], 1
            )
            uinput.syn()

        uinput.write(evdev.ecodes.ecodes["EV_KEY"], key, 1)
        uinput.syn()
        uinput.write(evdev.ecodes.ecodes["EV_KEY"], key, 0)
        time.sleep(0.05)
        uinput.syn()

        if character.isupper() or character in translate_upper:
            uinput.write(
                evdev.ecodes.ecodes["EV_KEY"], evdev.ecodes.ecodes["KEY_LEFTSHIFT"], 0
            )
            uinput.syn()


def main():
    """
    Main function
    """
    cap = evdev.util.find_ecodes_by_regex(r"KEY_[A-Z0-9]")
    cap[evdev.ecodes.ecodes["EV_KEY"]] += translate.values()
    with evdev.UInput(cap) as uinput:
        write_characters(uinput, sys.argv[1])
