# Niepewność w świecie Wumpusa

## Cel
Praktyczne zastosowanie rachunku prawdopodobieństwa dla celów AI.

## Zadanie
Napisz program, który wczyta plik zawierający opis środowiska uproszczonego Wumpus’a i dla każdego pola świata wywnioskuje prawdopodobieństwo, że pole zawiera jamę biorąc pod uwagę aktualną wiedzę agenta.


W ten sposób agent aktualizuje swoją wiedzę o stanie środowiska (wnioskuje na temat nieobserwowalnej części świata).

>> Do odpalenia zadania lokalnie potrzebne jest zainstalowanie pakietu [misio](misio).

## Opis wejścia i wyjścia

* Plik wejściowy rozpoczyna się od **i** ilości instancji do wczytania. Kolejne linie zawierają:
    * liczbę wierszy **n**, liczbę kolumn świata **m**,
    * prawdopodobieńśtwo obecności pułapki dla pola,
    * tablicę o **n** wierszach i **m** kolumnach zawierającą **‘?’** jeśli pole jest nieodwiedzone, **‘B’** jeśli pole jest odwiedzone i agent wyczuł wiatr, **‘O’** jeśli pole jest odwiedzone, ale agent nie wyczuł wiatru.
* Plik wyjściowy zawiera **i** tablic o wielkościach odpowiadających macierzom w pliku wejściowym. Tablice zawierają liczby rzeczywiste oznaczające prawdopodobieńśtwo obecności jamy na danym polu (liczby zaokrąglić do drugiego miejsca po przecinku np. 0.01, 0.20).
* [Przykładowe pliki in/out](test_cases)


## Zaliczenie
* Praca indywidualna.
* Program należy zgłosić na [Optil.io](https://www.optil.io/optilion/author/problem/3159).
* Termin: **godzina przed** kolejnymi zajęciami (planowo tydzień)

## Punktacja
* **15** punktów: **12**\*poprawność + **3**\*szybkość wykonania
* **10 pkt** + ewentualne punkty bonusowe
* **Spóźnienie**: **-3** punkty za każdy rozpoczęty tydzień (punkty mogą być ujemne; nie oddanie zadanie w ogóle skutkuje oceną 2 z przedmiotu).