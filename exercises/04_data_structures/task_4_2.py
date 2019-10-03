# -*- coding: utf-8 -*-

task = ('Задание 4.2'
'\n'
'Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX'
'\n'
'Ограничение: Все задания надо выполнять используя только пройденные темы.'
)

mac = 'AAAA:BBBB:CCCC'

print(task, '\n')
print(mac, '\n')

print(mac.replace(":", "."), '\n')