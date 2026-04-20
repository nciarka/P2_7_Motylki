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
1. Jakie czynniki mogą potencjalnie wpływać na zaobserwowane zmiany liczebności motyli?
2. Czy wyniki sugerują pogorszenie warunków środowiskowych dla motyli?
3. Dlaczego niektóre gatunki radzą sobie lepiej niż inne?

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
1. Zaobserwowane zmiany liczebności motyli mogą wynikać z wielu czynników środowiskowych. Do najważniejszych należą zmiany klimatyczne (np. temperatura, opady), utrata siedlisk związana z działalnością człowieka (urbanizacja, rolnictwo), a także dostępność roślin żywicielskich. Wahania liczebności mogą być również efektem naturalnej zmienności populacji oraz warunków pogodowych w poszczególnych latach.
2. Ogólny spadek liczebności motyli w analizowanym okresie (około 44,7%) może sugerować pogorszenie warunków środowiskowych. Należy jednak zaznaczyć, że dane wykazują duże wahania między latami, co utrudnia jednoznaczną ocenę. Wyniki mogą wskazywać na negatywne trendy, ale wymagają dalszych analiz oraz uwzględnienia dodatkowych czynników środowiskowych.
3. Zróżnicowane trendy wśród poszczególnych gatunków mogą wynikać z ich odmiennych wymagań środowiskowych oraz zdolności adaptacyjnych. Niektóre gatunki są bardziej odporne na zmiany środowiska i lepiej przystosowują się do warunków zmienionych przez działalność człowieka. Inne, bardziej wyspecjalizowane gatunki, mogą być wrażliwe na zmiany siedlisk i dostępność pokarmu, co prowadzi do spadków ich liczebności.
4. Widoczne w danych nagłe wzrosty liczebności w niektórych latach mogą wynikać z krótkoterminowo sprzyjających warunków środowiskowych, takich jak korzystna pogoda lub zwiększona dostępność pożywienia. Możliwe jest również, że są one częściowo efektem zmienności w sposobie zbierania danych.

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
