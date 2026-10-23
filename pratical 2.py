# Q1. Name and age

name = input("Enter name: ")
age = int(input("Enter age: "))
print("Name:", name, "Age:", age)
print(f"My name is {name} and I am {age} years old.")

# Q2. Arithmetic operations

a = float(input("First number: "))
b = float(input("Second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero.")

# Q3. Sum, average and expression

a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))
print("Sum:", a + b + c)
print("Average:", (a + b + c) / 3)
print("(a + b) * c / 2:", (a + b) * c / 2)

# Q4. Operator precedence

print(10 + 5 * 2)       # 20
print((10 + 5) * 2)     # 30
print(100 / 5 + 3 * 2)  # 26.0

# Q5. Salary breakdown

basic = float(input("Basic salary: "))
hra = basic * 0.20
da = basic * 0.10
net = basic + hra + da
print(f"HRA: ₹{hra:.2f}")
print(f"DA: ₹{da:.2f}")
print(f"Net salary: ₹{net:.2f}")

# Q6. Rectangle and circle

import math
length = float(input("Rectangle length: "))
width = float(input("Rectangle width: "))
radius = float(input("Circle radius: "))
print("Rectangle area:", length * width)
print("Rectangle perimeter:", 2 * (length + width))
print("Circle area:", math.pi * radius ** 2)
print("Circle circumference:", 2 * math.pi * radius)

# Q7. Unit conversion

km = float(input("Distance in km: "))
celsius = float(input("Temperature in Celsius: "))
rupees = float(input("Amount in rupees: "))
rate = 83.0  # example fixed rate; change if your worksheet specifies another rate
print("Metres:", km * 1000)
print("Fahrenheit:", celsius * 9 / 5 + 32)
print("Approx. dollars:", rupees / rate)

# Q8. Multiple inputs in one line

a, b, c = map(float, input("Enter three numbers separated by spaces: ").split())
print("Sum:", a + b + c)
print("Product:", a * b * c)

# Q9. Three-subject result

m1 = float(input("Subject 1 marks: "))
m2 = float(input("Subject 2 marks: "))
m3 = float(input("Subject 3 marks: "))
total = m1 + m2 + m3
percentage = total / 300 * 100
print("Total:", total, "/ 300")
print(f"Percentage: {percentage:.2f}%")
if percentage >= 90: grade = "A"
elif percentage >= 75: grade = "B"
elif percentage >= 50: grade = "C"
else: grade = "Fail"
print("Grade:", grade)

# Q10. Prevent common expression errors

try:
    a = float(input("Enter number: "))
    b = float(input("Enter divisor: "))
    print("Division:", a / b)
except ValueError:
    print("Please enter numeric values.")
except ZeroDivisionError:
    print("Division by zero is not allonwed.")

