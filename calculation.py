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
    outside = outside + 5
    return outside

square()
print(outside)
print(outside)

x = 2
y = 4
if x == 1:
    print(x)
else:
    var = (y)
    print(type(var))

print(++x)
print(y)

names = ["a", "b", "c"]
values = [1, 2, 3]
for x in zip(names, values):
    print(x[0])


def someFuction(param1, param2 = "hello"):
    if not param1:
        return
    return param1, param2,0


touple = someFuction(param2 ='Test', param1='data2')
print(type(someFuction(param2 ='Test', param1='data')))

print(touple[0:2] )
def student(firstname, lastname='Mark', standard='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')


# 1 keyword argument
student(firstname='John')

# 2 keyword arguments
student(firstname='John', standard='Seventh')

# 2 keyword arguments
student(lastname='Gates', firstname='John')