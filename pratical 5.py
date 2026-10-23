# Q1. break

for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Q2. continue

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

# Q3. Compare break and continue

print("break:")
for i in range(1, 8):
    if i == 5: break
    print(i)
print("continue:")
for i in range(1, 8):
    if i == 5: continue
    print(i)

# Q4. Search in list

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Number to search: "))
for index, value in enumerate(numbers):
    if value == target:
        print("Found at position:", index + 1)
        break
else:
    print("Not found")

# Q5. First number divisible by n

n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Enter a positive integer.")
else:
    for i in range(1, 101):
        if i % n == 0:
            print("First multiple:", i)
            break

# Q6. Skip negative numbers

numbers = list(map(int, input("Enter numbers: ").split()))
for n in numbers:
    if n < 0: continue
    print(n)

# Q7. Sum valid inputs

total = 0
while True:
    n = float(input("Enter number (0 to stop): "))
    if n == 0: break
    if n < 0: continue
    total += n
print("Sum of non-negative inputs:", total)

# Q8. Password retry system

correct_password = "python123"
for attempt in range(3):
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful")
        break
else:
    print("Failed after 3 attempts")

# Q9. pass statement

for i in range(5):
    pass  # placeholder; no action is performed
print("Loop finished")

# Q10. Skip even numbers in pattern

for row in range(1, 5):
    for number in range(1, row + 1):
        if number % 2 == 0:
            continue
        print(number, end=" ")
    print()

