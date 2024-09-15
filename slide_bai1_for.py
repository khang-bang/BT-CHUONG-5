# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:23:51 2024

@author: Student
"""
n = int(input("Nhập số n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i
print(f"{n}! = {giai_thua} ")