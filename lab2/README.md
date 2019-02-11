# Niepewność w świecie Wumpusa

## Cel
Praktyczne zastosowanie rachunku prawdopodobieństwa dla celów AI.

## Zadanie
Napisz program, który wczyta plik zawierający opis środowiska uproszczonego Wumpus’a i dla każdego pola świata wywnioskuje prawdopodobieństwo, że pole zawiera jamę biorąc pod uwagę aktualną wiedzę agenta.


W ten sposób agent aktualizuje swoją wiedzę o stanie środowiska (wnioskuje na temat nieobserwowalnej części świata).

## Opis wejścia i wyjścia

* Plik wejściowy rozpoczyna się od ilości instancji do wczytania. Kolejne linie zawierają:
    * liczbę wierszy **n**, liczbę kolumn świata **m**,
    * prawdopodobieńśtwo obecności pułapki dla pola,
    * tablicę o **n** wierszach i **m** kolumnach zawierającą **‘?’** jeśli pole jest nieodwiedzone, **‘B’** jeśli pole jest odwiedzone i agent wyczuł wiatr, **‘O’** jeśli pole jest odwiedzone, ale agent nie wyczuł wiatru.
* Plik wyjściowy zawiera tablicę n na m liczb rzeczywistych oznaczających prawdopodobieńśtwo obecności jamy w danym polu (liczby zaokrąglić do drugiego miejsca po przecinku).
* [Przykładowe pliki in/out](test_cases)
## Ocena
* 10 pkt + ewentualne punkty bonusowe
* Praca indywidualna.
* Na kolejne zajęcia przynieś **jedną** wydrukowaną kartkę A4 z wynikami zadań. (W szczególności kodem agenta, histogramem).
* Kod agenta należy zgłosić na [Optil.io](https://www.optil.io/optilion/author/problem/3159) najpóźniej do **godziny** przed następnymi zajęciami. Wyniki na kartce powinny zgadzać się z tymi uzyskanymi na Optil.io.
>> **Spóźnienie**: za każdy rozpoczęty tydzień -50% punktów.