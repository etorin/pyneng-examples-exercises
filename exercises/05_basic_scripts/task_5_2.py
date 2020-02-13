# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_net_mask=input("Insert IP address (X.X.X.X/XX): ")

template_ip = ('''
Network:
{:<8} {:<8} {:<8} {:<8}''')
template_ip_bits = ('''{:08b} {:08b} {:08b} {:08b}''') 
template_mask = ('''
Mask:
\\{}
{:<8} {:<8} {:<8} {:<8}
{:<8} {:<8} {:<8} {:<8}
''')

ip_template = template_ip + '\n' + template_ip_bits + '\n' +template_mask

ip,mask = ip_net_mask.split('/')
ip_oct = ip.split(".")

mask_str='1'*int(mask)+'0'*(32-int(mask))

template_mask_list=[mask]
template_mask_list.append(int('0b'+mask_str[0:8], 2))
template_mask_list.append(int('0b'+mask_str[8:16], 2))
template_mask_list.append(int('0b'+mask_str[16:24], 2))
template_mask_list.append(int('0b'+mask_str[24:32], 2))

template_mask_list.append(mask_str[0:8])
template_mask_list.append(mask_str[8:16])
template_mask_list.append(mask_str[16:24])
template_mask_list.append(mask_str[24:32])

#=== Запрещенный,но не самый элегантный прием ===#
ip_oct.extend(ip_oct)
numbers = [ int(x) for x in ip_oct ]
numbers.append(mask)
n=8
mask_octs_str = [mask_str[i:i+n] for i in range(0, len(mask_str), n)]
mask_octs = [ int('0b'+x, 2) for x in mask_octs_str ]
numbers.extend(mask_octs)
numbers.extend(mask_octs_str)
print(ip_template.format(*numbers))
print('='*50, '\n')
#================================================#

print(template_ip.format(int(ip_oct[0]),int(ip_oct[1]),int(ip_oct[2]),int(ip_oct[3])))
print(template_ip_bits.format(int(ip_oct[0]),int(ip_oct[1]),int(ip_oct[2]),int(ip_oct[3])))
print(template_mask.format(*template_mask_list))