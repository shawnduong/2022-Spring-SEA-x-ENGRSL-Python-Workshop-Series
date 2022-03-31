## Workshop 1: Hello Python!

In this workshop, you'll be learning the basics of programming and Python! This document is essentially a reference sheet for you, and will also contain the activities and descriptions.

### Important Topics

- The Big Picture Idea
- Logic
- Conditionals
- Loops
- Functions

### Activity: Logic

As a group, write out the steps you took to get to SE1 160 today.

### Activity: Conditionals

1. As a group, **think of an everyday example of a conditional and express it in pseudocode.**
   - Example: "If the temperature is greater than 90 degrees, then I'll take my jacket off."
```
if temperature > 90:
	I'll take my jacket off
```

2. As a group, **write and run your first real Python conditional: let X = 20. If X is an even number, then print out "X is even." Else, print out "X is odd."**
   - Your group should have a designated group leader. You may run the code on their device. You may also run the code on your own device if you have Python set up.

### Activity: Loops

1. As a group, **think of an everyday example of a "for x in y loop" and an everyday example of a "for x in range(N)" loop, and express them in pseudocode.**
   - Example: "For every item in my shopping list, I will search for that item and then buy it. For every year my friend has been alive, I will give them a birthday punch."
```python
for item in shoppingList:
	search for item
	buy item

for year in range(friendAge):
	birthday punch friend
```

2. As a group, **write and run your first real set of Python loops that print out all the even numbers from 0 to 10, but not including 10.** You're basically solving the same problem in 2 different ways.
   - For "for x in y" loops, you may find the following line of code useful: `numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

### Python Reference Sheet

```python
# Comments look like this. They start with a '#' sign.

# Conditionals look like this.
if condition:
	instructions

# Here are a few examples.

if x < 5:
	print("x is less than 5.")

if x < 5 and x % 2 == 0:
	print("x is less than 5, and x is also an even number.")

if passwordEntered == actualPassword:
	print("You entered the right password!")
	print("Hello user.")

# There are 3 kinds of loops:
# 1. while loops do something while a condition is true.
#    - We aren't going to worry about these for now.
# 2. "for x in y" loops do something for every item x in a collection of items y.
# 3. "for x in range(N)" will do something N many times.

# Here are a few examples.

people = ["John", "Jane", "Jack", "Jill"]
for person in people:
	print("Hello", person)

for i in range(10):
	print("Hi!")
```

## Tello Reference Sheet

**Note: we're not using the easyTello library -- we are using Shawn's easyTello fork which contains some important bug fixes. This is already in the repository in `tello.py`.**

We still need the OpenCV (Open Computer Vision) library in order to view out of the drone's camera. You can either do this through your IDE, or run the following command to install this library:

```sh
pip install opencv-python
```

This reference sheet only contains items relevant to workshop 1. You can check out the full documentation at: https://github.com/Virodroid/easyTello

Note that your Python file (ends in `.py`) must be in the same folder as `tello.py`!

```python
# Remember to import the libraries that you need.
# We'll talk more about libraries in the future.
import tello 

# This is how you make drone objects.
# We'll talk more about objects in the future.
drone = tello.Tello()

# This is how you turn the camera on and view the feed.
drone.streamon()

# This is how you turn the camera off and stop viewing the feed.
drone.streamoff()

# Get the drone off the ground.
drone.takeoff()

# Land the drone.
drone.land()

# In the following methods, n is an integer from [20, 500].

# Go forward n cm.
drone.forward(n)

# Go back n cm.
drone.back(n)
```

**Important note:** your program will try to finish as fast as possible. This means that it'll turn the camera on, *but then it immediately turns it off.* You might find this code useful:

```python
# Import the time library.
import time

# Sleep for 5 minutes. 5 minutes * 60 seconds/minute = 300 seconds.
time.sleep(300)
```
