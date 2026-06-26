# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
from tkinter.constants import WORD

Thirty = "Thirty"
days = "Days"
of = "Of"
python = "Python"
space = " "
sstr = Thirty + space + days + space + of + space + python
print(sstr)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding = "Coding"
fors = "For"
all = "All"
sstr = coding + space + fors + space + all
print(sstr)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = sstr
# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

print(sstr.capitalize())
print(sstr.title())
print(sstr.swapcase())

# Cut(slice) out the first word of Coding For All string.
first = sstr[1:14]
print(first)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(sstr.find("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
print(sstr.replace("Coding", "Python"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(sstr.split(space))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
sosmed = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(sosmed.split(", "))

# What is the character at index 0 in the string Coding For All.
print(sstr[0])

# What is the last index of the string Coding For All.
print(sstr[len(sstr) - 1])

# What character is at index 10 in "Coding For All" string.
print(sstr[10])

name = "Python For Everyone"
acronym = "".join(word[0] for word in name.split())
print(acronym)

acronym = "".join(word[0] for word in sstr.split())
print(acronym)
