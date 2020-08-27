# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

import sys

filname = sys.argv[1]

with open(filname, 'r') as src:
    with open('config_sw1_cleared.txt', 'w') as dest:
        for line in src:
            match_flag = False
            for i in ignore:
                if i in line:
                    match_flag = True
                    break
            if not match_flag:
                dest.write(line)