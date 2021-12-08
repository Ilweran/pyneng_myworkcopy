# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""
ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route_list = ospf_route.split()
prefix  = ospf_route_list[0]
ad      = ospf_route_list[1]
nh      = ospf_route_list[3][:-1]
age     = ospf_route_list[4][:-1]
intf    = ospf_route_list[5]
print(f'''
{"Prefix":<20}{prefix:<20}
{"AD/Metric":<20}{ad:<20}
{"Next-Hop":<20}{nh:<20}
{"Last Update":<20}{age:<20}
{"Outbound Interface":<20}{intf:<20}''')
