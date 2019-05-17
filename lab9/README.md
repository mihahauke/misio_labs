# Lab 9-10 Q-learning w świecie Pacmana

## Acknowledgement
Zadanie to bazuje (włącznie z kodem) na jednym z zadań z kursu [CS188 na UC Berkley](http://ai.berkeley.edu/home.html), dostępnym także na [edX](https://edge.edx.org/courses/BerkeleyX/CS188x-8/Artificial_Intelligence/about) jeśli ktoś nie planuje zmieniać uczelni w najbliższym czasie. Gorąco zachęcamy do wzięcia w nim udziału.

## Cel
Celem tego ćwiczenia jest poznanie jednego z bardziej popularnych i eleganckich algorytmów uczenia ze wzmocnieniem Q-learningu. 

## Zadanie
Zadaniem jest zaimplementowanie algorytmu Q-learninig, który będzie umiał grać w Pacmana. Rozwiązanie przetestowane zostanie wielokrotnie na wielu instancjach - część plansz jest dostępna (można się na nich uczyć) w folderze [pacman_layouts](pacman_layouts). 

> Niestety nie ma żadnej automatycznej metody weryfikacji faktycznego zaimplementowania Q-learning poza weryfikacją kodu. W przypadku wykrycia braku implementacji Q-learningu (a coś innego, np systemy regułowe, przeszukiwanie drzewa itd.) rozwiązanie nie zostanie zakceptowane (0 punktów).

Rozwiązania powinny być już nauczonymi agentami, lecz zgłoszenie powinno zawierać też kod i dane użyte do treningu oraz sposób odtworzenia uczenia (preferencyjnie z ustawionym seedem). **W przypadku braku kodu uczącego zadanie nie zostanie zaliczone.**

## Kod
Do odpalenia kodu lokalnie posłużyć może plik [pacman_run.py](pacman_run.py). By zagrać w Pacmana osobiście wystarczy odpalić skrypt. Skrypt ten pozwala też na odpalanie i testowanie agentów, by poznań szczegóły użyj przełącznika **--help**/**-h**.

Do odpalenia kodu na optil.io zalecamy użyć klasy **StdIOPacmanRunner**, której zastosowanie jest zaprezentowane w skrypcie [greedy_solution.py](greedy_solution.py) wykorzystującym agenta zachłannego, który jest jednak z zabawy wykluczony (nie implementuje Q-learningu).

Do samej implementacji mogą być pomocne pliki [qlearningAgents.py](qlearningAgents.py) oraz [featureExtractors.py](featureExtractors.py) (nie jest absolutnie konieczne by ich użyć, ale mogą okazać się pomocne).

>> Do zaliczenia zadania wystarczający jest liniowy aproksymator, lecz zachęcamy do zaimplementowania czegoś bardziej skomplikowanego np. sieci neuronowych czy nawet [DQN](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf).

## Zaliczenie
* Zgłoszenie rozwiązania na platformie [Optil.io](https://www.optil.io/optilion/problem/3169)
* Termin: **przed** zajęciami za **2 tygodnie** 

## Punktacja
* **15** punktów; punkty będą liczone na podstawie średniej proporcji zwycięstw (winrate, od 0 do 1), na podstawie następującego wzoru: **15*max(0, min(1, (winrate - 0.1) / 0.9 + 0.3)) * (winrate > 0.1)**
* By zaliczyć zadanie należy otrzymać **POWYŻEJ** 30% punktów (4.5)
* **Spóźnienie**: **-20%** za każdy rozpoczęty tydzień.
