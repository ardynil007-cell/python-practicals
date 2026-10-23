# Q1. Variable creation and naming rules

name = "Rahul"
age = 18
marks = 85.5
city = "Mumbai"

print(name, age, marks, city)
# Valid names use letters, digits and underscores, but cannot start with a digit.
# Keywords such as class cannot be used as variable names.

# Q2. Dynamic typing

value = 10
print(value, type(value))
value = "Python"
print(value, type(value))
value = 10.5
print(value, type(value))

# Q3. Constants simulation

PI = 3.14159
GRAVITY = 9.8
MAX_USERS = 100

print(PI, GRAVITY, MAX_USERS)
# Uppercase names are a convention for constants; Python does not enforce them.

# Q4. Data type identification

integer_value = 10
float_value = 10.5
string_value = "Hello"
boolean_value = True

for value in [integer_value, float_value, string_value, boolean_value]:
    print(value, "->", type(value))

# Q5. Type conversion

age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
print("Age next year:", age + 1)
print("Marks after adding 5:", marks + 5)

# Q6. Implicit and explicit conversion

a = 10
b = 2.5
print(a + b)                 # int + float becomes float

text_number = "20"
print(a + int(text_number))  # explicit conversion from string to int

# Q7. Memory behaviour of variables

a = 100
b = a
print("a:", a, "id:", id(a))
print("b:", b, "id:", id(b))
a = 200
print("After changing a:", a, b)

# Q8. Swapping variables

a = 10
b = 20

# Method 1: third variable
temp = a
a = b
b = temp
print("Using temp:", a, b)

# Method 2: tuple unpacking
a, b = b, a
print("Using tuple unpacking:", a, b)

# Q9. Data type-based calculator

a = input("Enter first value: ")
b = input("Enter second value: ")

try:
    print("Numeric addition:", float(a) + float(b))
except ValueError:
    print("String concatenation:", a + b)

# Q10. Boolean logic

age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
adult = age >= 18
good_marks = marks > 50
print("Adult:", adult)
print("Marks above 50:", good_marks)
if adult and good_marks:
    print("Both conditions are true.")

# Q11. Temperature converter

celsius = float(input("Temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.1f} C = {fahrenheit:.1f} F")

