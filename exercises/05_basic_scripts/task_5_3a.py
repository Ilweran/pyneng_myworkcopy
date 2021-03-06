# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

switchport_mode_template = {
    "access":   access_template,
    "trunk":    trunk_template,
}

question_template = {
    "access":   "Input PVID: ",
    "trunk":    "Input allowed VLANs: ",
}

intf    = input("Input interface type/number: ")
mode    = input("Input interface mode: ")
vlans   = input(question_template[mode])

print("\n")

print("interface ", intf)
print("\n".join(switchport_mode_template[mode]).format(vlans))
