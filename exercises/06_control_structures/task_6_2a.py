# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip_add = input("Type IP here in right format: ")

if ip_add:
    if len(ip_add.split('.')) == 4:
        for bit in ip_add.split('.'):
            if bit.isdecimal():
                pass
            else:
                print("Wrong address-3")
                exit(0)

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

    else:
        print("Wrong address-2")
        exit(0)

else:
    print("Wrong address-1")
    exit(0)