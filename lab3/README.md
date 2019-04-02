# Lab 3 Zagubiony Wumpus

## Cel
Wykorzystanie filtru histogramowego

## Zadanie
Napisz program, który wczyta plik zawierający opis środowiska oraz w najkrótszym możliwie czasie znajdzie drzwi wyjściowe.

Świat jest prostokątem, o wymiarach **N** wierszy na **M** kolumn. Wumpus porusza się w świecie wykonując ruchy Góra, Dół, Lewo, Prawo. Świat nie ma ścian i jest cykliczny, to znaczy, że wykonując ruch Góra w pola w pierwszym wierszu Wumpus (zwykle) dociera do pola w ostatnim wierszu. Wumpus jest otumaniony, dlatego jest niepewny swoich akcji. Wykonując ruch z prawdopodobieńśtwem **p** (np. 0.8) dotrze do docelowego pola, ale z prawd. (1-**p**)/4 (np. 0.05) znajdzie się na jednym z czterech pól sąsiadujących z polem docelowym.

W świecie Wumpusa są jamy. Dla otumanionego Wumpusa nie są one jednak groźne, a stanowią dla niego ważne punkty orientacyjne. Jeśli Wumpus stanie na polu, na którym jest jama odnotowuje ten fakt z prawdopodobieństwem **pj** (np. 0.7). Niestety, ze względu na otumanienie, czasem (z prawd. **pn** (np. 0.1)) wydaje mu się, że wpadł do jamy, gdy tymczasem nic takiego nie miało miejsca.

Wumpus posiada mapę świata, ale nie ma pojęcia, gdzie się znajduje. Pomóż mu jak w jak najmniejszej liczbie ruchów dotrzeć do pola oznaczonego jako Wyjście.

## Zaliczenie
* Rozwiązanie należy zgłościć na [Optil.io](https://www.optil.io/optilion/problem/3166). Rozwiązanie testowane będzie odpalane 100 razy na różnych instancjach.
* Zadanie indywidualne (proszę się konsultować, wymieniać pomysłami, natchnieniem, ale **nie kodem**)
* Termin: przed zajęciami za **dwa tygodnie**

## Punktacja
* 15 punktów: min(15,5 + (7000-k)/(7000-4700)*(15-5)), gdzie k to jest jest średnia ilośc krotków ze wszystkich instancji
* **Spóźnienie**: **-20%** za każdy rozpoczęty tydzień.
