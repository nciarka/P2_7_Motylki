# P2_2_Motylki

===PROJEKT=== 
Numer grupy: 7
Nazwa projektu: Jak zmieniała się liczebność zaobserwowanych motyli w Kalifornii w latach 2000-2016 na podstawie danych monitoringowych?
Opis: Celem projektu jest analiza zmian liczebności motyli w Kalifornii w latach 2000–2016 na podstawie danych monitoringowych.
Projekt ma na celu zidentyfikowanie trendów w czasie oraz porównanie liczebności wybranych gatunków motyli.

===GRUPA=== 
Lab grupa, ID, Nazwisko, Imie 
7, , Banasiewicz, Aleksandra
7, 72791, Ciarka, Natalia 
7, 73134, Gawda, Agata 
7, , Kęska, Karolina
7, , Kołodziejczyk, Milena

===WKLAD=== 
ID, Nazwisko, Imie: Krótki opis wkładu każdego studenta do grupowego projektu na tym etapie. 
73134, Gawda, Agata: przygotowanie i wybór źródła danych, wkład w przygotowanie skryptu do analizy eksploracyjnej oraz wizualizacji danych, 
wkład w tworzenie raportu, wkład w opracowanie repozytorium na githubie

===PYTANIA BADAWCZE=== 
1. 
2. 
3. 

===ZRODLA DANYCH=== 
=1= 
Nazwa zrodla: Github
Nazwa danych: Monitoring Western Butterflies: Count Data
Dataset URL: https://github.com/zgompert/MontaneButterfliesLTREB/blob/master/Shapiro_Counts.csv.gz

===ZMIENNE=== 
- site_name - lokalizacja
- visit_date – data obserwacji
- genus_species – nazwa gatunku motyla
- pa - Presence/Absence (parametr binarny: 1 - gatunek był obecny, 0 - gatunek nie był obecny)
- count – liczba zaobserwowanych osobników
- year - rok obserwacji 
- day - dzień w roku, w któym odbyła się obserwacja

===ANALIZA=== 
1. 
2. 
3. 

===SRODOWISKO=== 
Python version: 3.14
Main libraries: pandas==3.0.2, matplotlib==3.10.8

Wykonane analizy:
- agregacja danych rocznych
- analiza trendu liczebności
- obliczenie zmiany procentowej
- analiza 5 najczęściej występujących gatunków

===ZAWARTOSC=== 
P2_7_Etap2/
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
