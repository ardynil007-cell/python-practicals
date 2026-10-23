# Q1. Create dictionary

student = {"name": "Asha", "age": 18, "marks": 88}
print(student)
print(type(student))

# Q2. Access dictionary values

student = {"name": "Asha", "age": 18, "marks": 88}
print(student["name"])
print(student["marks"])
# student["city"] raises KeyError because the key does not exist.

# Q3. get method

student = {"name": "Asha", "age": 18}
print(student.get("name"))
print(student.get("city", "Not available"))

# Q4. Add and update

student = {"name": "Asha", "age": 18}
student["city"] = "Mumbai"
student["age"] = 19
print(student)

# Q5. Remove elements

student = {"name": "Asha", "age": 18, "marks": 88}
student.pop("age", None)
del student["marks"]
print(student)

# Q6. Iterate dictionary

student = {"name": "Asha", "age": 18}
for key in student:
    print("Key:", key)
for value in student.values():
    print("Value:", value)
for key, value in student.items():
    print(key, "=", value)

# Q7. keys, values and items

student = {"name": "Asha", "age": 18}
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

# Q8. Character frequency

text = input("Enter text: ")
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)

# Q9. Nested dictionary

students = {
    "S1": {"name": "Asha", "marks": 90},
    "S2": {"name": "Ravi", "marks": 82}
}
print(students["S1"]["name"])
students["S2"]["marks"] = 85
print(students)

# Q10. Merge dictionaries

a = {"name": "Asha", "age": 18}
b = {"age": 19, "city": "Mumbai"}
a.update(b)
print(a)  # duplicate keys are overwritten by the second dictionary

# Q11. Sort dictionary

marks = {"Ravi": 75, "Asha": 92, "Mina": 84}
print("By key:", dict(sorted(marks.items())))
print("By value:", dict(sorted(marks.items(), key=lambda item: item[1])))

# Q12. Inventory system

inventory = {"pen": 20, "book": 10}
inventory["pencil"] = 15
inventory["pen"] -= 2
remove_product = "book"
inventory.pop(remove_product, None)
for product, quantity in inventory.items():
    print(product, ":", quantity)