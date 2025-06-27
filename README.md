**Analiza danych lotniczych z USA (2015)** / **Analysis of US air data in 2015**

Projekt oparty na danych o lotach z amerykańskich lotnisk w 2015 roku. Celem było przetworzenie i analiza dużego zbioru danych w sposób skalowalny oraz przedstawienie wyników w formie wizualizacji.

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

---------------------ENG-----------------------

Project based on flight data from American airports in 2015. The goal was to process and analyze a large dataset in a scalable way and present the results in the form of visualizations.

Analysis scope:

The following analyses were carried out in the project:

- Calculation of the average flight distance
- Calculation of the average departure and arrival delay by airline
- Calculation of the airline cancellation rate
- Verification and assessment of the accuracy of airline data

Technologies:

- Python
- `mrjob` (MapReduce)
- `pandas`, `plotly`, `matplotlib` – for data analysis and visualization
- Jupyter Notebook – for presentation of results

Data:

The data source was public data on flights in the USA from 2015, containing, among others:
- flight date, flight number, airlines, delays for various reasons, distance, status, etc.
