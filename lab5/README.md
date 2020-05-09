# Lab 5 MDP (Markov Decision Process)

## Cel
Ćwiczenie z Procesów Decyzyjnych Markova.

## Zadanie
Wumpus prowadzi **dwa** rodzinne sklepy sprzedające magiczne grzyby. Każdego dnia do sklepów przychodzą klienci by kupić grzyby (1 klient - 1 grzyb). Jeśli w sklepie jest wystarczająca liczba grzybów, każdy grzyb zostaje sprzedany za **g** wumpusodolarów. Jeśli popyt jest większy niż dostępna liczba grzybów, zostają sprzedane tylko dostępne grzyby. Jeśli popyt jest mniejszy, część grzybów zostaje niesprzedana.

Każdego wieczora (po obsłużeniu wszystkich klientów) wumpus i pani wumpusowa (obsługuje w drugim sklepie) ścinają swieże grzyby w odpowiednich sklepach (hodują je w piwnicach). Liczba klientów i zebranych grzybów  (danego dnia) opisane są rozkładem Poissona (wyniki długoletnich obserwacji rodziny wumpusa) tzn. prawdopodobieństwo, że wartość przyjmie **n** równa jest p(n) = lambda^n/(n!)*exp(-lambda) gdzie lambda jest wartością oczekiwaną rozkładu. Załóż, że wartość oczekiwana liczby gości w sklepach to **L1** i **L2** zaś liczba zebranych grzybów dla odpowiednich sklepów to **L3** i **L4**.

Niestety w każdym sklepie jest tylko **m** super magicznych pojemników, w których trzeba przechowywać grzyby aby się nie zepsuły - wszelki nadmiar jest zjadany przez rodzinę wumpusa na kolację.

Aby grzyby były dostępne tam i wtedy gdzie jest na nie popyt, wumpus może w nocy przemieścić grzyby z jednego sklepu do drugiego (po kolacji). Niestety przeniesienie jednego grzyba kosztuje wumpusa **c** wumpusodolarów (specjalne materiały zabezpieczające). Dodatkowo, ze względu na ograniczoną pojemność super-magicznej torby wumpus może przenosić jedynie **F**  grzybów każdej nocy. Jeżeli po przeniesieniu w danych sklepie jest więcej niż **m** grzybów, nadmiar jest zjadany i nie może być sprzedany następnego dnia.

Sformułuj ten problem jako dyskretny proces decyzyjny Markov’a, w którym czas jest mierzony w dniach, stanem jest liczba dostępnych grzybów w poszczególnych sklepach, a akcją liczba grzybów do przemieszczenia z pierwszego do drugiego sklepu (wartość ujemna oznacza, że trzeba przemieścić grzyby z drugiego sklepu do pierwszego). 

Znajdź rozwiązanie tego problemu: strategię przemieszczania grzybów optymalizującą zysk w wumpusodolarach w przyszłości dla współczynnika dyskontowego **gamma** (czy wiesz, dlaczego musi być mniejszy od 1?) dla każdego stanu (wynikiem jest macierz **m+1** x **m+1**).

Przykładowe rozwiązanie można znaleźć [tutaj](sample_solution.py) (dobry format, złe odpowiedzi). Przykładowe [wejście](sample_testcase.in) i [wyjście](sample_testcase.out) (poprawny wynik). "Sample output" z otpill.io to wartośći losowe prezentujące poprawny format.

## Zaliczenie
* Zgłoszenie rozwiązania na platformie [Optil.io](https://www.optil.io/optilion/problem/3168)
* Termin: **przed** zajęciami za **2 tygodnie** - dla grup, którym zajęcia wypadną (święta/godziny rektorskie) spóźnienia naliczane są wedle tygodni kalendarzowych, a każdy tydzień rozpoczyna się wraz z godziną, o której rozpoczęłyby się zajęcia gdyby się odbywały.

## Punktacja
* 15 punktów (średnia ze wszystkich instancji)
* **Spóźnienie**: **-20%** za każdy rozpoczęty tydzień.
