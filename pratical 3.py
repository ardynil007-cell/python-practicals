# Q1. Positive number

n = float(input("Enter a number: "))
if n > 0:
    print("Positive number")

# Q2. Even or odd

n = int(input("Enter an integer: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3. Grade using elif

marks = float(input("Enter marks: "))
if marks >= 90: print("Grade A")
elif marks >= 75: print("Grade B")
elif marks >= 50: print("Grade C")
else: print("Fail")

# Q4. Voting eligibility

age = int(input("Enter age: "))
nationality = input("Enter nationality: ").strip().lower()
if age >= 18:
    if nationality == "indian":
        print("Eligible to vote, subject to voter registration.")
    else:
        print("Nationality condition not met.")
else:
    print("Not eligible by age.")

# Q5. Largest of three

a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))
if a >= b and a >= c: print("Largest:", a)
elif b >= a and b >= c: print("Largest:", b)
else: print("Largest:", c)

# Q6. Leap year

year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

# Q7. Simple calculator

a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))
if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/":
    if b != 0: print(a / b)
    else: print("Cannot divide by zero")
else: print("Invalid operator")

# Q8. Discount calculator

amount = float(input("Purchase amount: ₹"))
if amount >= 2000: discount_rate = 0.20
elif amount >= 1000: discount_rate = 0.10
else: discount_rate = 0
discount = amount * discount_rate
print("Discount:", discount)
print("Final amount:", amount - discount)

# Q9. Triangle type

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b == c: print("Equilateral")
elif a == b or a == c or b == c: print("Isosceles")
else: print("Scalene")

# Q10. Menu-driven program

print("1. Add\n2. Subtract\n3. Multiply")
choice = input("Choose 1, 2 or 3: ")
a = float(input("First number: "))
b = float(input("Second number: "))
if choice == "1": print("Result:", a + b)
elif choice == "2": print("Result:", a - b)
elif choice == "3": print("Result:", a * b)
else: print("Invalid choice")

