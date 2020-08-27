# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif 'mode access' in line:
                dict_access.update({interface_name:1})

    result = (dict_access, dict_trunk)
    return result

print(get_int_vlan_map('config_sw2.txt'))