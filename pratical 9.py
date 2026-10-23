# Q1. Define and call function

def greet():
    print("Welcome to Python!")
greet()
greet()

# Q2. Function with parameters

def add(a, b):
    return a + b
print("Sum:", add(10, 20))

# Q3. Return value

def square(n):
    return n * n
result = square(5)
print("Square:", result)

# Q4. Default and keyword arguments

def introduce(name, city="Mumbai"):
    print(f"{name} lives in {city}")
introduce("Asha")
introduce(name="Ravi", city="Pune")

# Q5. Built-in functions

numbers = [4, 8, 2, 9, 5]
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("String length:", len("Python"))

# Q6. List processing function

def process_list(values):
    return sum(values), max(values)
numbers = [4, 8, 2, 9, 5]
total, largest = process_list(numbers)
print("Sum:", total)
print("Largest:", largest)

# Q7. Recursive factorial

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter non-negative integer: "))
if n < 0: print("Invalid input")
else: print("Factorial:", factorial(n))

# Q8. Recursive Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
terms = int(input("Number of terms: "))
for i in range(max(0, terms)):
    print(fibonacci(i), end=" ")
print()

# Q9. Function calling another function

def get_number():
    return float(input("Enter a number: "))
def double(n):
    return n * 2
def display(result):
    print("Result:", result)
display(double(get_number()))

# Q10. Local and global scope

count = 10
def update_count():
    global count
    count += 1
update_count()
print("Global count:", count)

# Q11. Menu-driven functions

import math
def add(a, b): return a + b
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
def factorial(n):
    return math.factorial(n)
choice = input("1 Add, 2 Prime check, 3 Factorial: ")
if choice == "1":
    print(add(float(input("a: ")), float(input("b: "))))
elif choice == "2":
    print(is_prime(int(input("n: "))))
elif choice == "3":
    n = int(input("n: "))
    print(factorial(n) if n >= 0 else "Enter non-negative n")
else:
    print("Invalid choice")

# Q12. Student result system

def get_marks():
    return [float(input(f"Marks for subject {i + 1}: ")) for i in range(3)]
def calculate(marks):
    total = sum(marks)
    return total, total / 300 * 100
def grade(percent):
    if percent >= 90: return "A"
    if percent >= 75: return "B"
    if percent >= 50: return "C"
    return "Fail"
marks = get_marks()
total, percent = calculate(marks)
print("Total:", total, "/ 300")
print(f"Percentage: {percent:.2f}%")
print("Grade:", grade(percent))