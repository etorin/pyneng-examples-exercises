# -*- coding: utf-8 -*-

task = ('Задание 4.1'
'\n'
'Обработать строку nat таким образом,'
'чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.'
'\n'
'Ограничение: Все задания надо выполнять используя только пройденные темы.'
'\n'
)

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'

print(task)
print(nat, '\n')
print(nat.replace("FastEthernet", "GigabitEthernet"), '\n')