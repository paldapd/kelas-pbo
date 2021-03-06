# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:12:17 2021

@author: Palda Puspita Dianti
"""

class student :
    """ A class representing a student """
    def __init__ (self,n,a,p,i,g):
        self.full_name=n
        self.age=a
        self.prodi=p
        self.nim=i
        self.gender=g
    
    def get_age (self) :
        return self.age
    def get_univ (self) :
        return self.univ
    def get_prodi (self) :
        return self.prodi
    def get_nim (self) :
        return self.nim
    def get_gender (self) :
        return self.gender
f = student ("Palda Puspita Dianti", 19, "Sistel", 1904211, "Perempuan")   
print (f.full_name)
print (f.get_age())
print (f.get_prodi())
print (f.get_nim())
print (f.get_gender())