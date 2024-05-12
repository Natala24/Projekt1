Projekt 1 - Transformacje

PRZEPROWADZONE TRANOSFORMACJE:
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

OPIS PROGRAMU
 Plik przyjmuje argumenty podane za pomocą następujących flag:
 ```sh
   -plik przyjmuje plik (koniecznie z rozszerzeniem), w którym znajdują się dane potrzebne do wykonania transformacji
   -elip przyjmuje nazwę modelu elipsoidy, na której chcemy dokonać transformacji
   -funkcja przyjmuje nazwę transformacji, którą chcemy wykonać
  ```
  
  WYBÓR ELIPSOIDY MOŻLIWY JEST POPRZEZ WPISANIE JEDNEJ Z PONIŻSZYCH NAZWY:
  ```sh
   'WGS84'
   'GRS80'
   'Elipsoida Krasowskiego'
  ```
  
  WYBÓR TRANSFORMACJI MOŻLIWY JEST POPRZEZ WPISANIE JEDNEJ Z PONIŻSZYCH NAZW:
  ```sh
   'XYZ_BLH'
   'BLH_XYZ'
   'XYZ_NEU'
   'BL_PL1992'
   'BL_PL2000'
  ```
  
  PO WYBORZE PARAMETRÓW I ZAŁADOWANIU PLIKU Z DANYMI UTWORZY SIĘ PLIK TEKSTOWY ZAWIERAJĄCY WYNIKI WYKONANYCH OBLICZEŃ, A NA KONSOLI POJAWIĄ SIĘ KOMUNIKATY:
  ```sh
   Zapisano
  ```
  Pliku wynikowy zapisuje się pod nazwą:
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
  
  
  PRZYKŁADOWE TRANSFORMACJE
  
  XYZ ---> BLH
  dla danych z pliku (kolejno X[m], Y[m], Z[m])
  ```sh
  12345.789 65789.003 36674.123
  11111.222 22222.343 55555.332
  ```
  otrzymujemy wyniki (w kolejnych linijkach fi1, l1, h1, fi2, l2, h2, ...)
  ```sh
    5.209727221932659802e+01
    2.103153333279777115e+01
    1.413986623901873827e+02
    5.209727216202450961e+01
    2.103153314423015274e+01
    1.413998245187103748e+02
    5.209727212128520080e+01
    2.103153295566253433e+01
    1.414033538121730089e+02
    5.209727208606682325e+01
    2.103153276709491948e+01
    1.414076721612364054e+02
    5.209727208694960154e+01
    2.103153322806154435e+01
    1.414101303610950708e+02
    5.209727211984851181e+01
    2.103153317776271081e+01
    1.414022109359502792e+02
    5.209727206994543280e+01
    2.103153299757823191e+01
    1.414065340962260962e+02
    5.209727206155152146e+01
    2.103153280586428764e+01
    1.414110632874071598e+02
    5.209727212004385422e+01
    2.103153325424560194e+01
    1.414072633692994714e+02
    5.209727213641129140e+01
    2.103153317776271081e+01
    1.414045780999585986e+02
    5.209727210179833179e+01
    2.103153332234535000e+01
    1.414075766596943140e+02
    5.209727215407200163e+01
    2.103153318299952090e+01
    1.414055828107520938e+02
      ```
  
  BLH ---> XYZ
  dla danych z pliku (kolejno fi, lambda, h)
  ```sh
  52 21 319
  52 19 420
  ```
  otrzymujemy wyniki (kolejno X[m], Y[m], Z[m])
  ```sh
  3.673785422237344086e+06   1.410234096034315648e+06   5.003054720799141563e+06
  3.720822705660262145e+06   1.281182001713992795e+06   5.003134309885255992e+06
  ```
  
  XYZ,X0Y0Z0 ---> neu
  dla danych z pliku 'wsp_XYZ_NEU.txt' (kolejno fi, lambda h,)
  ```sh
   7.221181885654304642e+05
  -2.477294595237924659e+05 
  -1.045556128732857667e+07
  ```
  otrzymujemy wyniki (kolejno n, e, u)
  
  Ważne jest, aby współrzędne punktów podane zostały w odpowiedniej kolejności - jako pierwsze podać należy współrzędne początku układu NEU (x0, y0), a dopiero potem współrzędne, do których policzyć chcemy wektor. Stąd, żeby otrzymać jeden punkt wyjściowy należy wprowadzić dane aż dwóch punktów wejściowych.
  
  BL ---> XY PL1992
  dla danych z pliku 'bl-pl.txt' (kolejno fi, lambda)
  ```sh
  52  21
  52  17
  ```
  otrzymujemy wyniki (kolejno x92[m], y92[m])
  ```sh
  4.611972433942528442e+05   6.372531611049008789e+05
  4.611972433942528442e+05   3.627468388950995868e+05
  ```
  
  BL ---> XY PL2000
  dla danych z pliku 'bl-pl.txt' (kolejno fi, lambda)
  ```sh
  52  21
  52  17
  ```
  otrzymujemy wyniki (kolejno x00[m], y00[m])
  ```sh
  5.762899772909278050e+06   7.500000000000000000e+06
  5.763372029424777254e+06   6.431328112376346253e+06
  ```
   

 
