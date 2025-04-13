def check_password(func):

    def new_func(*args, **kwargs):
        if input('Введите пароль:') != 'qwe123!@#':
            print('В доступе отказано.')
            return None
        else:
            return func(*args, **kwargs)

    return new_func


calculator = check_password(lambda x, y: x + y)
print(calculator(1, 5))
