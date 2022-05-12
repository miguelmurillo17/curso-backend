from re import S


def palindrome(string):
    assert len(string) > 0, 'No puede estar vacio'
    assert string.isnumeric(), 'Debes ingresar un numero'
    return string == string[::-1]


try:
    print(palindrome('a'))
except AssertionError as e:
    print(e)
