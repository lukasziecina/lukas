# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 23:05:04 2021

@author: Lukasz Ziecina gr2
"""
'''
Program rozwiązujący układ równań N równań liniowych o N niewiadomych.
1. Wczytujemy plik tekstowy i zamieniamy tekst na wartości rzeczywiste (eliminując znaki - spacja/znak końca linii)
2. Tworzymy macierz glowną, uzupelniona i wyrazow wolnych
3. Wyznaczamy wskaźnik macierzy A, rząd macierzy A i U
4. Zgodnie z teoria Kroneckera-Capellego sprawdzamy czy układ równań bedzie oznaczony, sprzeczny czy nieoznaczony
5. Jeżeli układ jest oznaczony to liczymy macierz niewiadomych X metodą macierzy odwrotnej
6. Aby wybrac przykladowa macierz należy odkomentować jedną z 3 linijek
7. Wyświetlamy wyniki
'''

##################################################################################################

#Import
import numpy as np

if __name__ == "__main__":

    # Try to open file and read data
    matrix_file = open("oznaczony.txt")
    #matrix_file = open("sprzeczny.txt")
    #matrix_file = open("nieoznaczony.txt")
    
    try:
        matrix_data = matrix_file.read()
        matrix_data = matrix_data.split("\n") #Delate end line sign
        #print(matrix_data)
        matrix_data = [l.split(" ") for l in matrix_data] #Delate space
    finally:
        matrix_file.close() # Close file
    
    
    n = tuple(map(float,matrix_data[0]))
    N = int(n[0]) #Calculating the number of equations
    
    
    U = np.zeros(shape=(N,N+1)) #Init Matrix U
    A = np.zeros(shape=(N,N))   #Init Matrix A
    B = np.zeros(shape=(N,1))   #Init Matrix B
    a = []
    for i in range(1, N+1, 1):
        a = tuple(map(float, matrix_data[i]))
        U[i-1] = a
        A[i-1] = a[:-1]
        B[i-1] = a[-1]
    
    print("Wykryto plik z ukladem "+ str(N) + " rownan z " + str(N) +" niewiadomymi")
    print("Macierz uzupelniona U:")
    print(U)
    print("Macierz glowna A:")
    print(A)
    print("Macierz wyrazow wolnych B:")
    print(B)
    
    W_A = np.linalg.det(A)
    R_A = np.linalg.matrix_rank(A)
    R_U = np.linalg.matrix_rank(U)
    print("Wskaznik macierzy A: " + str(W_A))
    print("Rzad macierzy A: " + str(R_A))
    print("Rzad macierzy U: " + str(R_U))
    
    #Kronecker-Capelli theorem 
    if (R_A == N) and (R_U == N):
        print('Uklad rownan oznaczony - jedno rozwiazanie: X:')
        Aminus = np.linalg.inv(A) #Inverted matrix 
        X = np.dot(Aminus, B) # And finally here we calculate 
        print(X)
    elif R_A != R_U:
        print('Uklad rownan sprzeczny - brak rozwiazan')
    elif (R_A < N) and (R_U < N) and (R_U == R_A):
        print('Uklad rownan nieoznaczony - nieskonczenie wiele rozwiazan')
