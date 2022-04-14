#!/usr/bin/env python3

DEV = "/dev/input/event19"

CONTROLS = {
	144: [
		"SELECT",
		"START",
		"CROSS",
		"CIRCLE",
		"SQUARE",
		"TRIANGLE",
		"UP",
		"RIGHT",
		"DOWN",
		"LEFT",
	],
	96: [
		"CENTER",
	]
}

def trial(n: int) -> None:

	for size in CONTROLS.keys():

		for control in CONTROLS[size]:

			print(f"PRESS {control}")

			with open(DEV, "rb") as f:
				sequence = f.read(size)

			print(f"READ {size} BYTES")

			with open(f"./samples/{control}_t{n}.hex", "wb") as f:
				f.write(sequence)

			print(f"WRITTEN TO ./samples/{control}_t{n}.hex")
			print()

def main():

	for i in range(10):
		trial(i)

if __name__ == "__main__":
	main()
