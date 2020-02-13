# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

mode_type=input("Insert int mode (access/trunk): ")
int_type=input("Insert int type and number (ex.Gi0/3): ")

dict_of_config = {"access":access_template, "trunk":trunk_template}
dict_of_questions = {"access":"Input VLAN number(ex. 1): ", 
					 "trunk":"Input allowed VLAN numbers (ex. 1,2,3 or 1-5): "}

vlan_num=input("{}".format(dict_of_questions[mode_type]))

print('\ninterface {}'.format(int_type))
print('\n'.join(dict_of_config[mode_type]).format(vlan_num),'\n')