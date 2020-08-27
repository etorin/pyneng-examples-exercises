# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
    '''
    Обрабатывает конфигурационный файл коммутатора
    и возвращает кортеж из двух словарей
    '''
    dict_access = {}

    dict_trunk = {}

    with open(config_filename, 'r') as lines:
        for line in lines:
            line = line.rstrip()
            if 'interface' in line:
                interface_name = line.split('interface ')[1]
            elif 'vlan' in line:
                vlans = line.split('vlan ')[1]
                if ',' in vlans:
                    vlans_list = vlans.split(',')
                    vlans_list = [int(str) for str in vlans_list]
                    dict_trunk.update({interface_name:vlans_list})
                else:
                    dict_access.update({interface_name:int(vlans)})

    result = (dict_access, dict_trunk)
    return result

print(get_int_vlan_map('config_sw1.txt'))