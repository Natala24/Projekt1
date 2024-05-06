
from math import *
import numpy as np
import argparse
import os



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
    
    # BLH ---> XYZ
        """
            Algorytm przelicza współrzędne geodezyjne (BLH) na współrzędne w układzie ortokartezjańskim (XYZ)
        """
    def filh2XYZ(self, fi, lam, h):
        XYZ = []
        for fi, lam, h in zip(fi, lam, h):
            while True:
                N = self.Npu(fi)
                X = (N + h) * np.cos(fi) * np.cos(lam)
                Xp = X
                Y = (N + h) * np.cos(fi) * np.sin(lam)
                Z = (N * (1 - self.e2) + h) * np.sin(fi)
                if abs(Xp - X) < (0.000001/206265):
                    break
            
            XYZ.append([X, Y, Z])
        return(XYZ)



        # XYZ ---> NEU
        """
            Obliczenie macierzy Rneu
        """
    def Rneu(self, fi, lam):
        Rneu = np.array([[-np.sin(fi)*np.cos(lam), -np.sin(lam), np.cos(fi)*np.cos(lam)],
                         [-np.sin(fi)*np.sin(lam),  np.cos(lam), np.cos(fi)*np.sin(lam)],
                         [             np.cos(fi),            0,             np.sin(fi)]])
        return(Rneu)
    
    
        """
            Przeliczenie wsp XYZ na neu
        """
    def xyz2neup(self, X, Y, Z, X0, Y0, Z0):
        neu = []
        p = np.sqrt(X0**2 + Y0**2)
        fi = np.arctan(Z0 / (p*(1 - self.e2)))
        while True:
            N = self.Npu(fi)
            h = (p / np.cos(fi)) - N
            fi_poprzednia = fi
            fi = np.arctan((Z0 / p)/(1-((N * self.e2)/(N + h))))
            if abs(fi_poprzednia - fi) < (0.000001/206265):
                break 
        N = self.Npu(fi)
        h = p/np.cos(fi) - N
        lam = np.arctan(Y0 / X0)
        
        R_neu = self.Rneu(fi, lam)
        X_sr = [X - X0, Y - Y0, Z - Z0] 
        X_rneu = R_neu.T@X_sr
        neu.append(X_rneu.T)
            
        return(neu)



        # TRANSFORMACJA WSP BL ---> 1992
        """
            Algorytm przelicza współrzędne geodezyjne (BL) na współrzędne w układzie 1992 (XY)
        """
    def cale92(self, fi, lam):
        lam0 = (19*np.pi)/180
        m = 0.9993
        wsp = []
        for fi,lam in zip(fi,lam):
            b2 = (self.a**2) * (1-self.e2)   #krotsza polowa
            e2p = (self.a**2 - b2 ) / b2   #drugi mimosrod elipsy
            dlam = lam - lam0
            t = np.tan(fi)
            ni = np.sqrt(e2p * (np.cos(fi))**2)
            N = self.Npu(fi)
            sigma = self.Sigma(fi)
            
            xgk = sigma + ((dlam**2)/2)*N*np.sin(fi)*np.cos(fi) * ( 1+ ((dlam**2)/12)*(np.cos(fi))**2 * ( 5 - (t**2)+9*(ni**2) + 4*(ni**4)     )  + ((dlam**4)/360)*(np.cos(fi)**4) * (61-58*(t**2)+(t**4) + 270*(ni**2) - 330*(ni**2)*(t**2))  )
            ygk = (dlam*N* np.cos(fi)) * (1+(((dlam)**2/6)*(np.cos(fi))**2) *(1-(t**2)+(ni**2))+((dlam**4)/120)*(np.cos(fi)**4)*(5-18*(t**2)+(t**4)+14*(ni**2)-58*(ni**2)*(t**2)) )
                        
            x92 = xgk*m - 5300000
            y92 = ygk*m + 500000
            wsp.append([x92, y92]) 
            
        return(wsp)

