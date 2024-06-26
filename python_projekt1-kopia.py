from math import *
import numpy as np
import argparse
import os

class Transformations:
    def __init__(self, elipsoida):
        self.a = elipsoida[0]
        self.e2 = elipsoida[1]

    def Npu(self, fi):  # promien krzywizny w I wertykale
        N = self.a / np.sqrt(1 - self.e2 * np.sin(fi) ** 2)
        return N

    def Sigma(self, fi):
        A0 = 1 - (self.e2 / 4) - (3 * (self.e2) ** 2) / 64 - (5 * (self.e2) ** 3) / 256
        A2 = 3 / 8 * (self.e2 + (self.e2) ** 2 / 4 + 15 * (self.e2) ** 3 / 128)
        A4 = 15 / 256 * ((self.e2) ** 2 + (3 * ((self.e2) ** 3)) / 4)
        A6 = 35 * (self.e2) ** 3 / 3072
        sigma = self.a * (A0 * fi - A2 * np.sin(2 * fi) + A4 * np.sin(4 * fi) - A6 * np.sin(6 * fi))
        return sigma

    def hirvonen(self, X, Y, Z):
        flh = []
        for X, Y, Z in zip(X, Y, Z):
            p = np.sqrt(X ** 2 + Y ** 2)
            fi = np.arctan(Z / (p * (1 - self.e2)))
            while True:
                N = self.Npu(fi)
                h = p / np.cos(fi) - N
                fip = fi
                fi = np.arctan(Z / (p * (1 - N * self.e2 / (N + h))))
                if abs(fip - fi) < (0.000001 / 206265):
                    break
            lam = np.arctan2(Y, X)
            flh.append([np.rad2deg(fi), np.rad2deg(lam), h])
        return flh

    def filh2XYZ(self, fi, lam, h):
        XYZ = []
        for fi, lam, h in zip(fi, lam, h):
            N = self.Npu(fi)
            X = (N + h) * np.cos(fi) * np.cos(lam)
            Y = (N + h) * np.cos(fi) * np.sin(lam)
            Z = (N * (1 - self.e2) + h) * np.sin(fi)
            XYZ.append([X, Y, Z])
        return XYZ

    def Rneu(self, fi, lam):
        Rneu = np.array([[-np.sin(fi) * np.cos(lam), -np.sin(lam), np.cos(fi) * np.cos(lam)],
                         [-np.sin(fi) * np.sin(lam), np.cos(lam), np.cos(fi) * np.sin(lam)],
                         [np.cos(fi), 0, np.sin(fi)]])
        return Rneu

    def xyz2neup(self, X, Y, Z, X0, Y0, Z0):
        neu = []
        for x, y, z in zip(X, Y, Z):
            p = np.sqrt(X0 ** 2 + Y0 ** 2)
            fi = np.arctan(Z0 / (p * (1 - self.e2)))
            while True:
                N = self.Npu(fi)
                h = (p / np.cos(fi)) - N
                fi_poprzednia = fi
                fi = np.arctan((Z0 / p) / (1 - ((N * self.e2) / (N + h))))
                if abs(fi_poprzednia - fi) < (0.000001 / 206265):
                    break
            N = self.Npu(fi)
            h = p / np.cos(fi) - N
            lam = np.arctan2(Y0, X0)
            R_neu = self.Rneu(fi, lam)
            X_sr = [x - X0, y - Y0, z - Z0]
            X_rneu = R_neu.T @ X_sr
            neu.append(X_rneu)
        return neu

    def cale92(self, fi, lam):
        lam0 = (19 * np.pi) / 180
        m = 0.9993
        wsp = []
        for fi, lam in zip(fi, lam):
            b2 = (self.a ** 2) * (1 - self.e2)
            e2p = (self.a ** 2 - b2) / b2
            dlam = lam - lam0
            t = np.tan(fi)
            ni = np.sqrt(e2p * (np.cos(fi)) ** 2)
            N = self.Npu(fi)
            sigma = self.Sigma(fi)
            xgk = sigma + ((dlam ** 2) / 2) * N * np.sin(fi) * np.cos(fi) * (1 + ((dlam ** 2) / 12) * (np.cos(fi)) ** 2 * (
                        5 - (t ** 2) + 9 * (ni ** 2) + 4 * (ni ** 4)) + ((dlam ** 4) / 360) * (np.cos(fi) ** 4) * (
                                                                                                  61 - 58 * (t ** 2) + (
                                                                                                      t ** 4) + 270 * (
                                                                                                              ni ** 2) - 330 * (
                                                                                                                      ni ** 2) * (
                                                                                                                      t ** 2)))
            ygk = (dlam * N * np.cos(fi)) * (1 + (((dlam) ** 2 / 6) * (np.cos(fi)) ** 2) * (1 - (t ** 2) + (ni ** 2)) + (
                        (dlam ** 4) / 120) * (np.cos(fi) ** 4) * (5 - 18 * (t ** 2) + (t ** 4) + 14 * (ni ** 2) - 58 * (
                        ni ** 2) * (t ** 2)))
            x92 = xgk * m - 5300000
            y92 = ygk * m + 500000
            wsp.append([x92, y92])
        return wsp

    def cale00(self, fi, lam):
        m = 0.999923
        wsp = []
        for fi, lam in zip(fi, lam):
            lam0 = 0
            strefa = 0
            if np.deg2rad(13.5) < lam < np.deg2rad(16.5):
                strefa = 5
                lam0 = np.deg2rad(15)
            elif np.deg2rad(16.5) < lam < np.deg2rad(19.5):
                strefa = 6
                lam0 = np.deg2rad(18)
            elif np.deg2rad(19.5) < lam < np.deg2rad(22.5):
                strefa = 7
                lam0 = np.deg2rad(21)
            elif np.deg2rad(22.5) < lam < np.deg2rad(25.5):
                strefa = 8
                lam0 = np.deg2rad(24)
            else:
                print("Punkt znajduje się poza strefą odwzorowawczą układu PL_2000")
                continue
            b2 = (self.a ** 2) * (1 - self.e2)
            e2p = (self.a ** 2 - b2) / b2
            dlam = lam - lam0
            t = np.tan(fi)
            ni = np.sqrt(e2p * (np.cos(fi)) ** 2)
            N = self.Npu(fi)
            sigma = self.Sigma(fi)
            xgk = sigma + ((dlam ** 2) / 2) * N * np.sin(fi) * np.cos(fi) * (1 + ((dlam ** 2) / 12) * (np.cos(fi)) ** 2 * (
                        5 - (t ** 2) + 9 * (ni ** 2) + 4 * (ni ** 4)) + ((dlam ** 4) / 360) * (np.cos(fi) ** 4) * (
                                                                                                  61 - 58 * (t ** 2) + (
                                                                                                      t ** 4) + 270 * (
                                                                                                              ni ** 2) - 330 * (
                                                                                                                      ni ** 2) * (
                                                                                                                      t ** 2)))
            ygk = (dlam * N * np.cos(fi)) * (1 + (((dlam) ** 2 / 6) * (np.cos(fi)) ** 2) * (1 - (t ** 2) + (ni ** 2)) + (
                        (dlam ** 4) / 120) * (np.cos(fi) ** 4) * (5 - 18 * (t ** 2) + (t ** 4) + 14 * (ni ** 2) - 58 * (
                        ni ** 2) * (t ** 2)))
            x00 = xgk * m
            y00 = ygk * m + strefa * 1000000 + 500000
            wsp.append([x00, y00])
        return wsp

    def file(self, plik, funkcja):
        data = np.genfromtxt(plik, delimiter=" ")
        if funkcja == "XYZ_BLH":
            X = data[:, 0]
            Y = data[:, 1]
            Z = data[:, 2]
            blh = self.hirvonen(X, Y, Z)
            np.savetxt(f"WYNIK_{funkcja}.txt", blh, delimiter=";", fmt="%.6f")
        elif funkcja == "BLH_XYZ":
            fi = np.deg2rad(data[:, 0])
            lam = np.deg2rad(data[:, 1])
            h = data[:, 2]
            XYZ = self.filh2XYZ(fi, lam, h)
            np.savetxt(f"WYNIK_{funkcja}.txt", XYZ, delimiter=";", fmt="%.6f")
        elif funkcja == "XYZ_NEU":
            X0 = data[0, 0]
            Y0 = data[0, 1]
            Z0 = data[0, 2]
            X = data[1:, 0]
            Y = data[1:, 1]
            Z = data[1:, 2]
            neu = self.xyz2neup(X, Y, Z, X0, Y0, Z0)
            np.savetxt(f"WYNIK_{funkcja}.txt", neu, delimiter=";", fmt="%.6f")
        elif funkcja == "BL_PL1992":
            fi = np.deg2rad(data[:, 0])
            lam = np.deg2rad(data[:, 1])
            wsp92 = self.cale92(fi, lam)
            np.savetxt(f"WYNIK_{funkcja}.txt", wsp92, delimiter=";", fmt="%.6f")
        elif funkcja == "BL_PL2000":
            fi = np.deg2rad(data[:, 0])
            lam = np.deg2rad(data[:, 1])
            wsp00 = self.cale00(fi, lam)
            np.savetxt(f"WYNIK_{funkcja}.txt", wsp00, delimiter=";", fmt="%.6f")

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Podaj plik")
        parser.add_argument("-plik", type=str, help="Podaj nazwę pliku, w którym znajdują się dane wejściowe (ps. oprócz nazwy podaj rozszerzenie:)")
        parser.add_argument("-elip", type=str, help="Wybierz elipsoidę, na której ma wykonać się transformacja, wpisz jedną: 'WGS84', 'GRS80', 'Elipsoida Krasowskiego'")
        parser.add_argument("-funkcja", type=str, help="Wybierz transformację jaką chcesz obliczyć: 'XYZ_BLH', 'BLH_XYZ', 'XYZ_NEU', 'BL_PL1992', 'BL_PL2000'")
        args = parser.parse_args()
    except SyntaxError:
        print(f"Niestety nie ma takiego pliku. Spróbuj podać pełną ścieżkę do pliku lub upewnij się, że wpisujesz dobrą nazwę")
    elip = {'WGS84': [6378137.000, 0.00669438002290], 'GRS80': [6378137.000, 0.00669438002290], 'Elipsoida Krasowskiego': [6378245.000, 0.00669342162296]}
    funkcja = {'XYZ_BLH': 'hirvonen', 'BLH_XYZ': 'filh2XYZ', 'XYZ_NEU': 'xyz2neup', 'BL_PL1992': 'cale92', 'BL_PL2000': 'cale00'}
    try:
        geo = Transformations(elip[args.elip.upper()])
        finito = geo.file(args.plik, args.funkcja.upper())
        print("Zapisano")
    except KeyError:
        print("Podana funkcja/elipsoida nie istnieją, proszę upewnij się, że korzystasz z istniejących elipsoid")
    except AttributeError:
        print("Podana funkcja/elipsoida nie istnieje, proszę wprowadzić dostępne wartości.")
    except FileNotFoundError:
        print("Nie znaleziono takiego pliku. Proszę spróbować wprowadzić inny plik.")
    except IndexError:
        print("Nieodpowiedni format pliku. Proszę wprowadzić dane do pliku tak jak pokazano w przyładzie.")
    except ValueError:
        print("Nieodpowiedni format pliku. Proszę wprowadzić dane do pliku tak jak pokazano w przyładzie.")
