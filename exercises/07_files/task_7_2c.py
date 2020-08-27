# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

import sys

src_filname = sys.argv[1]
dst_filname = sys.argv[2]

with open(src_filname, 'r') as src:
    with open(dst_filname, 'w') as dest:
        for line in src:
            match_flag = False
            for i in ignore:
                if i in line:
                    match_flag = True
                    break
            if not match_flag:
                dest.write(line)