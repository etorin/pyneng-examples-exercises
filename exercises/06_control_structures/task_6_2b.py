# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# just to start cicle
ip_incorrect_bool = True

while ip_incorrect_bool:
    # flag of any mistake in IP
    bit_int_invalid = False
    ip_add_str = input("Type IP here: ")

    # check for var existing 
    if ip_add_str:

        # check for var length
        if len(ip_add_str.split('.')) == 4:
            
            # check for some mistakes - if not digit or not ipv4 numbers
            for bit_str in ip_add_str.split('.'):
                try:
                    # if int
                    bit_int = int(bit_str)
                    # if < 256
                    if int(bit_str) >= 256:
                        bit_int_invalid = True
                        print("{} > 255 - bit_int_invalid defined".format(int(bit_str)))
                        break
                    # and if > 0
                    elif int(bit_str) < 0:
                        bit_int_invalid = True
                        print("{} < 0 - bit_int_invalid defined".format(int(bit_str)))
                        break
                except ValueError:
                    bit_int_invalid = True
                    print("except ValueError: - bit_int_invalid defined - not digit")
                    break
            
            # point to exit with mistake flag
            if bit_int_invalid:
                print("bit_int_invalid - {}".format(bit_int_invalid))

            # correct point to continue
            elif not bit_int_invalid:
                print('The Correct Ip adress is {}'.format(ip_add_str))

                first_bype_of_ip_add = int(ip_add_str.split(".")[0])

                if ip_add_str=="0.0.0.0":
                    print("unassigned")
                    break

                elif ip_add_str=="255.255.255.255":
                    print("local broadcast")
                    break
                
                elif first_bype_of_ip_add <= 223:
                    print("unicast")
                    break

                elif first_bype_of_ip_add <= 239:
                    print("multicast")
                    break

                else:
                    print("unused")
                    break

            # unexpected point to exit
            else:
                print("try bit_int_invalid - else")
                pass
        else:
            print("length wrong")
    else:
        print("Empty str")