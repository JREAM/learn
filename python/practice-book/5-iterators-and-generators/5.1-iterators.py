x = iter([1,2,3])
x.next()  #1
x.next()   #2
x.next()  #3

# Lazy load
def gen_y(n):
    i = 0
    while i < n:
        yield i
        i += 1

gen_y(5)

