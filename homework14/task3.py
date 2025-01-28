def arg_rules(type_: type, max_length: int, contains: list):

    def decorator(func):
            
        def wrapper(*args, **kwargs):
            if max_length >= len(*args):
                
                if type_ == type(*args):
                    for word in contains:
                        if word in args[0]:
                            return func(*args, *kwargs)
                        
                        else:
                            print('There are no mandatary elements')
                            return False
                
                else:
                    print('Incorrect type')
                    return False

            else:
                print('Incorrect string length')
                return False
        
        return wrapper
    
    return decorator
    
    
    



@arg_rules(type_=str, max_length=15, contains=['05', '@'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"




assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'