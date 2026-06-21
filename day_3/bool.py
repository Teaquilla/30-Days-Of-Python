import math

age = 250
height = 200
complex_num = 1j
b = 0
h = 0
print("Enter base: ", input(b))
print("Enter height: ", input(h))
area = 0.5 * b * h
print("The area of the triangle is ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = 0
b = 0
c = 0
print("Enter side a: ", input(a))
print("Enter side b: ", input(b))
print("Enter side c: ", input(c))
perimeter = a + b + c
print("The perimeter of the triangle is ", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = 0
width = 0
print("Enter side length: ", input(length))
print("Enter side width: ", input(width))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = 0
pi = 3.14
print("Enter side r: ", input(r))
area = pi * r * r
c = 2 * pi * r
print("The area of the circle is ", area)
print("The circumference of the circle is ", c)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y = 2x - 2
m = 2
b = -2
# slope
slope = m
# x-intercept: set y = 0, solve 0 = 2x - 2
x_intercept = -b / m
# y-intercept: set x = 0, so y = b
y_intercept = b
print("Slope:", slope)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
# slope
m = (y2 - y1) / (x2 - x1)
# Euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Slope:", m)
print("Euclidean distance:", distance)

# Compare the slopes in tasks 8 and 9.
m1 = 2
m2 = (y2 - y1) / (x2 - x1)
print(m1 == m2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + 6 * x + 9
print("y =", y)
print("At x =", x, "y becomes", y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") < len("dragon"))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print(
    "I hope this course is not full of jargon. ",
    "jargon" in "I hope this course is not full of jargon. ",
)

# There is no 'on' in both dragon and python
print(
    "There is no on in both dragon and python. ",
    "on" not in "dragon" and "on" not in "python",
)

# Find the length of the text python and convert the value to float and convert it to string
py = len("python")
pyf = float(py)
pys = str(pyf)
print(py, pyf, pys)


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 8

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
num_int = int(2.7)
print(7 // 3 == num_int)

# Check if type of '10' is equal to type of 10
print(type("10") is type(10))

# Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = 0
rph = 0
print("Enter side hours: ", input(hours))
print("Enter side rph: ", input(rph))
print("Your weekly earning is ", hours * rph)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = 0
print("Enter number of years you have lived: ", input(years))
print("You have lived for ", years * 31536000, " second")

# Write a Python script that displays the following table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
