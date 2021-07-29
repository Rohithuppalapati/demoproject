def new_decorator(func):
    def wrapper(*args,**kwargs):
        print('*********')
        func(*args,**kwargs)
        print('*********')
    return wrapper

@new_decorator
def welcome(greeting='hello welcome to', course='python'):
    print(greeting,course)

welcome()
