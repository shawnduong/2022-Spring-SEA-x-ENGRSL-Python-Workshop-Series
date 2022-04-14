#!/usr/bin/env python3

from pynput.keyboard import Key, Controller

DEV = "/dev/input/event19"
CHUNKSIZE = 24
CONTROLS = {
	"LEFT"     : 0x01,
	"DOWN"     : 0x02,
	"UP"       : 0x03,
	"RIGHT"    : 0x04,
	"TRIANGLE" : 0x05,
	"SQUARE"   : 0x06,
	"CROSS"    : 0x07,
	"CIRCLE"   : 0x08,
	"SELECT"   : 0x09,
	"START"    : 0x0A,
	"CENTER"   : 0xFF,
}
SIGNATURES = [
	bytearray([0x04, 0x00, 0x04]),
	bytearray([0x03, 0x00, 0x01]),
]

def main():

	quantum = 10
	keyboard = Controller()

	while True:

		with open(DEV, "rb") as f:
			data = f.read(CHUNKSIZE)

		if data[0x10:0x13] not in SIGNATURES:
			continue

		if data[0x14] == CONTROLS["LEFT"]:
			keyboard.press(Key.left)
			keyboard.release(Key.left)

		elif data[0x14] == CONTROLS["DOWN"]:
			keyboard.press(Key.down)
			keyboard.release(Key.down)

		elif data[0x14] == CONTROLS["UP"]:
			keyboard.press(Key.up)
			keyboard.release(Key.up)

		elif data[0x14] == CONTROLS["RIGHT"]:
			keyboard.press(Key.right)
			keyboard.release(Key.right)

if __name__ == "__main__":
	main()
