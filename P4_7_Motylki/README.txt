# P4_2_Motylki

===PROJEKT=== 
Numer grupy: 7
Nazwa projektu: Klasyfikacja trendu liczebności motyli w Kalifornii w 2025 roku na podstawie danych monitoringowych z 2000-2016 z 
wykorzystaniem modelu DistilBERT.
Opis: Celem projektu było przygotowanie prostego modelu klasyfikacyjnego, który na podstawie danych dotyczących liczebności gatunków 
motyli przewiduje kierunek zmiany populacji w latach 2000–2016. 

===GRUPA=== 
Lab grupa, ID, Nazwisko, Imie 
7, 71555, Banasiewicz, Aleksandra
7, 72791, Ciarka, Natalia 
7, 73134, Gawda, Agata 
7, 73185, Kęska, Karolina
7, 72525, Kołodziejczyk, Milena

===WKLAD=== 
ID, Nazwisko, Imie: Krótki opis wkładu każdego studenta do grupowego projektu na tym etapie. 
71555, Banasiewicz, Aleksandra: Weryfikacja czytelności raportu.
72791, Ciarka, Natalia: 
73134, Gawda, Agata: Wkład w tworzenie raportu i repozytorium na githubie, udział w wyborze modelu oraz przygotowaniu danych wynikowych
73185, Kęska, Karolina: Wkład w tworzenie raportu i repozytorium na githubie
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
W projekcie przetestowano dwa różne podejścia:
* klasyczny model machine learning oparty na danych tabelarycznych — LightGBM,
* model Transformer wykorzystujący DistilBERT z biblioteki Hugging Face.

Model LightGBM osiągnął lepsze wyniki w zadaniu prognozowania liczebności motyli. Dane wykorzystane w projekcie miały głównie charakter 
liczbowy i tabelaryczny, dlatego model LightGBM lepiej radził sobie z analizą zależności pomiędzy gatunkami, sezonowością oraz cechami 
czasowymi.
Model DistilBERT został wykorzystany jako eksperymentalne podejście oparte na architekturze Transformer. Pomimo uzyskania stosunkowo 
wysokiej accuracy (~82%), szczegółowa analiza wykazała problemy związane z niezbalansowaniem klas oraz trudności w poprawnym rozpoznawaniu 
klasy „increasing”.
Przeprowadzone eksperymenty pokazały, że klasyczne modele gradient boosting mogą osiągać lepsze wyniki niż modele Transformer w przypadku 
danych ekologicznych o strukturze tabelarycznej.

===SRODOWISKO=== 
Python version: 3.14
Main libraries: 
pandas
numpy
matplotlib
scikit-learn
transformers
datasets
torch
evaluate

===ZAWARTOSC=== 
P4_7_Motylki
│
├── README.md # opis projektu
├── raport.pdf # raport końcowy
│
├── src/
│ └── hugging_face_train.py # dane oraz dzialanie
│
└── outputs/
  └── results.png # screenshot z wynikiem dzialania nr. 1
  └── result2.png # screenshot z wynikiem dzialania nr. 2
