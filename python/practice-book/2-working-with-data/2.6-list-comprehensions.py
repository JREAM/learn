a = range(5)  # [0, 1, 2, 3, 4]
[x+1 for x in a]  # [1, 2, 3, 4]

[x for x in a if x % 2 == 0]  # [0, 2, 4]
[x*2 for x in a if x % 2 == 0]  # [0, 2, 6, 16]  just guessin, its late

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
zip(a, b)  # [(1,3), (2,4), (3,5), (4,6)]
[x+y for x, y in zip(a, b)]  # [4, 6, 8, 10]

# tired
