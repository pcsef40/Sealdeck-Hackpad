import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
keyboard = KMKKeyboard()
keyboard.matrix = KeysScanner(
    pins=[
        board.D0,
        board.D1,
        board.D2,
        board.D3,
    ],
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
    ]
]
i2c = busio.I2C(
    board.D5,  # SCL
    board.D4,  # SDA
)

oled_driver = SSD1306(
    i2c=i2c,
    device_address=0x3C,
)

display = Display(
    display=oled_driver,
    width=128,
    height=32,
    entries=[
        TextEntry(
            text="HACKPAD",
            x=0,
            y=0,
        ),
        TextEntry(
            text="4 KEY MACROPAD",
            x=0,
            y=14,
        ),
    ],
)

keyboard.extensions.append(display)
if __name__ == "__main__":
    keyboard.go()