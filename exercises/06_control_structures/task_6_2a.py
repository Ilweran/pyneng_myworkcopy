# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address  = input("Input IP address in the format X.X.X.X: ")

if ip_address.count('.') != 3:
    print("Incorrect IP address format.")
elif (not ip_address.split(".")[0].isdigit()) or ( not ip_address.split(".")[1].isdigit()) or (not ip_address.split(".")[2].isdigit()) or (not ip_address.split(".")[3].isdigit()):
    print("Incorrect IP address format.")
elif (int(ip_address.split(".")[0]) < 0) or (int(ip_address.split(".")[0]) > 255):
    print("Incorrect IP address format.")
elif (int(ip_address.split(".")[1]) < 0) or (int(ip_address.split(".")[1]) > 255):
    print("Incorrect IP address format.")
elif (int(ip_address.split(".")[2]) < 0) or (int(ip_address.split(".")[2]) > 255):
    print("Incorrect IP address format.")
elif (int(ip_address.split(".")[3]) < 0) or (int(ip_address.split(".")[3]) > 255):
    print("Incorrect IP address format.")
else:
    if (int(ip_address.split(".")[0]) >= 1) and (int(ip_address.split(".")[0]) <= 223):
        print("unicast")
    elif (int(ip_address.split(".")[0]) >= 224) and (int(ip_address.split(".")[0]) <= 239):
        print("multicast")
    elif (int(ip_address.split(".")[0]) == 255) and (int(ip_address.split(".")[1]) == 255) and (int(ip_address.split(".")[2]) == 255) and (int(ip_address.split(".")[3]) == 255):
        print("local broadcast")
    elif (int(ip_address.split(".")[0]) == 0) and (int(ip_address.split(".")[1]) == 0) and (int(ip_address.split(".")[2]) == 0) and (int(ip_address.split(".")[3]) == 0):
        print("unassigned")
    else:
        print("unused")
