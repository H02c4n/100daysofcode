## Python Decorators

import time

def delay_decorator(fn):
    def wrapper():
        time.sleep(2)
        fn()
    return wrapper


@delay_decorator
def say_hi():
    print("Hello")


say_hi()


def say_bye():
    print("Bye")


say_bye()

decorated_func = delay_decorator(say_bye)

decorated_func()