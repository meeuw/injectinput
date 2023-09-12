import injectinput.injectinput
import unittest.mock
import evdev.ecodes

def test_letters():
    ui = unittest.mock.MagicMock()
    injectinput.injectinput.write_string(ui, "letters")
    assert ui.mock_calls == [
        unittest.mock.call.write(1, evdev.ecodes.KEY_L, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_L, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.KEY_E, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_E, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.KEY_T, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_T, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.KEY_T, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_T, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.KEY_E, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_E, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.KEY_R, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_R, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.KEY_S, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_S, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.syn(),
    ]

def test_special_characters():
    ui = unittest.mock.MagicMock()
    injectinput.injectinput.write_string(ui, "\\rL[(")
    assert ui.mock_calls == [
        unittest.mock.call.write(1, evdev.ecodes.KEY_ENTER, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_ENTER, 0),
        unittest.mock.call.syn(),

        unittest.mock.call.write(1, evdev.ecodes.KEY_LEFTSHIFT, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_L, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_L, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.KEY_LEFTSHIFT, 0),

        unittest.mock.call.write(1, evdev.ecodes.KEY_LEFTBRACE, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_LEFTBRACE, 0),
        unittest.mock.call.syn(),

        unittest.mock.call.write(1, evdev.ecodes.KEY_LEFTSHIFT, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_9, 1),
        unittest.mock.call.write(1, evdev.ecodes.KEY_9, 0),
        unittest.mock.call.syn(),
        unittest.mock.call.write(1, evdev.ecodes.KEY_LEFTSHIFT, 0),

        unittest.mock.call.syn(),
    ]
