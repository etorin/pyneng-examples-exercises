# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route_list = []

form = (''
        'Protocol:              {}\n'
        'Prefix:                {}\n'
        'AD/Metric:             {}\n'
        'Next-Hop:              {:10.9}\n'
        'Last update:           {:10.5}\n'
        'Outbound Interface:    {}\n')

with open('ospf.txt', 'r') as f: 
    for line in f: 
#        print(line)
        ospf_route_list = line.split()
#        print(ospf_route_list)
        ospf_route_list.remove('via')
#        print(ospf_route_list)
        if ospf_route_list[0] == 'O':
        	ospf_route_list[0]=ospf_route_list[0].replace('O','OSPF')
#        print(ospf_route_list)
        ospf_route_list[2]=ospf_route_list[2].replace('[','').replace(']','')
#        print(ospf_route_list)
        print(form.format(*ospf_route_list))