# Q1. Basic try-except

try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Division:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Q2. Catch different errors

try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Division:", a / b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Q3. try-except-else

try:
    a = float(input("Numerator: "))
    b = float(input("Denominator: "))
    result = a / b
except (ValueError, ZeroDivisionError) as error:
    print("Error:", error)
else:
    print("Result:", result)
    print("Calculation successful.")

# Q4. finally cleanup message

try:
    file = open("sample.txt", "r", encoding="utf-8")
    print(file.read())
except FileNotFoundError:
    print("File does not exist.")
finally:
    try:
        file.close()
        print("File closed.")
    except NameError:
        print("No file was opened to close.")

# Q5. Capture exception details

try:
    number = int(input("Enter an integer: "))
    print(100 / number)
except Exception as error:
    print("An error occurred:", error)

# Q6. Repeat until valid integer

while True:
    try:
        number = int(input("Enter an integer: "))
        print("Valid input:", number)
        break
    except ValueError:
        print("Invalid input. Try again.")

# Q7. User-friendly calculator

try:
    a = float(input("First number: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Second number: "))
    if op == "+": print(a + b)
    elif op == "-": print(a - b)
    elif op == "*": print(a * b)
    elif op == "/":
        if b == 0: print("Cannot divide by zero.")
        else: print(a / b)
    else: print("Please choose a valid operator.")
except ValueError:
    print("Please enter numbers correctly.")

# Q8. Raise exception for age

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Age requirement satisfied.")
except ValueError as error:
    print("Notice:", error)

# Q9. Custom marks exception

class InvalidMarksError(Exception):
    pass

try:
    marks = float(input("Enter marks (0-100): "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    print("Marks accepted:", marks)
except ValueError:
    print("Enter a numeric value.")
except InvalidMarksError as error:
    print(error)

# Q10. Bank withdrawal

balance = 5000
class InsufficientBalanceError(Exception):
    pass

try:
    amount = float(input("Withdrawal amount: ₹"))
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")
    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)
except (ValueError, InsufficientBalanceError) as error:
    print("Transaction failed:", error)

# Q11. Multiple except vs generic Exception

# Specific exceptions are clearer and allow different messages.
try:
    number = int(input("Enter integer: "))
    print(10 / number)
except ValueError:
    print("Input was not an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Generic Exception catches many unexpected errors but is less specific.
try:
    number = int(input("Enter integer: "))
    print(10 / number)
except Exception as error:
    print("Something went wrong:", error)

# Q12. Nested try-except

values = [10, 20, 30]
try:
    number = int(input("Enter divisor: "))
    try:
        print("First list value divided:", values[0] / number)
        index = int(input("Enter list index (0-2): "))
        print("Selected value:", values[index])
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except IndexError:
        print("Index is out of range.")
except ValueError:
    print("Please enter integers only.")

