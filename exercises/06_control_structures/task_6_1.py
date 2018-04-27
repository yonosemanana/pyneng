# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

IP_ADDR = input("Enter ip address in format '10.0.1.1': ")

FIRST_OCTET = int(IP_ADDR.split(".")[0])

if FIRST_OCTET >= 1 and FIRST_OCTET <= 223:
    print("unicast")
elif FIRST_OCTET >= 224 and FIRST_OCTET <= 239:
    print("multicast")
elif IP_ADDR == "0.0.0.0":
    print("unassigned")
elif IP_ADDR == "255.255.255.255":
    print("local broadcast")
else:
    print("unused")
    
    
