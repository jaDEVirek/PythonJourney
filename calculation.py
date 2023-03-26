
x = 1
def f():
    x = 2
    return x

print(x)
print(f())
print(x)

def fxy(f, x, y):
    return f(x) + f(y)

cube = lambda x: x ** 3
print(fxy(cube, 2, 3))

outside = 5

def square():
    global outside
    outside = outside +5
    return outside

print(outside)





