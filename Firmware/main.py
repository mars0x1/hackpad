import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode

keyboard = KMKKeyboard()

# --- 1. THE MATRIX CONFIGURATION ---
# Based on your XIAO pins
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.col_pins = (board.D6, board.D7, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- 2. THE ENCODER ROTATION (D10, D8) ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D11, board.D10, None, False),)
encoder_handler.map = [((KC.VOLU, KC.VOLD),)] # Volume wheel

# --- 3. THE OLED DISPLAY ---
oled_ext = Oled(
    OledDisplayMode.TXT,
    oob_config={'scl': board.D5, 'sda': board.D4},
)
keyboard.extensions.append(oled_ext)

# --- 4. THE KEYMAP ---
# Row 1, Col 3 is your Encoder Click (Master Audio Mute)
# One of your other keys is now FN+F5 (Mic Mute)
keyboard.keymap = [
    [
        # ROW 1: Undo, Cut, SYSTEM AUDIO MUTE (Encoder Click)
        KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.MUTE, 
        
        # ROW 2: Copy, Paste, MIC MUTE (FN + F5)
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.HYPR(KC.F5), 
        
        # ROW 3: Save, Play/Pause, Next Track
        KC.LCTL(KC.S), KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
        
        # ROW 4: Alt+Tab, Desktop, Enter
        KC.LALT(KC.TAB), KC.LWIN(KC.D), KC.ENTER
    ]
]

if __name__ == '__main__':
    keyboard.go()