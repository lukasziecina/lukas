# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:53:15 2022

@author: Lukasz Ziecina gr2
"""

"""
Program do wyszukiwania liczb pierwszych metodą Sita Eratostenesa.
1. Tworzymy listę liczb naturalnych z przedziału [2,n] – n podaje użytkownik
2. Program wyszukuje najmniejszą (funkcja: find_the_smallest) i zeruje jej wielokrotności w całej liście.
3. Kolejno wyszukuje najmniejszą (nie 0) kolejną liczbę i zeruje jej wielokrotności aż do warunku: najmniejsza jest mniejsza od pierwiastka kwadratowego z „n”.
4. Kolejno tworzymy nową tablicę bez zer jako wynik.
"""

#Import
from math import sqrt

#Functions
def find_the_value_not_zero(table, left, right): 
    i = left
    value = 0
    while value == 0 or i == right:
        if table[i] != 0:
            value = table[i]
        else:
            i += 1
    return i    

def find_the_smallest(table, left, right):
    a = left
    i = left + 1
    while i <= right:
        if table[i] < table[a]:
            a = i
        i += 1
    return a

def do_Sito_Eratostenesa (table, the_smallest):
    for z in range(0, n-1, 1):
        if (((table[z])%(the_smallest)) == 0) and (table[z] != the_smallest):
            table[z] = 0
            #print(table)
    return table





if __name__ == "__main__":
    
    #User input
    n = int(input("Podaj zakres do metody Sito Eratostenesa: "))


    #Data
    series=[]

    for i in range(2, n+1, 1):
        series.append(i)

    #print(series)
    
    square_root_of_n = int(sqrt(n)) #The condition of the last smallest verified number
    the_smallest_index = 0
    the_smallest = 0
      
    while square_root_of_n>the_smallest:
        
        the_smallest_index = find_the_value_not_zero(series, the_smallest_index, n-2)
        the_smallest = series[the_smallest_index]
        #print(the_smallest_index)
        #print(the_smallest)
        if square_root_of_n>the_smallest:
            series = do_Sito_Eratostenesa(series, the_smallest)
            the_smallest_index += 1 
        #print(series)
        
    
    #Result
    prime_numbers = []
    for i in range(0, n-1, 1):
        if series[i] != 0:
            prime_numbers.append(series[i])
    print("Ponizej tabela liczb pierwszych ze zbioru: [2.."+str(n) +"]:")
    print(prime_numbers)
