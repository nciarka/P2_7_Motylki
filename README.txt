# P2_2_Motylki

===PROJEKT=== 
Numer grupy: 7
Nazwa projektu: Jak zmieniała się liczebność zaobserwowanych motyli w Kalifornii w latach 2000-2016 na podstawie danych monitoringowych?
Opis: Celem projektu jest analiza zmian liczebności motyli w Kalifornii w latach 2000–2016 na podstawie danych monitoringowych.
Projekt ma na celu zidentyfikowanie trendów w czasie oraz porównanie liczebności wybranych gatunków motyli.

## Opis danych
Dane zawierają informacje o liczbie zaobserwowanych motyli w poszczególnych latach oraz dla różnych gatunków.

Kolumny:
- site_name - lokalizacja
- visit_date – data obserwacji
- genus_species – nazwa gatunku motyla
- pa - Presence/Absence (parametr binarny: 1 - gatunek był obecny, 0 - gatunek nie był obecny)
- count – liczba zaobserwowanych osobników
- year - rok obserwacji 
- day - dzień w roku, w któym odbyła się obserwacja


## Metody analizy
W projekcie wykorzystano:
- Python
- bibliotekę pandas (analiza danych)
- bibliotekę matplotlib (wizualizacja)

Wykonane analizy:
- agregacja danych rocznych
- analiza trendu liczebności
- obliczenie zmiany procentowej
- analiza 5 najczęściej występujących gatunków

## Struktura projektu
P2_2_Motylki/
│
├── README.md # opis projektu
├── main.py # główny kod analizy
├── raport.pdf # raport końcowy
├── requirements.txt # wymagane biblioteki
│
├── data/
│ └── data1.csv # dane wejściowe
│
├── src/
│ ├── script1.py # dodatkowy skrypt
│ └── notebook1.ipynb # analiza w Jupyter Notebook
│
└── outputs/
├── plot1.png # wykres wynikowy
└── data1.csv # dane po przetworzeniu
