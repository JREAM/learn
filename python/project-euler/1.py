# -*- coding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

multiples = [3, 5]

result = 0

for m in multiples:
    for i in range(1, 10):
        if i % m is 0:
            result += i

print result

result = 0

for m in multiples:
    for i in range(1, 1000):
        if i % m == 0:
            result += i

print result
