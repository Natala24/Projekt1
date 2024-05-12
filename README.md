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
  Dla danych z pliku (kolejno X[m], Y[m], Z[m]) otrzymujemy wyniki (w kolejnych linijkach fi1, l1, h1, fi2, l2, h2, ...)
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
  Dla danych z przykładowego pliku, otrzymujemy wyniki (kolejno X[m], Y[m], Z[m])
  ```sh
    3.519148476177780423e+06;-8.058846240752805956e+06;7.221782633644362912e+06
    3.518246811368130147e+06;-8.060617148406046443e+06;7.220251167392918840e+06
    3.517344529170780908e+06;-8.062387742863076739e+06;7.218719484124908224e+06
    3.516441628994218074e+06;-8.064158022301887162e+06;7.217187582870155573e+06
    3.520158619975043926e+06;-8.061159468966477551e+06;7.218719486032334156e+06
    3.519011511451998260e+06;-8.060834155242622830e+06;7.219638519677306525e+06
    3.518300408910815138e+06;-8.062658984539208002e+06;7.217953559884781018e+06
    3.517155899965156335e+06;-8.064259403564777225e+06;7.216727970327695832e+06
    3.519906124335436150e+06;-8.060581254222247750e+06;7.219485354949392378e+06
    3.519011512378350366e+06;-8.060834157364573330e+06;7.219638521584975533e+06
    3.520609529018185567e+06;-8.060274053074301220e+06;7.219485354313515127e+06
    3.518961021663734689e+06;-8.060718500659395941e+06;7.219791687940459698e+06
  ```
  
  XYZ,X0Y0Z0 ---> NEU
  Dla danych z pliku, otrzymujemy wyniki (kolejno n, e, u)
  
Ważne jest, aby współrzędne punktów podane zostały w odpowiedniej kolejności - jako pierwsze podać należy współrzędne początku układu NEU (x0, y0), a dopiero potem współrzędne, do których policzyć chcemy wektor. Stąd, żeby otrzymać jeden punkt wyjściowy należy wprowadzić dane aż dwóch punktów wejściowych.
  
  BL ---> XY PL1992
  Dla danych z pliku, otrzymujemy wyniki (kolejno x92[m], y92[m])
  BL ---> XY PL2000

 Następnie otrzymujemy wyniki (kolejno x00[m], y00[m])
  ```sh

  ```
   

 
