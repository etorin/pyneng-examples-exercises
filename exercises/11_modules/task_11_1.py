# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). 
Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(command_output):
    '''
    Функция ожидает как аргумент вывод команды одной строкой (не имя файла).
    Функция должна возвращать словарь, который описывает соединения между устройствами.
    '''
    result_dict = {}
    list_of_lines = command_output.split('\n')
#    print('RRRRRR: {}'.format(list_of_lines))
    list_of_lines = [ n.rstrip() for n in list_of_lines if 'Eth' in n or 'neighbors' in n]
#    print('RRRRRR: {}'.format(list_of_lines))
    hostname = list_of_lines[0].split('>')[0]
    del list_of_lines[0]
    for line in list_of_lines:
        output_list = line.split()
        dev_id, local_int_name, local_int_id = output_list[0:3]
        port_name, portid = output_list[-2:]
        #dev_id, local_int_name, local_int_id, _, _, _, _, _, port_name, portid = line.split()
        result_dict[(str(hostname),str(local_int_name)+str(local_int_id))] = (str(dev_id),str(port_name)+str(portid))

    return result_dict

if __name__ == '__main__':
    
    with open('sh_cdp_n_r1.txt', 'r') as f:
        all_output_lines = f.read()

    print(parse_cdp_neighbors(all_output_lines))

    with open('sh_cdp_n_r2.txt', 'r') as f:
        all_output_lines = f.read()

    print(parse_cdp_neighbors(all_output_lines))

    with open('sh_cdp_n_r3.txt', 'r') as f:
        all_output_lines = f.read()

    print(parse_cdp_neighbors(all_output_lines))

    with open('sh_cdp_n_sw1.txt', 'r') as f:
        all_output_lines = f.read()

    print(parse_cdp_neighbors(all_output_lines))