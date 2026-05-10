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
71555, Banasiewicz, Aleksandra: 
72791, Ciarka, Natalia: 
73134, Gawda, Agata: udział w wyborze modeli uczenia maszynowego, przygotowanie danych i wykresów wynikowych, wkład w tworzenie raportu, wkład w opracowanie repozytorium na GitHubie
73185, Kęska, Karolina: udział w wyborze modeli uczenia maszynowego, przygotowanie i trenowanie dwóch modeli predykcyjnych, opracowanie kodu projektu, współtworzenie raportu końcowego, udział w przygotowaniu pytań badawczych oraz analizie wyników, współudział w opracowaniu i organizacji repozytorium projektu na GitHubie
72525, Kołodziejczyk, Milena: 

===PYTANIA BADAWCZE=== 
1. Czy możliwe jest przewidywanie liczebności motyli na podstawie historycznych danych monitoringowych?
2. Które gatunki motyli wykazują najwyższą przewidywaną liczebność w prognozie na rok 2025?
3. Czy analiza trendów pozwala wykryć gatunki o rosnącej lub malejącej liczebności?

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
1. Wstępne oczyszczanie i przygotowanie danych (konwersja dat,usunięcie brakujących wartości,przygotowanie cech czasowych)
2. Feature engineering (utworzenie zmiennej day_of_year, przygotowanie zmiennych kategorycznych)
3. Podział danych na zbiór treningowy i testowy:
- dane przed 2019 rokiem (train),
- dane od 2019 roku (test)
4. Trenowanie modeli uczenia maszynowego (CatBoost, LightGBM)
5. Porównanie modeli przy użyciu metryki MAE (Mean Absolute Error)
6. Wybór najlepszego modelu na podstawie wyników ewaluacji
7. Forecast liczebności motyli na rok 2025
8. Analiza sezonowości występowania motyli
9. Analiza trendów populacyjnych gatunków
10. Wizualizacja wyników oraz interpretacja ekologiczna

===SRODOWISKO=== 
Python version: 3.14
Main libraries: 
- pandas,
- numpy
- matplotlib
- scikit-learn
- LightGBM
- CatBoost
- XGBoost

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
├── outputs/
│ ├── plot.png # wykresy i tabele wynikowe
│ └── data1.csv 
│ └── data2.csv
│ └── data3.csv
│
└── models/
├── lightgbm_model.pkl # model
