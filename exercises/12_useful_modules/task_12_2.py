# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''

import ipaddress

def if_ip(ip_or_not):
    '''
    Функция принимает на вход что-то и проверяет,
    ip это или нет. Возвращает объект ip в случае успеха
    Тут можно было возвращать строку с IP.
    '''
    try:
        ip = ipaddress.ip_network(ip_or_not)
        return ip
    except ValueError:
        return False

def convert_ranges_to_ip_list(incoming_list):
    '''
    Конвертирует список IP-адресов в разных форматах в список, 
    где каждый IP-адрес указан отдельно.
    '''
    # Пустой список
    list_of_full_ips = []
    # Цикл по входному листу
    for ip_or_range in incoming_list:
        # Если указан диапазон
        if '-' in ip_or_range:
            # Часть IP до тире
            ip_obj = if_ip(ip_or_range.split('-')[0])
            # Часть IP после тире
            ip_second_obj = if_ip(ip_or_range.split('-')[1])
            # И если обе части являются IP адресами
            if ip_obj and ip_second_obj:
                # то тут диапазон между 2-мя IP
                # нужен список октетов первого и второго IP
                ip_obj_list = ip_obj.network_address.compressed.split('.')
                ip_second_obj_list = ip_second_obj.network_address.compressed.split('.')
                # Тут бесполезная проверка на совпадение первых 3х октетов
                if all(ip_obj_list[i] == ip_second_obj_list[i] for i in range(0, 3)):
                    # если совпали - проходим по диапазону между начальным и конечным значением 4-го октета
                    for i in range(int(ip_obj_list[3]), int(ip_second_obj_list[3])+1):
                        # тут костыль для первых трех
                        list_of_octets = [ip_obj_list[y] for y in range(0,3)]
                        # тут не смог разом получить и join всех четырех, поэтому так
                        list_of_octets.append(str(i))
                        # в итоге в цикле добавляем все IP
                        list_of_full_ips.append('.'.join(list_of_octets))
                # Иначе десятичная математика не подойдет
                else:
                   print('More sophisticated math')
            # А если первый IP, а второй нет
            elif ip_obj and not ip_second_obj:
                # Часть IP до тире и нужен список октетов
                ip_obj = if_ip(ip_or_range.split('-')[0])
                ip_obj_list = ip_obj.network_address.compressed.split('.')
                # Часть НЕ IP после тире
                last_octet = int(ip_or_range.split('-')[1])
                # Тут проходим по диапазону между начальным и конечным значением 4-го октета
                for i in range(int(ip_obj_list[3]), last_octet + 1):
                    # тут тот же костыль
                    list_of_octets = [ip_obj_list[y] for y in range(0, 3)]
                    list_of_octets.append(str(i))
                    list_of_full_ips.append('.'.join(list_of_octets))
        else:
            # если не диапазон вообще
            print('This {} is not range'.format(ip_or_range))
            # проверяем что ip и добавляем в список общий
            if if_ip(ip_or_range):
                list_of_full_ips.append(ip_or_range)
            # иначе какая-то непонятная переменная, ну ее
            else:
                print('Strange value {}'.format(ip_or_range))

    return list_of_full_ips

if __name__ == '__main__':
    list_of_ips_and_ranges = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(list_of_ips_and_ranges))