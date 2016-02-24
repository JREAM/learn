simple = [1, 2, 3]
nested = [1, 2, [3, 4], 5]
auto = range(5)      # [0, 1, 2, 3, 4]
auto2 = range(3, 6)  # [3, 4, 5]
auto2 = range(2, 10, 3)  # [2, 5, 8] (every 3 digitals between 2 and 10)
len(simple)  # 3

a = [1, 2]
b = [3, 4]
print a + b  # [1,2,3,4]

print a * 2  # [1,2,1,2]


simple[0]   # 1
simple[-1]  # 3

simple[1:3]  # [2,3]
simple[0:-1]  # [1,2] (Dice off last item)

simple[:2]  # [1,2]
simple[2:]  # [3]
simple[:]  # [1,2,3]

zoo = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zoo[0:6:2]  # from 0 to 5 inc of 2 [0, 2, 4]

zoo[::-1]  # Reverse [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

2 in zoo  # true
500 in zoo # false

a = [1, 2]
a.append(3)  # [1,2,3]


# Solve
x = [0, 1, [2]]
x[2][0] = 3
print x   # [0, 1, [3]]
x[2].append(4)
print x  # [0, 1, [3, 4]]
x[2] = 2
print x  # [0, 1, 2]


for x in [1,2,3]:
    print x

zip(["cat", "dog", "fish"], [1, 2, 3]) #  [('cat', 1), ('dog', 2), ('fish', 3)]

names = ["sack", "fab", "boy"]
ages = [21, 22, 23]
for name, age in zip(names, ages):
    print name, age

sum([1,2,3])  # 6

# Stopping here this is boring
