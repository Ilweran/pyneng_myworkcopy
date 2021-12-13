from sys import argv

#print("Input IP address and mask in the format ipaddr/mask: " )
#prefix      = input('Input network in the format \"prefix len\": ')
ip_address  = argv[1]
mask_num    = int(argv[2])

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


