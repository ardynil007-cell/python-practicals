# Q1. Write to text file

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.write("File handling practical\n")
print("File written successfully")

# Q2. Read entire file

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Q3. Read line by line

with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
        
# Q4. Use with statement

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("First line\nSecond line\n")
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
# The with statement closes the file automatically.

# Q5. Append data

with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Appended line\n")
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Q6. Count lines, words and characters

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))
print("Characters:", len(content))

# Q7. Search word in file

word = input("Word to search: ")
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Occurrences:", content.count(word))

# Q8. Copy file

with open("sample.txt", "r", encoding="utf-8") as source:
    content = source.read()
with open("copy.txt", "w", encoding="utf-8") as destination:
    destination.write(content)
print("Copied to copy.txt")

# Q9. Filter lines by keyword

keyword = input("Keyword: ").lower()
with open("sample.txt", "r", encoding="utf-8") as source:
    lines = source.readlines()
with open("filtered.txt", "w", encoding="utf-8") as destination:
    for line in lines:
        if keyword in line.lower():
            destination.write(line)
print("Matching lines saved to filtered.txt")

# Q10. Student record file

with open("students.txt", "a", encoding="utf-8") as file:
    name = input("Student name: ")
    roll = input("Roll number: ")
    marks = input("Marks: ")
    file.write(f"{roll},{name},{marks}\n")
with open("students.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Q11. Handle missing file

try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Check the filename and location.")

# Q12. Replace word in file

old_word = input("Word to replace: ")
new_word = input("New word: ")
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
content = content.replace(old_word, new_word)
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write(content)
print("File updated")