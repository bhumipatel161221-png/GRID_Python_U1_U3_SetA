# 1. Create a set from a list
nums = [4, 7, 4, 9, 7, 7, 2, 9]

s = set(nums)

print(sorted(s), len(nums), len(s))

# 2. Set methods
s.add(11)
s.discard(99)
s.remove(2)

print(sorted(s))

# 3. Show KeyError safely
try:
    s.remove(1000)
except KeyError:
    print("KeyError")

# 4. Set operations
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

print(sorted(s1 | s2), sorted(s1 & s2))

print(sorted(s1 - s2), sorted(s2 - s1),
      sorted(s1 ^ s2))

# 5. Type names
print(type({}).__name__, type(set()).__name__)

# 6. Membership operators
print(9 in s, 9 not in s1)

# 7. Try to create a set containing lists
try:
    {[1, 2], [3, 4]}
except TypeError:
    print("TypeError")

# Create dictionary
d = {
    'name': 'Rahul',
    'age': 20,
    'course': 'Python',
    'marks': [80, 85, 90],
    'address': {'city': 'Ahmedabad', 'country': 'India'}
}

# 1. Access dictionary values
print(d["name"], d.get("phone"), d.get("phone", "Not found"))

# 2. Update age and add grade
d["age"] = 21
d["grade"] = "A"

print(d["age"], len(d))

# 3. Remove items using pop() and del
removed = d.pop("course")

print(removed, d.pop("zzz", "none"))

del d["marks"]

print(list(d.keys()))

# 4. Access nested dictionary
print(d["address"]["city"])

# 5. Membership operators
print("name" in d, 'Rahul' in d, 'Rahul' in d.values())

# 6. Loop through dictionary items
for key, value in d.items():
    print(key, "->", value)

# 7. Handle KeyError
try:
    print(d["email"])
except KeyError:
    print("KeyError")

# 8. Duplicate keys
dup = {"name": "first", "x": 1, "name": "second"}

print(dup)    