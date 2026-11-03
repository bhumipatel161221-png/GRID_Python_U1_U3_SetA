# 1. Print using sep and end
print("Python", "Fundamentals", "Test", sep="|", end="!\n")

# 2. Multiple assignment and escape characters
name, city, year = "Asha", "Surat", 2026
print("Name:\t", name, "\nCity:\t", city)

# 3. Print both types of quotes using variable
print("She said \"It's", year, "\"", sep="")

# 4. Swap values without temporary variable
a, b = 10, 20
a, b = b, a

print("a =", a)
print("b =", b)


# 1. Take input from the user
item = input("Enter item name: ")
price = float(input("Enter price: "))

raw_qty = input("Enter quantity: ")

print(type(raw_qty))

quantity = int(raw_qty)

print(type(quantity))


# 2. Calculate total using f-string
total = price * quantity

print(f"Total for {item}: {total:.2f}")


# 3. Show errors safely

try:
    int("25.5")
except ValueError:
    print("ValueError")

try:
    "25" + 5
except TypeError:
    print("TypeError")


# 4. Type conversion and floor division
print(int(float("25.5")), int(-9.9), -9.9 // 1)

# 1. List of type names
vals = [42, 3.5, 'Python', True, None]
print([type(v).__name__ for v in vals])

# 2. Dynamic typing
x = 10
x = 'ten'
print(type(x).__name__)

# 3. Floating-point comparison
print(0.1 + 0.2 == 0.3, round(0.1 + 0.2, 2))

# 4. Boolean comparison and addition
print(True == 1, True + True)

# 5. Boolean values of different objects
print([bool(v) for v in [0, '', None, [], 'False', 5]])

# 6. Check using isinstance
print(isinstance(25, (int, float)))