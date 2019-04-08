# Inteligentne Agenty (AIMA)

## Cel
Wstępne zapoznanie się z podstawowymi pomysłami w AI: środowiska, agenty, racjonalność itd.

## Zadanie
Uruchom **ipython3 notebook** i wybierz [misio_lab1.ipynb](misio_lab1.ipynb). Postępuj zgodnie z instrukcją.

>> Do odpalenia zadań lokalnie potrzebne jest zainstalowanie pakietu [misio](../misio) oraz [aima3].

```
git clone https://github.com/mihahauke/misio_labs
cd misio
sudo pip3 install .
sudo pip3 install aim3
```
albo:
```
sudo pip3 install git+https://github.com/mihahauke/misio_labs
sudo pip3 install aima3
```
albo bez uprawnień roota:
```
pip3 install git+https://github.com/mihahauke/misio_labs --user 
pip3 install aima3 --user
```


## Zaliczenie
* Praca indywidualna.
* Na kolejne zajęcia przynieś **jedną** wydrukowaną **stronę** A4 z wynikami zadań - odpowiedziami na pytania w notebooku (W szczególności kodem agenta, histogramem). W przypadku oddania większej liczby stron, wszystkie poza peirwszą zostaną zignorowane. [Przykładowe sprawozdanie(na 0 punktów)](report/aima_sample_report.pdf)
* Kod agenta należy zgłosić na [Optil.io](https://www.optil.io/optilion/problem/3161). Testy będą odpalane deterministycznie więc zgłoszenie deterministycznego agenta będzie skutkowało tym samym wynikiem. Przed zgłoszeniem można przetestować agenta lokalnie (wynik powinien być podobny) dlatego czętość zgłoszeń na platformie jest ograniczona. Wyniki na kartce powinny zgadzać się z tymi uzyskanymi na Optil.io.
* Termin: **godzina przed** kolejnymi zajęciami (planowo tydzień)

## Przykładowe rozwiązanie:
Kod agenta, który ssie:
```python
#!usr/bin/python3
n,s = [int(x) for x in input().split()]
for _ in range(n*s):
  _ = input()
  print("Suck")

```
