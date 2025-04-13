def ask_password(login: str, password: str, successful, failure):
    login = login.lower()
    password = password.lower()
    vowels = 'aeiouy'
    consonants = 'bcdfghjklmnpqrstvwxz'
    correct_vowels = len(list(filter(lambda x: x in vowels, password))) == 3
    correct_consonants = [i for i in password if i in consonants] == [i for i in login if i in consonants]
    if not correct_vowels and not correct_consonants:
        failure(login, 'Everything is wrong')
    elif not correct_vowels:
        failure(login, 'Wrong number of vowels')
    elif not correct_consonants:
        failure(login, 'Wrong consonants')
    else:
        successful(login)


def main(login, password):
    successful = lambda log: print(f"Привет, {log}!")
    failure = lambda log, err: print(f"Кто-то попытался притвориться пользователем {log}, "
                                     f"но допустил ошибку: {str.upper(err)}")
    ask_password(login, password, successful, failure)


main('anastasia', 'nsyatos')
main('eugen', 'aaanig')
