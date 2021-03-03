# Lab 7 Advantage Actor Critic (Continuous Action-Spaces RL)

Zadania te korzystają ze środowiska [OpenAI Gym](https://gym.openai.com). By odpalać kod lokalnie należy zainstalować odpowiednie pakiety.

```bash
sudo pip3 install gym==0.17.2
sudo pip3 install box2d-py==2.3.8

```

>>> Proszę zwrócić uwagę, że w wersji 0.17.2 Potrzeba użyć 
"BipedalWalker-v3", lecz zdokumentowany jest "BipedalWalker-v2". Z czego to wynika nie mam pojęcia.

## Cel
Celem tego zadania jest zaimplementowanie metody Policy Gradient, która pozwala operować w środowiskach używających ciągłych akcji, w przeciwieństwie do Q-learningu gdzie akcje muszą być zdyskretyzowane.

## Zadanie
Jak w [poprzednim ćwiczeniu](../lab6) zadaniem jest napisanie agenta, który będzie działał w środowisku (otrzymywał stany, wykonywał akcje i otrzymywał za to nagrody) i uczył się zyskiwać jak najwięcej punktów (sumaryczna nagroda). W tym wypadku akcje będą w **przestrzeni ciągłej** tzn. nie będą przyjmowały jednej z np. 4 wartości (up, down, left, right) lecz będą dowolnymi liczbami rzeczywistymi (lub nawet wektorami rzeczywistymi).

Należy zaimplementować metodę Policy Gradient (np. Advantage Actor Critic lub  Deterministic Policy Gradient), który będzie umiał postawić [wahadło](https://gym.openai.com/envs/Pendulum-v0/) i poruszać się [dwunożnym stworkiem](https://gym.openai.com/envs/BipedalWalker-v2) (proszę nie dyskretyzować przestrzeni akcji). 

Rozwiązania powinny być już nauczonymi agentami, lecz zgłoszenie powinno zawierać też **kod** i **dane** użyte do treningu oraz **instrukcję** odtworzenia uczenia w sposób deterministyczny. **W przypadku braku kodu uczącego, zadanie nie zostanie zaliczone.**

> Niestety nie ma żadnej automatycznej metody weryfikacji faktycznego zaimplementowania Gradient Policy. W przypadku wykrycia braku implementacji odpowiedniego algorytmu (a coś innego, np systemy regułowe, przeszukiwanie drzewa itd.) rozwiązanie nie zostanie zakceptowane (0 punktów). W przypadku wykrycia skopiowania kodu z internetu także przyznane zostanie 0 punktów.

## Od czego zacząć
Skrypt [run_locally.py](run_locally.py) pokazuje jak odpalić środowiska lokalnie. Najlepiej zapoznać się ze środowiskami przez zabawę skryptem oraz dokumentację 
[Pendulum-v0](https://gym.openai.com/envs/Pendulum-v0/) i [BipedalWalker-v2](https://gym.openai.com/envs/BipedalWalker-v2).

## Przykładowe rozwiązanie
Skrypt [random_solution.py](random_solution.py) pokazuje deterministycznego losowego agenta.

## Kod uczący
Żeby zadanie zostało zaliczone należy wysłać także kod uczący i instrukcję. Powinno być to zrealizowane jak w [poprzednim zadaniu](../lab6).

### Materiały
* [Wykład Davida Silvera o  Gradient Policy](https://www.youtube.com/watch?v=KHZVXao4qXs)
* [Deterministic Policy Gradient](http://proceedings.mlr.press/v32/silver14.pdf)
* [DDPG (Deep-DPG)](https://arxiv.org/abs/1509.02971)
* [A3C (asynchronous advantage actor-critic)](https://arxiv.org/pdf/1602.01783.pdf)

## Zaliczenie
* Zgłoszenie rozwiązania na platformie [Optil.io](https://www.optil.io/optilion/problem/3170)
* Wzięte zostanie pod uwagę **OSTATNIE** zgłoszenie.
* Termin: **TODO**

## Punktacja
* **15** punktów; punkty będą liczone na podstawie punktów uzyskanych na obydwu roblemach, według wzoru: **TODO**. Na zadaniu można uzyskać do 5 dodatkowych punktów. Błąd na którejkolwiek z instancji (MLE, RTE, TLE etc.) skutkuje niezaliczeniem zadania.
* Zadanie jest **OBOWIĄZKOWE**, by je zaliczyć należy otrzymać **CONAJMNIEJ** 30% punktów (4.5)
* **Spóźnienie**: spóźnienia nie są dopuszczalne, należy dostarczyć rozwiązanie przed rozpoczęciem **lipca** 2020.
