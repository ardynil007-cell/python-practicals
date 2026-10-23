# Q1. Create list and tuple

numbers = [10, 20, 30, 40, 50]
names = ("Asha", "Ravi", "Mina")
print(numbers, type(numbers))
print(names, type(names))

# Q2. Indexing

numbers = [10, 20, 30, 40, 50]
print("First:", numbers[0])
print("Last:", numbers[-1])
print("Middle:", numbers[len(numbers) // 2])

# Q3. Slicing

values = [10, 20, 30, 40, 50, 60]
print("First 3:", values[:3])
print("Last 2:", values[-2:])
print("Alternate:", values[::2])

# Q4. Mutability

items = [1, 2, 3]
items[0] = 100
print("Changed list:", items)
fixed = (1, 2, 3)
# fixed[0] = 100 would raise TypeError because tuples are immutable.
print("Tuple:", fixed)

# Q5. append and insert

items = [10, 20, 30]
items.append(40)
items.insert(1, 15)
print(items)

# Q6. remove and pop

items = [10, 20, 30, 20]
items.remove(20)
last = items.pop()
print("List:", items)
print("Popped:", last)

# Q7. sort and reverse

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)
numbers.reverse()
print("Reversed:", numbers)

# Q8. Tuple count and index

values = (10, 20, 10, 30, 10)
print("Count of 10:", values.count(10))
print("Index of 20:", values.index(20))

# Q9. Nested list

matrix = [[1, 2], [3, 4]]
print("Element:", matrix[1][0])
matrix[1][0] = 99
print(matrix)

# Q10. Convert list and tuple

items = [1, 2, 3]
t = tuple(items)
print(t)
back_to_list = list(t)
back_to_list.append(4)
print(back_to_list)

# Q11. Iterate and sum

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
print("Sum:", sum(numbers))
words = ("red", "blue", "green")
for word in words:
    print(word)

# Q12. Shopping cart

cart = ["bread", "milk", "eggs"]
categories = ("food", "drinks", "home")
cart.append(input("Add product: "))
remove_item = input("Product to remove: ")
if remove_item in cart:
    cart.remove(remove_item)
print("Cart:", cart)
print("Fixed categories:", categories)

