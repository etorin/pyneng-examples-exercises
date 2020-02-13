# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# Input some subnet
ip_net_mask=input("Insert IP address (X.X.X.X/XX): ")

# Definition of templates with alignment
template_ip = ('''
Network:
{:<8} {:<8} {:<8} {:<8}
{:<8} {:<8} {:<8} {:<8}''') 

template_mask = ('''
Mask:
\\{}
{:<8} {:<8} {:<8} {:<8}
{:<8} {:<8} {:<8} {:<8}
''')

# Devide and define ip and mask parts of input
ip,mask = ip_net_mask.split('/')
# Devide ip by octets in list
ip_oct = ip.split(".")

# Empty list to Network part 
net_list = []

# Every octet becomes the string of 8 symbols 0 and 1 - binary view and added to list
net_list.append(str(format(int(ip_oct[0]), '08b')))
net_list.append(str(format(int(ip_oct[1]), '08b')))
net_list.append(str(format(int(ip_oct[2]), '08b')))
net_list.append(str(format(int(ip_oct[3]), '08b')))

# Count network
# Current net list becomes the long string included 32 bits
net_str =''.join(net_list)

# Separation network and ip part by lenght of mask
net_net = net_str[0:int(mask)]
net_add = net_str[int(mask):32]
# Replase ip part by zeros
net_add = '0'*(32-int(mask))
# Get 32 bits of network again
net_net = net_net+net_add

# Make net list empty again (to use '*list' in template format)
net_list = []

# Get network list from octets, whitch became demical
net_list.append(int(net_net[0:8], 2))
net_list.append(int(net_net[8:16], 2))
net_list.append(int(net_net[16:24], 2))
net_list.append(int(net_net[24:32], 2))

# Add to list binary view of network
net_list.append(net_net[0:8])
net_list.append(net_net[8:16])
net_list.append(net_net[16:24])
net_list.append(net_net[24:32])

# Count mask in binary view
mask_str='1'*int(mask)+'0'*(32-int(mask))

# Make mask list to use '*list' in template format
template_mask_list=[mask]

# Get mask list from octets, whitch became demical by int function
template_mask_list.append(int('0b'+mask_str[0:8], 2))
template_mask_list.append(int('0b'+mask_str[8:16], 2))
template_mask_list.append(int('0b'+mask_str[16:24], 2))
template_mask_list.append(int('0b'+mask_str[24:32], 2))

# Add to list binary view of mask
template_mask_list.append(mask_str[0:8])
template_mask_list.append(mask_str[8:16])
template_mask_list.append(mask_str[16:24])
template_mask_list.append(mask_str[24:32])

# Using format function to print result
print(template_ip.format(*net_list))
print(template_mask.format(*template_mask_list))