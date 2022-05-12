def run():
    write()

def write():
    names = ['Susana','Ana','Claudia']
    with open('./files/names.txt','a',encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


if __name__ == '__main__':
    run()