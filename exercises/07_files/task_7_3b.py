# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlan_print=input("VLAN: ")

with open ('CAM_table.txt', 'r') as file:
    for line in file:
        if 'Gi0' in line:
            vlan, mac, src, port = line.split()
            if vlan == vlan_print:
                print('{:<5} {:<15} {:<5}'.format(vlan, mac, port))