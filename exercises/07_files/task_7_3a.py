# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

list_of_list = []

with open('CAM_table.txt', 'r') as file:
    for line in file:
        if 'Gi0' in line:
            vlan, mac, src, port = line.split()
            list_of_line = [vlan, mac, port]
            list_of_list.append(list_of_line)

list_length = len(list_of_list)
i = 0

while i < list_length - 1:
    j = 0
    while j < list_length - 1 - i:
        if int(list_of_list[j][0]) > int(list_of_list[j+1][0]):
            list_of_list[j][0], list_of_list[j+1][0] = list_of_list[j+1][0], list_of_list[j][0]

        j += 1
    i += 1

for line in list_of_list:
    print('{:<5} {:<15} {:<5}'.format(line[0], line[1], line[2]))
