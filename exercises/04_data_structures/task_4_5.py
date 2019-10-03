# -*- coding: utf-8 -*-
task = ('Задание 4.5'
'\n\n'
'Из строк command1 и command2 получить список VLANов,\n'
'которые есть и в команде command1 и в команде command2.'
'\n\n'
'''Результатом должен быть список: ['1', '3', '8']\n'''
'\n\n'
'Ограничение: Все задания надо выполнять используя только пройденные темы.\n'
''
)

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

print(task)
print("{}\n{}\n".format(command1, command2))

vlans1 = set(command1.split()[4:][0].split(','))
vlans2 = set(command2.split()[4:][0].split(','))

vlans = list(vlans1.intersection(vlans2))

vlans.sort()

print(vlans)