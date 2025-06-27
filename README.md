**3 analizy:**

1) **Analiza danych lotniczych z USA (2015)** / **Analysis of US air data in 2015**
2) **Analiza danych o kursach taxi w NY (2016)** / **Analysis of taxi ride data in NY (2016)**,
3) **Analiza recenzji restauracji klientów** / **Analysis of customer restaurant reviews**


**1)** Projekt oparty na danych o lotach z amerykańskich lotnisk w 2015 roku. Celem było przetworzenie i analiza dużego zbioru danych w sposób skalowalny oraz przedstawienie wyników w formie wizualizacji.

Zakres analizy:

W projekcie zostały przeprowadzone następujące analizy:

- Obliczenie średniego dystansu lotów
- Obliczenie średniego opóźnienia odlotu i przylotu według danej linii lotniczej
- Obliczenie wskaźnika anulowania lotu przez linie lotnicze
- Weryfikacja i ocena dokładności danych linii lotniczych

Technologie:

- Python
- `mrjob` (MapReduce)
- `pandas`, `plotly`, `matplotlib` – do analizy i wizualizacji danych
- Jupyter Notebook – do prezentacji wyników

Dane:

Źródłem danych były dane publiczne o lotach w USA z 2015 roku, zawierające m.in.:
- datę lotu, numer lotu, linie lotnicze, opóźnienia z różych powodów, dystans, status itp.

2) **Analiza danych kursów taxi z 2016 z NY**

Projekt oparty na danych przejazdów amerykańskich taxi w 2016 roku. Celem było przetworzenie i analiza dużego zbioru danych w sposób skalowalny oraz przedstawienie wyników w formie wizualizacji.

Zakres analizy:
- Obliczenie ilości przejazdów według operatora
- obliczenie średniej ilości pasażerów na jeden kurs
- Znalezienie najpopularniejszej przybliżonej lokalizacji odbioru klientów
- Rozkład najpopularniejszych godzin sięgania po usługę
- Średni dystans kursu

Technologie:

- Python
- `mrjob` (MapReduce)
- `pandas`, `plotly`, `matplotlib` – do analizy i wizualizacji danych
- Jupyter Notebook – do prezentacji wyników

Dane:

Źródłem danych były dane publiczne o kursach taxi w USA z 2016 roku, zawierające m.in.:
- nazwę, numer przewoźnika, datę, lokalizację, godzinę odbioru i destynacji, liczbę pasażerów na kurs, wskaźnik notowania, wielkość napiwku itp.


**3)Analiza recenzji klientów usług gastronomicznych**

Projekt oparty na zbiorze danych Amazon Food Reviews. Celem było zidentyfikowanie najczęściej używanych przymiotników w recenzjach z oceną 1 oraz 5, z wykorzystaniem przetwarzania danych w stylu MapReduce (Python, mrjob) i podstawowego NLP.

Zakres analizy:
- Oczyszczanie danych tekstowych – usuwanie znaków specjalnych, stopwordów, lematyzacja
- Analiza części mowy (POS tagging) – filtrowanie tylko przymiotników (JJ)
- MapReduce:
  - zmapowanie przymiotników względem oceny (Score)
  - policzenie częstotliwości słów
  -	wyodrębnienie 20 najczęściej występujących przymiotników dla ocen 1 i 5
  
  
Technologie
  -	Python
  -	mrjob (MapReduce)
  -	NLTK (lemmatyzacja, stopwords, pos_tag)
  -	re (czyszczenie tekstu)




---------------------ENG-----------------------

**3 analyses:
1) **Analysis of US air data in 2015**
2) **Analysis of taxi ride data in NY (2016)**,
3) **Analysis of customer restaurant reviews**

**1)** Project based on flight data from US airports in 2015. The goal was to process and analyze a large dataset in a scalable way and present the results in the form of visualizations.

Scope of analysis:

The following analyses were carried out in the project:

- Calculation of average flight distance
- Calculation of average departure and arrival delay by airline
- Calculation of flight cancellation rate by airlines
- Verification and assessment of the accuracy of airline data

Technologies:

- Python
- `mrjob` (MapReduce)
- `pandas`, `plotly`, `matplotlib` – for data analysis and visualization
- Jupyter Notebook – for presentation of results

Data:

The source of the data was public data on flights in the USA from 2015, containing, among others:
- flight date, flight number, airlines, delays for various reasons, distance, status, etc.

2) **Analysis of taxi ride data from 2016 from NY**

The project is based on data from American taxi rides in 2016. The goal was to process and analyze a large dataset in a scalable way and present the results in the form of visualizations.

Scope of the analysis:

- Calculation of the number of trips by operator
- Calculation of the average number of passengers per trip
- Finding the most popular approximate pickup location for customers
- Distribution of the most popular times to reach for the service
- Average trip distance

Technologies:

- Python
- `mrjob` (MapReduce)
- `pandas`, `plotly`, `matplotlib` – for data analysis and visualization
- Jupyter Notebook – for presentation of results

Data:

The source of the data was public data on taxi trips in the USA from 2016, containing, among others:
- name, carrier number, date, location, pickup time and destination, number of passengers per trip, rating indicator, tip size, etc.

**3) Analysis of customer reviews of food services**

The project is based on the Amazon Food Reviews dataset. The goal was to identify the most frequently used adjectives in reviews with ratings of 1 and 5, using MapReduce-style data processing (Python, mrjob) and basic NLP.

Analysis scope:
- Text data cleaning – removing special characters, stopwords, lemmatization
- Part-of-speech analysis (POS tagging) – filtering only adjectives (JJ)
- MapReduce:
- mapping adjectives to rating (Score)
- counting word frequency
- extracting the 20 most frequently occurring adjectives for ratings 1 and 5

Technologies
- Python
- mrjob (MapReduce)
- NLTK (lemmatization, stopwords, pos_tag)
- re (text cleaning)