'''
Провести дослідження реалізації бінарного дерева пошуку для вирішення задач пошуку.
Дослідження провести на основі вирішення наступних задач при роботі зі словниким слів, який збережений у файлі.
Для досліджнь потрібно розробити модуль search_time_test.py який дозволить:

Визначити час пошуку 10000 випадкових слів у впорядкованому за абеткою словнику (пошук у списку слів).
Визначити час пошуку 10000 випадкових слів у словнику, який представлений у вигляді бінарного дерева пошуку.
Бінарне дерево пошуку будується на основі словника в якому слова не впорядковані за абеткою.
Визначити час пошуку 10000 випадкових слів у словнику, який представлений у вигляді збалансованого бінарного дерева пошуку.
'''
import time
import random
import string
from binary_search_tree import Binary_search_tree


def sortByAlphabet(inputStr):
    return inputStr[0]

def random_words():
    alp = list(string.ascii_lowercase)
    with open('example.txt', 'w') as f:
        for i in range(10000):
            lst = []
            for _ in range(5):
                a = random.choice(alp)
                lst.append(a)
            f.write(''.join(lst))
            f.write('\n')

def time_for_list_alp():
    main_lst = []
    for i in range(10000):
        lst = []
        for _ in range(5):
            a = random.choice(alp)
            lst.append(a)
        main_lst.append(''.join(lst))
    main_lst.sort(key=sortByAlphabet)
    a = random.choice(main_lst)
    start_time = time.time()
    main_lst.index(a)
    print("--- %s seconds ---" % (time.time() - start_time))


def time_for_list():
    main_lst = []
    for i in range(10000):
        lst = []
        for _ in range(5):
            a = random.choice(alp)
            lst.append(a)
        main_lst.append(''.join(lst))
    a = random.choice(main_lst)
    start_time = time.time()
    main_lst.index(a)
    print("--- %s seconds ---" % (time.time() - start_time))




def time_for_bst():
    tree = Binary_search_tree()
    lst = []
    with open('example.txt', 'r') as f:
        for line in f:
           for i in line.split():
               lst.append(i)
    for i in lst:
        tree.insert(i)
    a = random.choice(lst)
    start_time = time.time()
    tree.search(a)
    print("--- %s seconds ---" % (time.time() - start_time))

time_for_bst()






