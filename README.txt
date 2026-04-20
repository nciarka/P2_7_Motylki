# P2_2_Motylki

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
71555, Banasiewicz, Aleksandra: wkład w przygotowanie raportu, wkład w opracowanie repozytorium na GitHubie
72791, Ciarka, Natalia: stworzenie i wkład w przygotowanie repozytorium na GitHubie, wkład w przygotowanie raportu
73134, Gawda, Agata: przygotowanie i wybór źródła danych, wkład w przygotowanie skryptu do analizy eksploracyjnej oraz wizualizacji danych, wkład w tworzenie raportu, wkład w opracowanie repozytorium na GitHubie
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
1. Agregacja danych do poziomu rocznego w celu określenia całkowitej liczebności motyli w poszczególnych latach
2. Analiza trendu liczebności motyli w czasie na podstawie danych zagregowanych
3. Obliczenie procentowej zmiany liczebności motyli między rokiem 2000 a 2016
4. Analiza zmian liczebności dla 5 najczęściej występujących gatunków motyli

===SRODOWISKO=== 
Python version: 3.14
Main libraries: pandas==3.0.2, matplotlib==3.10.8

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
