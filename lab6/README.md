# Lab 6 MDP (Markov Decision Process)

## Cel
Ćwiczenia z Procesów Decyzyjnych Markova.

## Zadanie
Wumpus prowadzi **dwa** rodzinne sklepy sprzedające magiczne grzyby. Każdego dnia pewna liczba klientów przychodzi do każdego sklepu aby zakupić grzybki. Jeśli w sklepie jest wystarczająca ilość opakowań grzybów, opakowanie takie zostaje sprzedane za **g** cebulionów. Jeśli w sklepie nie ma już grzybów, klient odchodzi z kwitkiem (brak zysku dla Wumpusa).

Każdego wieczora (po obsłużeniu wszystkich klientów) wumpus i pani wumpusowa (obsługuje w drugim sklepie) ścinają swieże grzybki w odpowiednich sklepach (hodują je w piwnicach). Liczby klientów (sprzedanych grzybów) i zebranych grzybów opisane są rozkładen Poissona (wyniki długoletnich obserwacji rodziny wumpusa) tzn. prawdopodobieństwo, że wartość przyjmie n równa jest p(n) = lambda^n/(n!)*exp(-lambda) gdzie lambda jest wartością oczekiwaną rozkładu. Załóż, że wartość oczekiwana liczby gości w sklepach to **L1** i **L2** zaś liczba zebranych opakowań grzybów dla odpowiednich sklepów to **L3** i **L4**.

Niestety w każdym sklepie jest tylko **m** super magicznych pojemników, w których trzeba przechowywać grzyby aby się nie zepsuły - wszelki nadmiar jest zjadany przez rodzinę wumpusa na kolację.

Aby grzyby były dostępne tam i wtedy gdzie jest na nie popyt, wumpus może w nocy przemieścić opakowanie grzybów z jednego sklepu do drugiego. Niestety przeniesienie jednego opakowania kosztuje wumpusa **c** cebulionów. Dodatkowo, ze względu na wysoką aktywność Magicznych Organów Ścigania wumpus może przenosić jedynie **F** opakowań grzybów każdej nocy (przy większej liczbie ucieczka byłaby niemożliwa).

Sformułuj ten problem jako dyskretny proces decyzyjny Markov’a, w którym czas jest mierzony w dniach, stanem jest liczba dostępnych opakowań grzybów w poszczególnych sklepach, a akcją liczba opakowań grzybów do przemieszczenia z pierwszego do drugiego sklepu (wartość ujemna oznacza, że trzeba przemieścić grzyby z drugiego sklepu do pierwszego).

Znajdź rozwiązanie tego problemu: strategię przemieszczania grzybów optymalizującą zysk w cebulionach w przyszłości dla współczynnika dyskontowego **gamma** (czy wiesz, dlaczego musi być mniejszy od 1?) dla każdego stanu (wynikiem jest macierz **m+1** x **m+1**).

Przykładowe rozwiązanie można znaleźć [tutaj](sample_solution.py) (dobry format, złe odpowiedzi).

## Zaliczenie
* Zgłoszenie rozwiązania na platformie [Optil.io](https://www.optil.io/optilion/problem/3168)
* Termin: **przed** zajęciami za **3 tygodnie** - dla grup, którym zajęcia wypadną (święta/godziny rektorskie) spóźnienia naliczane są wedle tygodni kalendarzowych, a każdy tydzień rozpoczyna się wraz z godziną, o której rozpoczęłyby się zajęcia gdyby się odbywały

## Punktacja
* 15 punktów (średnia ze wszystkich instancji)
* **Spóźnienie**: **-20%** za każdy rozpoczęty tydzień.
