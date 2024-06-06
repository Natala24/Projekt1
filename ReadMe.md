PROJEKT NUMER 1 "TRANSFORMACJE WSPÓŁRZĘDNYCH"

PRZEPROWADZONE TRANSFORMACJE:
```sh
    XYZ (geocentryczne) -> BLH (elipsoidalne fi, lambda, h)
    BLH -> XYZ
    XYZ -> NEUp
    BL(GRS80, WGS84, elipsoida Krasowskiego) -> 2000
    BL(GRS80, WGS84, elipsoida Krasowskiego) -> 1992
```
 WYBRANE ELIPOSIDY:
 ```sh
     GRS80
     WGS84
     Elipsoida Krasowskiego
 ```
 WYKORZYSTYWANE NARZĘDZIA PRACY:
 ```sh
    Systemy operacyjne: Windows 11 oraz macOS 12.5.1
    Python oraz importowane biblioteki: numpy oraz argparse
```

OPIS PROGRAMU:
```sh
 Plik przyjmuje argumenty podane za pomocą następujących flag:
 ```

 ```sh
   -plik przyjmuje plik (koniecznie z rozszerzeniem), w którym znajdują się dane potrzebne do wykonania transformacji
   -elip przyjmuje nazwę modelu elipsoidy, na której chcemy dokonać transformacji
   -funkcja przyjmuje nazwę transformacji, którą chcemy wykonać
  ```
  
  WYBÓR ELIPSOIDY:
  ```sh
  Możliwe, jest wtedy, gdy wpiszemy nazwę wybranej przez nas elipsoidy:
  ```
  ```sh
   'WGS84'
   'GRS80'
   'Elipsoida Krasowskiego'
  ```
  
  WYBÓR TRANSFORMACJI:
  ```sh
  Transformację wybieramy, wpisując jedną z poniższych nazw.
  ```
  ```sh
   'XYZ_BLH'
   'BLH_XYZ'
   'XYZ_NEU'
   'BL_PL1992'
   'BL_PL2000'
  ```
  KOMUNIKAT
  ```sh
  Po wybraniu wszystkich parametrów i załadowaniu pliku z przykładowymi danymi, utworzy się plik z wynikami obliczeń w formacie txt.
```
  ```sh
   Zapisano
  ```
 NAZWA ZAPISANEGO PLIKU:
  ```sh
  "WYNIK_{funkcja}.txt"
  (gdzie {funkcja} oznacza nazwę transformacji, którą chcemy wykonać)
  ```
  
  PRZYKŁADOWE WYWOŁANIA PROGRAMU:
  ```sh
    -> python skrypt.py -plik dane.txt -elip GRS80 -funkcja XYZ_BLH
    -> python skrypt.py -plik dane.txt -elip WGS84 -funkcja BL_PL1992
    -> python skrypt.py -plik dane.txt -elip Elipsoida Krasowskiego -funkcja BL_XYZ
    -> python skrypt.py -plik dane.txt -elip WGS84 -funkcja XYZ_NEU
  ```
  
  
  PRZYKŁADOWE TRANSFORMACJE:
  
  XYZ ---> BLH
  ```sh
  Dla danych z pliku (kolejno X[m], Y[m], Z[m]) otrzymujemy wyniki (w kolejno w pierwszym wierszu fi1, l1, h1 w kolejnej kolumnie  fi2, l2, h2, [stopnie dziesiętn]) itd... 
  ```

  
  BLH ---> XYZ
 ```sh
 Plik wejściowy dla BL [stopnie dziesiętn] dla H [m]
  Dla danych z przykładowego pliku, otrzymujemy wyniki (kolejno X[m], Y[m], Z[m])
  ```
  
  
  XYZ, X0Y0Z0 ---> NEU  (kolejno fi, lambda, h[stopnie dziesiętn])
  ```sh
Po przeprowadzeniu transformacji, otrzymujemy następujące wartości ( kolejno : N, E, U[stopnie, minuty, sekundy])
```
Ważne jest, aby współrzędne punktów podane zostały w odpowiedniej kolejności - jako pierwsze podać należy współrzędne początku układu NEU (x0, y0), a dopiero potem współrzędne, do których policzyć chcemy wektor. Stąd, żeby otrzymać jeden punkt wyjściowy należy wprowadzić dane aż dwóch punktów wejściowych.

BL ---> XY PL1992 dla danych z pliku 'BL_PL1992.txt' (kolejno fi, lambda [stopnie dziesiętn])
```sh
Kolejną transfomacją, która będzie wykonana jest przeliczenie współrzędnych geodezyjnech do układu współrzędnych 1992. Otrzymujemy wyniki (kolejno X92[m],Y92[m])
 ``` 
 
BL ---> XY PL2000 (kolejno fi, lambda [stopnie dziesiętn])
```sh
Dla danych z pliku, otrzymujemy wyniki (kolejno x2000[m], y2000[m])
 ```
  

 
