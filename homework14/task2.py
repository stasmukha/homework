def stop_words(words: list):
    
    def decorator(func):
        
        def wrapper(*args, **kwargs):
            check = func(*args)
            
            for stop_word in words:
                check = check.replace(stop_word, '*')
                
            return check
        
        return wrapper
    
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):

    return f"{name} drinks pepsi in his brand new BMW!"




assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
