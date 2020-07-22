# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_add=input("Input IP-add if format 10.0.1.1: ")

if ip_add=="0.0.0.0":
    print("unassigned")
    exit(0)
elif ip_add=="255.255.255.255":
    print("local broadcast")
    exit(0)

first_bype_of_ip_add = int(ip_add.split(".")[0])
if first_bype_of_ip_add <= 223:
    print("unicast")
    exit(0)
elif first_bype_of_ip_add <= 239:
	print("multicast")
	exit(0)
else:
	print("unused")
	exit(0)
