# -*- coding: utf-8 -*-
task = ('Задание 4.6'
'\n\n'
'Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:'
'\n\n'
'Protocol:              OSPF\n'
'Prefix:                10.0.24.0/24\n'
'AD/Metric:             110/41\n'
'Next-Hop:              10.0.13.3\n'
'Last update:           3d18h\n'
'Outbound Interface:    FastEthernet0/0'
'\n\n'
'Ограничение: Все задания надо выполнять используя только пройденные темы.\n'
)

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

print(task)
print(ospf_route, '\n')

ospf_route_list = ospf_route.split()

ospf_route_list.remove('via')

ospf_route_list.pop(0)

ospf_route_list.insert(0, 'OSPF')

ospf_route_list[2]=ospf_route_list[2][1:7]

form = (''
'Protocol:              {}\n'
'Prefix:                {}\n'
# Тут бы скобки убрать...
'AD/Metric:             {}\n'
'Next-Hop:              {:10.9}\n'
# Тут я не смог найти аналога [:-1], чтоб срезать последний символ
'Last update:           {:10.5}\n'
'Outbound Interface:    {}\n')

print(form.format(*ospf_route_list))