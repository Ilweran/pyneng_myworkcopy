# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

prefix      = input('Input network in the format \"prefix/len\": ')
ip_address  = prefix.split("/")[0]
mask_num    = int(prefix.split("/")[1])

ip_oct1, ip_oct2, ip_oct3, ip_oct4 = ip_address.split('.')

ip_oct1_d = int(ip_oct1)
ip_oct2_d = int(ip_oct2)
ip_oct3_d = int(ip_oct3)
ip_oct4_d = int(ip_oct4)

ip_oct1_bin_str = format(ip_oct1_d, '#010b')[2:]
ip_oct2_bin_str = format(ip_oct2_d, '#010b')[2:]
ip_oct3_bin_str = format(ip_oct3_d, '#010b')[2:]
ip_oct4_bin_str = format(ip_oct4_d, '#010b')[2:]

ip_str = ip_oct1_bin_str + ip_oct2_bin_str + ip_oct3_bin_str + ip_oct4_bin_str

mask_str = "1" * mask_num + "0" * (32 - mask_num)
tmp_str = (mask_str + '.')[mask_str.find('0'):-1]
final_ip_str = ip_str[:-len(tmp_str)] + tmp_str

fin_ip_oct1 = final_ip_str[:8]
fin_ip_oct2 = final_ip_str[8:16]
fin_ip_oct3 = final_ip_str[16:24]
fin_ip_oct4 = final_ip_str[24:]

m_oct1  = mask_str[0:8]
m_oct2  = mask_str[8:16]
m_oct3  = mask_str[16:24]
m_oct4  = mask_str[24:]

m_oct1_d = int(m_oct1, base=2)
m_oct2_d = int(m_oct2, base=2)
m_oct3_d = int(m_oct3, base=2)
m_oct4_d = int(m_oct4, base=2)

print(f'''
    Network:
    {int(fin_ip_oct1, base=2):<10}{int(fin_ip_oct2, base=2):<10}{int(fin_ip_oct3, base=2):<10}{int(fin_ip_oct4, base=2):<10}
    {fin_ip_oct1:<10}{fin_ip_oct2:<10}{fin_ip_oct3:<10}{fin_ip_oct4:<10}

    Mask:
    /{mask_num}
    {m_oct1_d:<10}{m_oct2_d:<10}{m_oct3_d:<10}{m_oct4_d:<10}
    {m_oct1_d:08b}  {m_oct2_d:08b}  {m_oct3_d:08b}  {m_oct4_d:08b}
    ''')
