# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:43:02 2022

@author: Lukasz Ziecina gr2
"""

'''
Program służy do odnajdywania liczb Armstronga w zbiorze liczb naturalnych w zakresie podanym przez użytkownika.
1. Podajemy liczbę która będzie maksimum iteracji
2. Definiujemy funkcję, która zamienia kolejne liczby na string aby określij jej długość i umożliwić odwołanie do każdej kolejnej składowej liczby
3. Wrzucamy każda cyfre do tablicy jako int
4. Sumujemy n-tą potęgę każdej liczby
5. Wywołujemy funkcję zadaną ilość razy i sprawdzamy warunek Armstronga
6. Znalezione liczby dodajemy do tablicy i wyświetlamy wynik.
'''



#Functions
def find_armstrong(number):
    a = number
    b = str(a) #Replace with string - because any character can be referenced 
    p = len(b) 
    n = []
    s = 0
    for i in range(0, p, 1):
        n.append(int(b[i]))
        s += n[i]**p #Add the sum of exp of the numbers 
    return s



#Main        
if __name__ == "__main__":

    #Input
    value = int(input('Podaj maksymalna liczbe calkowita, ktora bedzie sprawdzana pod katem liczb Armstronga: '))
    
    z = 0
    Armstrong = []
    for f in range (1, value + 1, 1): #Iterate a range of numbers up to the maximum number given 
        z = find_armstrong(f)
        if z == f:
            Armstrong.append(f)
            
    print("Lista znalezionych liczb Armstronga: ")        
    print(Armstrong)