import imp
import random
from turtle import end_fill
import os

def run():
    ahorcado()

def ahorcado():
    words = get_words()
    answer = random.choice(words)
    answer_mask = ''
    for i in range(len(answer)):
        answer_mask = answer_mask + '_' + ' '
    print(answer)
    
    for i in range(0,7):
        os.system('cls')
        #print(get_image(i))
        print('\n')
        print('Descubre la palabra: ')
        print('\n')
        print(answer_mask)
        print('\n')
        letter = input('Ingrese una letra: ')
        if letter in answer:
            print(answer)

def get_words():
    words = []
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.replace('\n',''))
    return words

def get_image(errors):
    if errors == 0:
        image = ('''
                ---------
                |       |
                |       
                |
                |
                |
                ''')
    elif errors == 1:
        image = ('''
                ---------
                |       |
                |       O
                |
                |
                |
                ''')
    elif errors == 2:
        image = ('''
                ---------
                |       |
                |       O
                |       |
                |
                |
                ''')
    elif errors == 3:
        image = ('''
                ---------
                |       |
                |       O
                |      -|
                |
                |
                ''')
    elif errors == 4:
        image = ('''
                ---------
                |       |
                |       O
                |      -|-
                |
                |
                ''')
    elif errors == 5:
        image = ('''
                ---------
                |       |
                |       O
                |      -|-
                |      /
                |
                ''')
    elif errors == 6:
        image = ('''
                ---------
                |       |
                |       O
                |      -|-
                |      /|
                |   ¡AHORCADO!
                ''')

    return image



if __name__ == '__main__':
    run()