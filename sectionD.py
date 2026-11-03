# Starting list
items = ['Amit', 'Priya', 'Rahul', 'Sneha']

# 1. List methods
items.append("Vikram")
items.extend(['Neha', 'Karan'])
items.insert(1, "Zoya")
items.remove("Rahul")

# 2. Remove last item using pop()
last = items.pop()

# Change item at index 0
items[0] = "Aman"

# 3. Print list, last item and length
print(items)
print(last, len(items))

# 4. Difference between append() and extend()

list1 = ['a', 'b']
list1.append(['c', 'd'])

list2 = ['a', 'b']
list2.extend(['c', 'd'])

print(list1, len(list1))
print(list2, len(list2))

# 5. Show three errors safely

try:
    items[50]
except IndexError:
    print("IndexError")

try:
    items.remove("Nobody")
except ValueError:
    print("ValueError")

try:
    [].pop()
except IndexError:
    print("IndexError")

# Create a tuple
t = (10, 20, 20, 30, 40)

# 1. Indexing and slicing
print(t[0], t[-1], t[1:3])

# 2. Count and index methods
print(t.count(20), t.index(30))

# 3. Single value and single-item tuple
x = (5)
y = (5,)

print(type(x).__name__, type(y).__name__)

# 4. Show three errors safely

try:
    t[0] = "yellow"
except TypeError:
    print("TypeError")

try:
    t.append(99)
except AttributeError:
    print("AttributeError")

try:
    t.index(1000)
except ValueError:
    print("ValueError")

# 5. Modify list inside a tuple
data = ([1, 2, 3], 'hello')

data[0].append(4)
print(data)

# 6. Create a new tuple with first item replaced
new_t = ("yellow",) + t[1:]
print(new_t)    

