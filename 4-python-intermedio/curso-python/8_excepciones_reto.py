try:
    num = int(input('Ingrese un entero: '))
    if num < 0:
        raise ValueError('Debes ingresar un entero')
    print(f'Ingresaste {str(num)}')
except ValueError as ve:
    print(ve)

