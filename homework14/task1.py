def logger(func):
    def wrapper(*args, **kwargs):
        print(f'A function {func.__name__} is called with arguments{args}')
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):

    return x + y

 

@logger
def square_all(*args):

    return [arg ** 2 for arg in args]

print(add(1, 4))