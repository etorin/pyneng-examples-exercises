# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


import sys

filname = sys.argv[1]

with open(filname, 'r') as f: 
    for line in f:
        match_flag = False
        for i in ignore:
            if i in line:
                match_flag = True
                break
        if not match_flag and not line.startswith('!'):
            print(line.rstrip()) 