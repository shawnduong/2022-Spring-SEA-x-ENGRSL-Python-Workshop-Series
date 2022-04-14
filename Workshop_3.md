## Workshop 3: Go Go Tello!

In this workshop, we will explore user input devices and write a program that interfaces a user input device with drone controls.

We're going to control a drone with a Dance Dance Revolution mat.

### Topics

- User input devices

### Python Reference Sheet

```python
# Conditionals look like this.
if condition:
	instructions

# Here are a few examples.

if x == "A":
	print("You entered the letter A.")

if x < 5 and x % 2 == 0:
	print("x is less than 5, and x is also an even number.")

# There are 3 kinds of loops:
# 1. while loops do something while a condition is true.
# 2. "for x in y" loops do something for every item x in a collection of items y.
# 3. "for x in range(N)" will do something N many times.

# Here are a few examples.

while True:
	print("This will loop forever!")
	print("Unless I break. Then it'll stop.")
	break

people = ["John", "Jane", "Jack", "Jill"]
for person in people:
	print("Hello", person)

for i in range(10):
	print("Hi!")

# You can get user input using the input() function.
# If you give the function an argument, it'll display
# the argument as a prompt.

# Here are a few examples.

userInput = input()
age = input("What is your age? ")
```

## Tello Reference Sheet

**Reminder: we're not using the easyTello library -- we are using Shawn's easyTello fork which contains some important bug fixes. This is already in the repository in `tello.py`.**

Remember to install OpenCV if you want to be able to use the drone's camera!

At some point, every programmer learns that reading code can be a valuable way to learn how to use something. In this case, try reading the `tello.py` code and seeing if you can use it to make your drone move the way you want it to: [tello.py](./tello.py)
