# def uppercase_decorator(function):
#     print('Was called')
#     func = function()
#     make_uppercase = func.upper()
#     return make_uppercase
#
#
# @uppercase_decorator
# def say_hi():
#     print('done')
#     return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        result = function()
        print('done')
        make_uppercase = result.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    print('done')
    return 'hello there'

# print(say_hi())

def myfunc(n):
  return lambda a : a * n

print(myfunc(5)(2))