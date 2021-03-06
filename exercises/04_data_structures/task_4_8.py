# -*- coding: utf-8 -*-
task = ('Задание 4.8'
'\n\n'
'Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:\n'
'- первой строкой должны идти десятичные значения байтов\n'
'- второй строкой двоичные значения'
'\n\n'
'Вывод должен быть упорядочен также, как в примере:\n'
'- столбцами\n'
'- ширина столбца 10 символов'
'\n\n'
'Пример вывода для адреса 10.1.1.1:\n'
'10        1         1         1\n'
'00001010  00000001  00000001  00000001'
'\n\n'
'Ограничение: Все задания надо выполнять используя только пройденные темы.\n'
)

ip = '192.168.3.1'

print(task)
print(ip, '\n')

ip_list = ip.split(".")
print("{:8} {:8} {:8} {:8}".format(*ip_list))
# А вдруг можно лаконичнее?
print('{:08b} {:08b} {:08b} {:08b}'.format(int(ip_list[0]), int(ip_list[1]), int(ip_list[2]), int(ip_list[3])))