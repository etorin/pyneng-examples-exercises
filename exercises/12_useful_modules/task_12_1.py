# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess
from typing import List

def ping_ip_addresses(ip_address_list, count=1):
    '''
    Ping IP address and return tuple
    '''
    available_list = List['str'] = []
    unavailable_list = List['str'] = []
    for ip in ip_address_list:
        reply = subprocess.run('ping -c {} -n {}'
                               .format(count, ip),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
#                               encoding='utf-8')
        if reply.returncode == 0:
#            print(ip, 'OK')
            available_list.append(ip)
        else:
#            print(ip, 'Not OK')
            unavailable_list.append(ip)
    return (available_list, unavailable_list)

if __name__ == '__main__':
    print(ping_ip_addresses(['192.168.109.141', '8.8.8.8', '192.168.199.1', '1.1.1.1', '2.2.2.2']))
