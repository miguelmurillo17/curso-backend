def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('No debe ser cadena vacia')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindrome(''))
except TypeError:
    print('Solo puede ingresar strings')
finally:
    pass
    # cerrar archivo
    # cerrar conexion a BD
    # liberar recursos externos
