def check_password(password):
    def decorator(func):

        def new_func(*args, **kwargs):
            if input('Введите пароль:') != password:
                print('В доступе отказано.')
                return None
            else:
                return func(*args, **kwargs)

        return new_func

    return decorator


@check_password('superstrongpassword')
def summa(a, b):
    return a + b


print(summa(1, 2))
