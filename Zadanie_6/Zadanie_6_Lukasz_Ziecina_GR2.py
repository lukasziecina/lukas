# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Sun Jan  9 09:51:38 2022

@author: Lukasz Ziecina gr2

"""
"""
Program, który sprawdza empirycznie sprawdza szansę, że wśród n osób są przynajmniej k, które mają urodziny tego samego dnia.
1. Losujemy n dni urodzin i sprawdzamy, czy któryś się powtórzył – funkcja random i count.
2. Liczymy ile jest przypadków osób, które mają urodziny tego samego dnia – funkcja len
"""


#Import
import random
from collections import Counter


if __name__ == "__main__":

    #Input
    k = int(input(("Wpisz ilosc k osob, ktore moga miec urodziny tego samego dnia: ")))
    number_of_people = int(input(("Wpisz ilosc badanych ludzi: ")))
    
    if k < 2:
        k = 2
    else:
        k
     
    if number_of_people < 2:
        number_of_people = 2
    else:
        number_of_people    
    
    birthdays = []
    
    for i in range(0, number_of_people, 1):
        birthdays.append(random.randrange(1, 365, 1)) #Draw days of the year 
    
    print(birthdays)
    
    repeat = []
    for i in range (0, number_of_people):  
        if birthdays.count(i)>=k:   #Counting repetitions 
            repeat.append(birthdays.count(i)) 
    
    #print(repeat)
    print("W: "+str(len(repeat))+" przypadkach co najmniej: "+ str(k)+" osob/osoby mialo urodziny tego samego dnia.")