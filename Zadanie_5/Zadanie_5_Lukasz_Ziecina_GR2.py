# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 09:51:38 2022

@author: Lukasz Ziecina gr2
"""

"""
Metoda Gronsfelda
Program do szyfrowania tekstu metodą Gronsfelda. 
W pierwszej kolejność generujemy słownik (bez polskich znaków, ale ze znakami specjalnymi, małymi i dużymi lirami.
Kolejno dopasowujemy długość klucza do długości tekstu, który ma być zaszyfrowany - przez dopełnienie.                               
Po kolei wyszukujemy indeksu każdego znaku i albo dodajemy albo odejmujemy indeks według tablicy klucza i na nowo przeszukujemy słownik otrzymując wynik.
"""

#Functions
def find_value(value, table): #Look for values in the table and return the index 
    f=0
    for i in table:
        if i == value:
            return f
        f += 1
    return f

def gronsfeld_cipher (table, key, text): #Encryption with the Gronsfeld method 
    
    key_len = len(str(key))
    key_str =  str(key)
    text_len = len(text)
    table_len = len(table)
    
    #Padding the key to the encrypted text
    key_completed = []
    
    if key_len == text_len:
        for i in range(0, text_len, 1):
            key_completed.append(key_str[i]) 
    elif key_len < text_len:
        g = 0
        for i in range(0, text_len, 1):
            
            key_completed.append(key_str[g]) 
            if g < (key_len-1):
                g += 1
            else:
                g=0
    else:
        for i in range(0, text_len, 1):
            key_completed.append(key_str[i]) 

    crypted_text = ""
    crypted_text_table = []
    a = 0
    b = 0
    #We find the index of the next letter and successively shift them by the key value 
    for i in range(0, text_len, 1):
        a = find_value(text[i], table)
        b = a + int(key_completed[i])
        if b > (table_len-1):
            b = b - table_len
        crypted_text_table.append(table[b])
        crypted_text += str(crypted_text_table[i])
        
    return crypted_text

def gronsfeld_decryption (table, key, crypted_text): #Decryption with the Gronsfeld method
    
    key_len = len(str(key))
    key_str =  str(key)
    text_len = len(crypted_text)
    table_len = len(table)
    
    #Padding the key to the encrypted text 
    key_completed = []
    
    if key_len == text_len:
        for i in range(0, text_len, 1):
            key_completed.append(key_str[i]) 
    elif key_len < text_len:
        g = 0
        for i in range(0, text_len, 1):
            
            key_completed.append(key_str[g]) 
            if g < (key_len-1):
                g += 1
            else:
                g=0
    else:
        for i in range(0, text_len, 1):
            key_completed.append(key_str[i]) 

    decrypted_text = ""
    decrypted_text_table = []
    a = 0
    b = 0
    #We find the index of the next letter and successively shift them by the key value 
    for i in range(0, text_len, 1):
        a = find_value(crypted_text[i], table)
        b = a - int(key_completed[i])
        if b > (table_len-1):
            b = b - table_len
        decrypted_text_table.append(table[b])
        decrypted_text += str(decrypted_text_table[i])
        
    return decrypted_text




if __name__ == "__main__":
    
    #Input
    gronsfeld_key = 123599998889
    unencrypted_text = "Cyberbezpieczenstwo w praktyce :)~"
    crypted_text = "D{ej{kn$xqml{gqx}!x) (x{bmw~ln)C1'"
    
    #Table
    dictionary=[]
    for i in range(32,127):
        dictionary.append(chr(i))
    print(dictionary)

    #Encryption 
    print(gronsfeld_cipher(dictionary, gronsfeld_key, unencrypted_text))
    
    #Decryption  
    print(gronsfeld_decryption(dictionary, gronsfeld_key, crypted_text))
            
    