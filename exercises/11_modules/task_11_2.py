# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology
from pprint import pprint

def merge_two_dicts(x, y):
    '''
    Украденная в Интернетах функция по складыванию словарей
    '''
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def find_matched_element(searching_list, list_whete_we_are_look_for):
    '''
    Функция получает на вход 2 списка, ищет первое совпадение и возвращает его,
    если совпадений нет - возвращает False
    '''
    for i in searching_list:
        for j in list_whete_we_are_look_for:
            if i == j:
                return i
    return False

def create_network_map(filenames):
    filal_dict = {}
    '''
    Функция должна возвращать словарь, который описывает соединения между устройствами.
    '''
    with open(filenames, 'r') as f:
        for file in f:
            with open(file.rstrip(), 'r') as f:
                all_output_lines = f.read()
                current_dict = parse_cdp_neighbors(all_output_lines)
                filal_dict = merge_two_dicts(filal_dict, current_dict)

    duble_flug = True
    # Идея алгоритма:
    # беру список значений словаря и список ключей словаря на каждой итерации цикла while
    # прохожу по спискам на предмет совпадающих элементов (функция find_matched_element)
    #
    # Если совпадение найдено (функция find_matched_element вернула совпадение) - 
    # - удаляю значение по ключу
    #
    # На следующей итерации снова формируются списки ключей и значений (обновленного словаря)
    # и процесс повторяется, пока ф-я find_matched_element не выдаст отсутствие совпадений
    while duble_flug is True:
        value_list = list(filal_dict.values())
        key_list = list(filal_dict.keys())

        matching = find_matched_element(value_list, key_list)
        if matching:
            # удаление совпадающего элемента
            filal_dict.pop(matching)
        else:
            # выход из while
            duble_flug=False

    return filal_dict

if __name__ == '__main__':
    topology = create_network_map('sum_file.txt')
    print(topology)
    draw_topology(topology)