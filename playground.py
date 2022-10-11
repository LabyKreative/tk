def add(*args):
    print(args[5])
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 5, 6, 2, 7, 8, ))


def calculate(**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #       Print(key
    #       print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

