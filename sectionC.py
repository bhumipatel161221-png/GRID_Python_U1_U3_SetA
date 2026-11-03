# Create a string
word = "Fundamentals"

# 1. First character, last character and length
print(word[0], word[-1], len(word))

# 2. String slicing
print(word[:3], word[3:], word[::-1], word[::2])

# 3. Try changing a character (TypeError)
try:
    word[0] = "X"
except TypeError:
    print("TypeError")

# Try accessing an invalid index (IndexError)
try:
    print(word[50])
except IndexError:
    print("IndexError")

# 4. Build a new string
new_word = "X" + word[1:]
print(new_word)

# Given messy text
raw = " pRiYa deSai , Surat , priya@mail.com "

# 1. Remove outer spaces and split the text
clean = raw.strip()

parts = [part.strip() for part in clean.split(",")]

print(parts)

# 2. Unpack parts into variables
name, city, email = parts

print(name.title(), city.upper(), email.lower(), sep="|")

# 3. Check email conditions
print(email.endswith(".com"), email.startswith("priya"),
      email.find("@"), email.find("#"))

# 4. Find invalid character using index()
try:
    email.index("#")
except ValueError:
    print("ValueError")

# 5. Replace every 'a' with '@'
print(city.replace("a", "@"))

# 6. Check lstrip() and rstrip()
print(raw.lstrip() == clean, raw.rstrip() == clean)

# Given values
customer = "Rahul"
item = "Laptop bag"
price = 1450
qty = 2
disc = 0.125

total = price * qty * (1 - disc)

# 1. Receipt using triple-quoted f-string
print(f"""
----- SHOPPING RECEIPT -----
Customer: {customer}
Item: {item}
Price: {price}
Quantity: {qty}
Discount: {disc:.1%}
Total: {total:.2f}
----------------------------
""")

# 2. Using format() with empty placeholders
print("{} bought {} item(s)".format(customer, qty))

# 3. Using format() with named placeholders
print("{name} paid {amount:.1f}".format(name=customer, amount=total))

# 4. Using old % formatting style
print("%s bought %d item(s) for %.2f" % (customer, qty, total))