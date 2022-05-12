def divisors(num):
    divisors = [i for i in range(1, num+1) if num%i == 0]
    #print(divisors)
    return(divisors)


def run():
    num = int(input('Ingresa un numero: '))
    print(divisors(num))
    print('Fin de mi programa')

if __name__ == '__main__':
    run()