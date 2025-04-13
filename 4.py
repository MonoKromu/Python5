def russian_alfabet():
    for i in range(ord('а'), ord('я')+1):
        yield chr(i)


print(list(russian_alfabet()))
