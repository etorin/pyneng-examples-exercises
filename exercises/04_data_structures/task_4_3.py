# -*- coding: utf-8 -*-

task = ('Задание 4.3'
'\n'
'Получить из строки config список VLANов вида:'
'\n'
'''['1', '3', '10', '20', '30', '100']'''
'\n'
'Ограничение: Все задания надо выполнять используя только пройденные темы.'
'\n'
)

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

print(task)
print(config, '\n')

print(config.split()[4:][0].split(','))

print('\n')