# Niepewność w świecie Wumpusa

## Cel
Praktyczne zastosowanie rachunku prawdopodobieństwa dla celów AI.

## Zadanie
Napisz program, który wczyta plik zawierający opis środowiska uproszczonego Wumpus’a i dla każdego pola świata wywnioskuje prawdopodobieństwo, że pole zawiera jamę biorąc pod uwagę aktualną wiedzę agenta.


W ten sposób agent aktualizuje swoją wiedzę o stanie środowiska (wnioskuje na temat nieobserwowalnej części świata).

>> Do odpalenia zadania lokalnie  **może** się przydać pakiet [misio](../misio).

## Opis wejścia i wyjścia

* Plik wejściowy rozpoczyna się od **i** ilości instancji do wczytania. Kolejne linie zawierają:
    * liczbę wierszy **n**, liczbę kolumn świata **m**,
    * prawdopodobieńśtwo obecności pułapki dla pola,
    * tablicę o **n** wierszach i **m** kolumnach zawierającą **‘?’** jeśli pole jest nieodwiedzone, **‘B’** jeśli pole jest odwiedzone i agent wyczuł wiatr, **‘O’** jeśli pole jest odwiedzone, ale agent nie wyczuł wiatru.
* Plik wyjściowy zawiera **i** tablic o wielkościach odpowiadających macierzom w pliku wejściowym. Tablice zawierają liczby rzeczywiste oznaczające prawdopodobieńśtwo obecności jamy na danym polu (liczby zaokrąglić do drugiego miejsca po przecinku np. 0.01, 0.20).
* [Przykładowe pliki in/out](test_cases)
* Wynikowe macierze będą porównywane za pomocą funkcji [compare_outputs](../misio/uncertain_wumpus/testing.py#L17)(macierz jest poprawna lub nie), wynik z instancji jest średnia poprawnoscią macierzy pomnożoną przez **15**

## Zaliczenie
* Praca indywidualna.
* Program należy zgłosić na [Optil.io](https://www.optil.io/optilion/problem/3159) (nie ma sprawozdania).
* Program ma **liczyć** poprawny wynik, w przypadku wykrycia programu, który przekleja na sztywno wpisane wartości (np. te z udostpęnionych plików wejściowych) nie zostanie uznany.
* Termin: **przed** kolejnymi zajęciami (planowo tydzień)

## Punktacja
* **15** punktów - średnia z 15 instancji; do części z nich zostały opublikowane pliki wejściowe, a do części nawet pliki wyjściowe, vide [test_cases](test_cases)
* **Spóźnienie**: **-20%** za każdy rozpoczęty tydzień spóźnienia
