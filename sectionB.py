# 1. Floor division and modulus
a, b = 17, 5
print(a // b, a % b, -a // b, -a % b)

# 2. Floor division rule
print((-a // b) * b + (-a % b) == -a)

# 3. Operator precedence
print(2 + 3 * 4 ** 2 // 5, 2 ** 3 ** 2, 7 // -2)

# 4. Type of division
print(type(10 / 2).__name__, type(10 // 2).__name__)

# 5. Shopping bill
price = 250
quantity = 3
tax_rate = 18

subtotal = price * quantity
tax = subtotal * tax_rate / 100
total = subtotal + tax

print(f"Subtotal: {subtotal}  Tax: {tax:.2f}  Total: {total:.2f}")

# 1. Chained comparison
age = 25
has_id = True
has_guardian = False

print(18 <= age <= 60)

# 2. Logical AND and OR
can_enter = (age >= 18 and has_id) or has_guardian
print(can_enter)

# 3. Logical operators
print("Hello" and "World", "" or "Guest", not 10)

# 4. Short-circuit evaluation
user = ""
print(user or "Guest")

# 5. Compound assignment operators
score = 10

score += 5
score *= 2
score //= 4
score **= 2

print(score)

