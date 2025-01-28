def search_variables(func):
    return func.__code__.co_nlocals

def test():
    a = 168767
    b = 36463

print(search_variables(test))