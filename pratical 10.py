# Q1. Indexing

text = input("Enter a string: ")
if text:
    print("First:", text[0])
    print("Last:", text[-1])
    print("Middle:", text[len(text) // 2])
else:
    print("String is empty")

# Q2. Slicing

text = input("Enter a string: ")
print("First 5:", text[:5])
print("Last 4:", text[-4:])
print("Index 2 to 7:", text[2:7])

# Q3. Step slicing

text = input("Enter a string: ")
print("Alternate characters:", text[::2])
print("Reverse:", text[::-1])

# Q4. String immutability

text = "Python"
try:
    text[0] = "J"
except TypeError as error:
    print("Strings cannot be changed by index:", error)
text = "J" + text[1:]
print("New string:", text)

# Q5. in and not in

text = input("Enter sentence: ")
word = input("Search word: ")
if word in text: print("Word found")
if word not in text: print("Word not found")

# Q6. find and index

text = "Python programming"
word = input("Search word: ")
print("find():", text.find(word))
try:
    print("index():", text.index(word))
except ValueError:
    print("index(): word not found")

# Q7. Count occurrences

text = input("Enter text: ")
character = input("Enter character/word to count: ")
print("Occurrences:", text.count(character))

# Q8. Case conversion

text = input("Enter sentence: ")
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())

# Q9. Strip, replace and f-string

text = input("Enter sentence with possible extra spaces: ").strip()
old = input("Word to replace: ")
new = input("Replacement word: ")
updated = text.replace(old, new)
print(f"Original cleaned text: {text}")
print(f"Updated text: {updated}")

# Q10. Split and join

sentence = input("Enter sentence: ")
words = sentence.split()
print("Words:", words)
print("Joined with hyphens:", "-".join(words))

# Q11. Palindrome checker

text = input("Enter word or phrase: ").lower().replace(" ", "")
if text == text[::-1]: print("Palindrome")
else: print("Not palindrome")

# Q12. Text analyzer

from collections import Counter
import re
text = input("Enter paragraph: ")
words = re.findall(r"\b\w+\b", text.lower())
print("Word count:", len(words))
print("Character count (including spaces):", len(text))
if words:
    print("Most frequent word:", Counter(words).most_common(1)[0][0])
else:
    print("No words found")

