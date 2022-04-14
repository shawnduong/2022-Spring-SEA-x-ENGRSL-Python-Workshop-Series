#!/usr/bin/env python3

DEV = "/dev/input/event19"
CHUNKSIZE = 24
CONTROLS = {
	0x01: "LEFT",
	0x02: "DOWN",
	0x03: "UP",
	0x04: "RIGHT",
	0x05: "TRIANGLE",
	0x06: "SQUARE",
	0x07: "CROSS",
	0x08: "CIRCLE",
	0x09: "SELECT",
	0x0A: "START",
	0xFF: "CENTER",
}
SIGNATURES = [
	bytearray([0x04, 0x00, 0x04]),
	bytearray([0x03, 0x00, 0x01]),
]

def main():

	while True:

		with open(DEV, "rb") as f:
			data = f.read(CHUNKSIZE)

		if data[0x10:0x13] in SIGNATURES:
			try:
				print("KEY PRESSED:", CONTROLS[data[0x14]])
			except:
				pass
		else:
			continue

if __name__ == "__main__":
	main()
