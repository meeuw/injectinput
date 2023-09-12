"""
Tests for injectinput
"""
import unittest.mock
import evdev.ecodes
import injectinput.injectinput


def test_characters():
    """
    Test simple characters
    """
    uinput = unittest.mock.MagicMock()
    injectinput.injectinput.write_characters(uinput, "letters")
    assert uinput.mock_calls == [
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_L"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_L"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_E"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_E"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_T"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_T"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_T"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_T"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_E"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_E"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_R"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_R"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_S"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_S"], 0),
        unittest.mock.call.syn(),
    ]


def test_special_characters():
    """
    Test special characters
    """
    uinput = unittest.mock.MagicMock()
    injectinput.injectinput.write_characters(uinput, "\\rL[(")
    assert uinput.mock_calls == [
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_ENTER"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_ENTER"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_LEFTSHIFT"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_L"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_L"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_LEFTSHIFT"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_LEFTBRACE"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_LEFTBRACE"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_LEFTSHIFT"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_9"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_9"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_LEFTSHIFT"], 0),
        unittest.mock.call.syn(),
    ]

def test_last_upper():
    """
    Test last upper
    """
    uinput = unittest.mock.MagicMock()
    injectinput.injectinput.write_characters(uinput, "L")
    assert uinput.mock_calls == [
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_LEFTSHIFT"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_L"], 1),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_L"], 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.ecodes["KEY_LEFTSHIFT"], 0),
        unittest.mock.call.syn(),
    ]
