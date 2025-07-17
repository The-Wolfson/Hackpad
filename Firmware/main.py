import board

#Rotary 1 A - GP1
#Rotary 1 B - GP2
#Rotary 2 A - GP4
#Rotary 2 B - GP3

#Led Strip - GP0
#Column 1 = GP26
#Column 2 = GP27
#Column 3 = GP28
#Row 1 = GP29
#Row 2 = GP6
#Row 3 = GP7

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.midi import MidiKeys, MIDI_CC
from kmk.modules.keypad import MatrixScanner
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

midi_keys = MidiKeys()
keyboard.modules.append(midi_keys)

rgb = RGB(pixel_pin=board.GP0, num_pixels=16)
keyboard.extensions.append(rgb)

keyboard.matrix = MatrixScanner(
    cols=(board.GP26, board.GP27, board.GP28),
    rows=(board.GP29, board.GP6, board.GP7)
)

encoder_handler.pins = (
    (board.GP1, board.GP2),
    (board.GP4, board.GP3),
)

encoder_handler.map = [
    ((MIDI_CC, 0x1A, 1), (MIDI_CC, 0x1A, 127)),
    ((MIDI_CC, 0x2A, 1), (MIDI_CC, 0x2A, 127)),
]

keyboard.keymap = [
    [
        KC.MIDI_CC(0x3A),
        KC.MIDI_CC(0x3B),
        KC.MIDI_CC(0x3C),
        KC.MIDI_CC(0x4A),
        KC.MIDI_CC(0x4B),
        KC.MIDI_CC(0x4C),
        KC.MIDI_CC(0x5A),
        KC.MIDI_CC(0x5B),
        KC.MIDI_CC(0x5C),
    ]
]


if __name__ == '__main__':
    keyboard.go()
