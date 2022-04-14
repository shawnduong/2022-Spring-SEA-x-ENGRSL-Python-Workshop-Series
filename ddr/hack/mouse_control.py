#!/usr/bin/env python3

from pynput.mouse import Button, Controller

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
	mouse = Controller()

	while True:

		with open(DEV, "rb") as f:
			data = f.read(CHUNKSIZE)

		if data[0x10:0x13] not in SIGNATURES:
			continue

		if data[0x14] == CONTROLS["LEFT"]:
			mouse.move(-quantum, 0)

		elif data[0x14] == CONTROLS["DOWN"]:
			mouse.move(0, quantum)

		elif data[0x14] == CONTROLS["UP"]:
			mouse.move(0, -quantum)

		elif data[0x14] == CONTROLS["RIGHT"]:
			mouse.move(quantum, 0)

		elif data[0x14] == CONTROLS["CROSS"]:
			mouse.press(Button.left)
			mouse.release(Button.left)

		elif data[0x14] == CONTROLS["CIRCLE"]:
			mouse.press(Button.right)
			mouse.release(Button.right)

		elif data[0x14] == CONTROLS["TRIANGLE"]:
			quantum += 10

		elif data[0x14] == CONTROLS["SQUARE"]:
			quantum -= 10

		if quantum < 0:
			quantum = 0

if __name__ == "__main__":
	main()
