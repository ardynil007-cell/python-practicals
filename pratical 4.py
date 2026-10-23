# Q1. For loop and even numbers

for i in range(1, 11):
    print(i)
print("Even numbers:")
for i in range(2, 11, 2):
    print(i)

# Q2. While loop

i = 1
while i <= 10:
    print(i)
    i += 1

# Q3. Sum and average of n numbers

n = int(input("How many numbers? "))
total = 0
for i in range(n):
    total += float(input(f"Number {i + 1}: "))
if n > 0:
    print("Sum:", total)
    print("Average:", total / n)
else:
    print("Enter at least one number.")

# Q4. Factorial using for and while

n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, n + 1): fact *= i
    print("For-loop factorial:", fact)
    fact2, i = 1, 1
    while i <= n:
        fact2 *= i
        i += 1
    print("While-loop factorial:", fact2)

# Q5. Multiplication table

n = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Q6. Reverse number and palindrome

n = input("Enter a non-negative integer: ")
reverse = n[::-1]
print("Reverse:", reverse)
print("Palindrome" if n == reverse else "Not palindrome")

# Q7. Count digits, even and odd digits

n = input("Enter an integer: ").lstrip("-")
even = odd = 0
for ch in n:
    if ch.isdigit():
        if int(ch) % 2 == 0: even += 1
        else: odd += 1
print("Total digits:", sum(ch.isdigit() for ch in n))
print("Even digits:", even)
print("Odd digits:", odd)

# Q8. Prime checker

n = int(input("Enter integer: "))
is_prime = n >= 2
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not prime")

# Q9. Fibonacci series

terms = int(input("Number of terms: "))
a, b = 0, 1
for _ in range(max(0, terms)):
    print(a, end=" ")
    a, b = b, a + b
print()

# Q10. Nested-loop patterns

for i in range(1, 5):
    print("*" * i)
print("Reverse:")
for i in range(4, 0, -1):
    print("*" * i)
print("Number pattern:")
for i in range(1, 5):
    print(*range(1, i + 1))