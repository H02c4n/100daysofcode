def add(*args):
    print(args[0])
    print(type(args))
    sum = 0
    for n in args:
        sum += n
    return sum



print(add(3,4,5,6,8,9))


def calculate(n, **kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seat = kw["seat"]

my_car = Car(make="nissan", model="GT_R", seat=4)

print(my_car.model)