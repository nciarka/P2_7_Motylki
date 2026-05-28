# P4_2_Motylki

===PROJEKT=== 
Numer grupy: 7
Nazwa projektu: Jak zmieniała się liczebność zaobserwowanych motyli w Kalifornii w latach 2000-2016 na podstawie danych monitoringowych?
Opis: Celem projektu jest analiza zmian liczebności motyli w Kalifornii w latach 2000–2016 na podstawie danych monitoringowych.
Projekt ma na celu zidentyfikowanie trendów w czasie oraz porównanie liczebności wybranych gatunków motyli.

===GRUPA=== 
Lab grupa, ID, Nazwisko, Imie 
7, 71555, Banasiewicz, Aleksandra
7, 72791, Ciarka, Natalia 
7, 73134, Gawda, Agata 
7, 73185, Kęska, Karolina
7, 72525, Kołodziejczyk, Milena

===WKLAD=== 
ID, Nazwisko, Imie: Krótki opis wkładu każdego studenta do grupowego projektu na tym etapie. 
71555, Banasiewicz, Aleksandra: 
72791, Ciarka, Natalia: 
73134, Gawda, Agata: 
73185, Kęska, Karolina: 
72525, Kołodziejczyk, Milena: 

===PYTANIA BADAWCZE=== 
1. Czy możliwe jest przewidywanie liczebności motyli na podstawie historycznych danych monitoringowych?
2. Które gatunki motyli wykazują najwyższą przewidywaną liczebność w prognozie na rok 2025?
3. Czy analiza trendów pozwala wykryć gatunki o rosnącej lub malejącej liczebności?

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


===SRODOWISKO=== 
Python version: 3.14
Main libraries: 

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
