# P3_7_Motylki

===PROJEKT=== 
Numer grupy: 7
Nazwa projektu: Przewidzenie liczebności motyli w Kalifornii w 2025 roku (forecast) na podstawie danych monitoringowych z 2000-2016?
Opis: Celem projektu jest przewidywanie liczebności motyli (count) na podstawie historycznych danych 
ekologicznych.

===GRUPA=== 
Lab grupa, ID, Nazwisko, Imie 
7, 71555, Banasiewicz, Aleksandra
7, 72791, Ciarka, Natalia 
7, 73134, Gawda, Agata 
7, 73185, Kęska, Karolina
7, 72525, Kołodziejczyk, Milena

===WKLAD=== 
ID, Nazwisko, Imie: Krótki opis wkładu każdego studenta do grupowego projektu na tym etapie. 
71555, Banasiewicz, Aleksandra: wkład w przygotowanie raportu, wkład w opracowanie repozytorium na GitHubie
72791, Ciarka, Natalia: stworzenie i wkład w przygotowanie repozytorium na GitHubie, wkład w przygotowanie raportu
73134, Gawda, Agata: przygotowanie i wybór źródła danych, napisanie skryptu do pobrania zestawu danych, wkład w przygotowanie skryptu do analizy eksploracyjnej oraz wizualizacji danych, wkład w tworzenie raportu, wkład w opracowanie repozytorium na GitHubie
73185, Kęska, Karolina: zaproponowanie i przedstawienie koncepcji tematu projektu, wkład w przygotowanie raportu, wkład w przygotowanie pytań badawczych i ich analizy, wkład w opracowanie repozytorium na GitHubie
72525, Kołodziejczyk, Milena: wkład w przygotowanie raportu, wkład w opracowanie repozytorium na GitHubie

===PYTANIA BADAWCZE=== 
1. Czy obserwowany trend liczebności motyli ma charakter rosnący, malejący czy zmienny w czasie?
2. Czy najczęściej występujące gatunki motyli wykazują podobne trendy zmian liczebności, czy różnią się między sobą?
3. Które z analizowanych gatunków odnotowały największe zmiany liczebności w badanym okresie?

===ZRODLA DANYCH=== 
=1= 
Nazwa zrodla: Github
Nazwa danych: Monitoring Western Butterflies: Count Data
Dataset URL: https://github.com/zgompert/MontaneButterfliesLTREB/raw/refs/heads/master/Shapiro_Counts.csv.gz

===ZMIENNE=== 
Dane wejściowe (input):
- site_name - lokalizacja obserwcji
- genus_species – nazwa gatunku motyla
- year - rok obserwacji 
- month — miesiąc obserwacji
- day - dzień w roku, w któym odbyła się obserwacja

Dane wyjściowe (output):
- count – liczba zaobserwowanych osobników  

===ANALIZA=== 
1. Agregacja danych do poziomu rocznego w celu określenia całkowitej liczebności motyli w poszczególnych latach
2. Analiza trendu liczebności motyli w czasie na podstawie danych zagregowanych
3. Obliczenie procentowej zmiany liczebności motyli między rokiem 2000 a 2016 (dla całej populacji motyli oraz dla 5 najpopularniejszych gatunków)
4. Analiza zmian liczebności dla 5 najczęściej występujących gatunków motyli
5. Analiza regresji liniowej
6. Obliczenie współczynnika zmienności dla poszczególnych gatunków motyli

===SRODOWISKO=== 
Python version: 3.14
Main libraries: pandas==3.0.2, matplotlib==3.10.8, numpy==2.4.3

===ZAWARTOSC=== 
P3_7_Motylki
│
├── README.md # opis projektu
├── main.py # główny kod analizy
├── Raport_P3.pdf # raport końcowy fo etapu 3
├── requirements.txt # wymagane biblioteki
│
├── data/
│ └── data1.csv # dane wejściowe
│
├── src/
│ ├── Forecast.ipynb # przetrenowany model
│
└── outputs/
├── plot.csvpng # wykresy i tabele wynikowe
└── data1.csv.gz # dane po przetworzeniu
│
└── models/
├── lightgbm_model.pkl # model
