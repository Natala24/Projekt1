
from math import *
import numpy as np
import argparse
import os

C:\Users\natal\OneDrive\Pulpit\Projekt1\python_projekt1.py


class Transformations:
    def __init__(self, elipsoida):
        """
        Parametry elipsoid:
        a - duża półos elipsoidy 
        e2 - kwadrat mimosrodu elipsoidy
            + WGS84
            + GRS80
            + Elipsoida Krasowskiego
        """
        self.a = elipsoida[0]
        self.e2 = elipsoida[1]
            
            
            
        """
        Poniższe funkcje są funkcjami pomocniczymi dla obliczeń transformacji
        """
    def Npu(self, fi):     #promien krzywizny w I wertykale
        N = self.a / np.sqrt(1 - self.e2 * np.sin(fi)**2)
        return(N)

    def Sigma(self, fi):
        A0 = 1 - (self.e2/4) - (3*(self.e2)**2)/64 -  (5*(self.e2)**3)/256
        A2 = 3/8 * (self.e2 + (self.e2)**2/4 + 15*(self.e2)**3/128)
        A4 = 15/256 * ( (self.e2)**2 + (3*((self.e2)**3))/4 )
        A6 = 35 * (self.e2)**3 / 3072
        sigma = self.a * ( A0 * fi - A2 * np.sin(2*fi) + A4 * np.sin(4*fi) - A6 * np.sin(6*fi) )
           
        return(sigma)
    

        
        # XYZ ---> BLH - ALGORYTM HIRVONENA
        """
            Następujący algorytm przelicza współrzędne z układu ortokartezjańskiego na współrzędne geodezyjne.
        """
    def hirvonen(self, X, Y, Z):
        flh = []
        for X,Y,Z in zip(X,Y,Z):
            p = np.sqrt(X**2 + Y**2)
            fi = np.arctan(Z / (p * (1 - self.e2)))
            while True:
                N = self.Npu(fi)
                h = p / np.cos(fi) - N
                fip = fi     #fip - fi poprzednie, fi - fi nowe
                fi = np.arctan(Z / (p * (1 - N * self.e2 / (N + h))))
                if abs(fip - fi) < (0.000001/206265):
                    break
        
            lam = np.arctan2(Y, X)
            flh.extend([np.rad2deg(fi), np.rad2deg(lam), h])
        return(flh)
