# Day 2: 30 Days of python programming'

from fcntl import F_GETLEASE
from inspect import AGEN_RUNNING
from operator import sub

# Level 1
first_name = "Harana"
last_name = "Harda"
full_name = "Harana Harda"
country = "Indonesia"
city = "Surakarta"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = True
drink, food, day = "beras_kencur", "Gudeg", "Thursday"

# Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(drink))
print(type(food))
print(type(day))

print(len(first_name))

first_len = len(first_name)
last_len = len(last_name)
if first_len > last_len:
    print("Your first name is longer than your last name.")
elif first_len < last_len:
    print("Your last name is longer than your first name.")
else:
    print("Your first name and last name have the same length.")

    num_one = 5
    num_two = 4
    total = num_one + num_two  # add
    print(total)
    diff = num_two - num_one  # substract
    print(diff)
    product = num_two * num_one  # multiply
    print(product)
    division = num_one / num_two  # devide
    print(division)
    remainder = num_two % num_one  # modulus
    print(remainder)
    exp = num_one**num_two  # exponential
    print(exp)
    floor_division = num_one // num_two  # floor division
    print(floor_division)

    radius = 30
    pi = 3.14
    area_of_circle = pi * radius**2
    circum_of_circle = 2 * pi * radius
    print(area_of_circle)
    print(circum_of_circle)

    print("Input Radius: ")
    input(radius)
    print(area_of_circle)
    print(circum_of_circle)

    print("First Name: ")
    input(first_name)
    print("Last Name: ")
    input(last_name)
    print("Country: ")
    input(country)
    print("Age: ")
    input(age)
