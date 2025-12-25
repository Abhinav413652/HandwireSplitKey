import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

# --------------------------------------------------------------------------gemini btw
# WIRELESS SPLIT SETUP
# This enables the two halves to talk over Bluetooth without a cable.
# The Left half connects to your iPad/PC. The Right half connects to the Left.
# --------------------------------------------------------------------------
split = Split(split_type=SplitType.BLE)
keyboard.modules.append(split)
keyboard.modules.append(Layers())

# --------------------------------------------------------------------------
# PIN CONFIGURATION
# (Matches the wiring logic for the case you are using)
# --------------------------------------------------------------------------
# Rows connect to these pins on the XIAO
keyboard.row_pins = (board.D1, board.D2, board.D9, board.D10)

# Columns connect to these pins on the XIAO
keyboard.col_pins = (board.D3, board.D4, board.D5, board.D6, board.D7, board.D8)

# Diode direction: Col2Row is standard for handwiring
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --------------------------------------------------------------------------
# KEYMAP (Standard QWERTY - 44 Keys)
# --------------------------------------------------------------------------
keyboard.keymap = [
    [
        # LEFT HAND (Rows 1-4)
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   
        KC.ESC,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   
                 KC.LGUI, KC.LALT, KC.LCTL, KC.MO(1),        

        # RIGHT HAND (Rows 1-4)
        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,     KC.BSPC,
        KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN,  KC.ENT,
        KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,  KC.QUOT,
        KC.SPC,  KC.MO(2), KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT
    ]
]

if __name__ == '__main__':
    keyboard.go()
