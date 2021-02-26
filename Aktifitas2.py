# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:22:18 2021

@author: Palda Puspita Dianti
"""

#OPERATOR
bil1 = int (input("Masukan Angka Pertama: "))
bil2 = int (input("Masukan Angka Kedua: "))

jumlah = bil1+bil2
kurang = bil1-bil2
kali = bil1*bil2
bagi = bil1/bil2
modulus = bil1%bil2

print ("Hasil dari %d + %d = %d" % (bil1, bil2, jumlah))
print ("Hasil dari %d - %d = %d" % (bil1, bil2, kurang))
print ("Hasil dari %d * %d = %d" % (bil1, bil2, kali))
print ("Hasil dari %d / %d = %d" % (bil1, bil2, bagi))
print ("Hasil dari %d mod %d = %d" % (bil1, bil2, modulus))