# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 22:18:38 2022

@author: Lukasz Ziecina gr2
"""

"""
Program pozwalający grać w grę MasterMind.
Kod do odgadnięcia składa się z 4 cyfr od 1-6 (cyfry mogą się powtarzać). Kod losowany jest funkcją Random.
Wpisana przez zgadującego liczba sprawdzana jest pod kątem zgodności: 4 cyfry od 1-6. Jeżeli błędna liczba gracz traci jedną szansę.
Jeżeli gracz wpiszę liczbę to dostaję informację czy zgadł i jeśli nie to program podpowiada o ilości cyfr na właściwym miejscu i ilości wszystkich wystąpieć.
Gracz ma 10 szans.
P.S.
Gdzieś mi się taki opis gry w wersji „cyferki” udało zdobyć i stąd taki sposób podpowiadania.
"""

#Import
import random

#Main
if __name__ == "__main__":
    
    random_number = []  #Random number 
    for i in range(0, 4, 1):
        random_number.append(random.randrange(1, 6, 1))
        
    #print(random_number)
    
    guessing_number_table = [0, 0, 0, 0]
    number_of_tries = 1
    
    while (guessing_number_table != random_number) and (number_of_tries<11):
        #Input
        guessing_number = int(input("Wpisz liczbe 4 cyfrowa - kazda cyfra jest w zakresie 1-6 - Powodzenia: "))
        
        #Validating the entered number 
        if len(str(guessing_number)) == 4:
            
            for i in range(0, 4, 1):
                guessing_number_table[i] =int(str(guessing_number)[i])
            print(guessing_number_table)
            
            if (guessing_number_table[0] > 0) and (guessing_number_table[0] < 7):
                if (guessing_number_table[1] > 0) and (guessing_number_table[1] < 7):
                    if (guessing_number_table[2] > 0) and (guessing_number_table[2] < 7):
                        if (guessing_number_table[3] > 0) and (guessing_number_table[3] < 7):
                            is_guessing_number_ok = True
                        else:
                            is_guessing_number_ok = False
                    else:
                        is_guessing_number_ok = False
                else:
                    is_guessing_number_ok = False
            else:
                is_guessing_number_ok = False
        else:
            is_guessing_number_ok = False
    
        #Checking whether the user has guessed a number 
        if guessing_number_table == random_number:
            print("!!!!!!!!!!!!!!!!!WYGRALES!!!!!!!!!!!!!!!!")
            print("Za: " + str(number_of_tries) + " proba :)")
            break
            
        
        if is_guessing_number_ok == True:                 
            counter_of_guessed_numbers = 0
            for find_exactly in random_number:
                if find_exactly in guessing_number_table:
                    counter_of_guessed_numbers += 1
            
            print("Odgadles: " + str(counter_of_guessed_numbers) + " wystapienia cyfr w zbiorze.")
            
            number_counter_on_the_right_place = 0
            for z in range(0, 4, 1):
                if random_number[z] == guessing_number_table[z]:
                    number_counter_on_the_right_place += 1
            print("Liczba cyfr na wlasciwym miejscu: "+ str(number_counter_on_the_right_place))
            print("Pozostalo: "+ str(10-number_of_tries)+" prob :(")
            number_of_tries += 1
        else:
            number_of_tries += 1
            print("Wpisales bledna liczbe, pozostalo: "+ str(10-number_of_tries)+" prob :(")
        
    
    print("Koniec :)-")