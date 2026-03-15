def repeat(n):
    def decorator(fn):
        def wrap(*args, **kwargs):
            for i in range(n):
                fn(*args, **kwargs)
        return wrap
    return decorator


@repeat(3)
def say_hi():
    print('hi')
say_hi()



def deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result*=2
        return result
    return wrapper

@deco
def summa(*args):
    total=0
    for i in args:
        total+=i
    return total

print(summa(2,3))


is_admin=True

def admin_req(func):
    def wrap(*args, **kwargs):
        global is_admin
        if is_admin:
            print('Hello world')
            return func(*args, **kwargs)
        else:
            print("Доступ запрещен")
            return None
    return wrap

@admin_req
def say_hi():
    print('hi')
say_hi()


def decor(func):
    def wrap(*args, **kwargs):
        print('Начало')
        result=func(*args, **kwargs)
        print('Конец')
        return result
    return wrap

@decor
def say_hellooo():
    print('привет!')

say_hellooo()
