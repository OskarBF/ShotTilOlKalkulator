import numpy as np
import matplotlib.pyplot as plt

def ShotTilPils(N,size = 40,prosent = 40):
    ''' 
    Tar inn; N: antall shots,
      size: størrelsen på shotten i ml
      prosent: styrke på alkohol i %
      returnerer antall 4.7%, 0.5l øl
    '''
    prosent = prosent/100
    liter = N * size * 0.001
    ren_alkohol = prosent * liter
    liter_ol = ren_alkohol / 0.047
    ol = liter_ol / 0.5
    print(N, " shots tilsvarer", ol, " øl.")
    return ol
