# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 21:18:58 2022

@author: Lukasz Ziecina gr2
"""

'''
Program do sprawdzania czy dana liczba jest palindromem. 
1. Jeżeli nie jest to zostaje zapisana od tyłu i dodana do oryginału i kolejno sprawdzana (10 powtórzeń).
2. Jeżeli zostanie osiągnięty palindrom to kończymy program z wynikiem i przechodzimy do następnej liczby.
3. Sprawdzanie 200 liczb całkowitych wykazało, że nie zawsze udało się osiągnąć palindrom o czym program poinformuje.
'''


#Functions
def reverse_number (number):
    
    a = number
    b = str(a)
    c = b[::-1]
    inwerted = int(c)
    return inwerted

def checking_palindrome (number):
    a = number
    b = str(a)
    c = len(b)
    d = []
    for i in range(0, c, 1):
        d.append(int(b[i]))
        e = d[::-1]
    palindrome = False    
    if d!=e:
        palindrome = False
    else:
        palindrome = True
    
    return palindrome

def testing_the_hypothesis (value):

    value_tested = value

    palindrome = False
    counter = 1
    while (palindrome == False) and (counter<11):
        palindrome = checking_palindrome(value_tested)
        if checking_palindrome(value_tested) == True:
            palindrome = True;
            print("Hipoteza potwierdzona dla liczby: " + str(value) + " po: "+ str(counter) + " probie, co dalo wartosc " + str(value_tested))
        else:
            value_tested = value_tested + reverse_number(value_tested)
            counter += 1
            if counter>10:
                print("Hipoteza obalona dla: " + str(value))
 
    
 
#Main        
if __name__ == "__main__": 
    
    for h in range (1, 201, 1):
        testing_the_hypothesis(h)

