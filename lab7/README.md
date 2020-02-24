# Lab 7 Advantage Actor Critic (Continuous Action-Spaces RL)

## Acknowledgement
Zadania te korzystają ze środowiska [OpenAI Gym](https://gym.openai.com). By odpalać kod lokalnie należy zainstalować odpowiednie pakiety.
```bash
sudo pip3 install gym
sudo pip3 install sudo pip3 install box2d-py

```

## Cel
Celem tego ćwiczenia jest poznanie jednego z bardziej popularnych i eleganckich algorytmów uczenia ze wzmocnieniem Q-learningu. 

## Zadanie
Zadaniem jest zaimplementowanie algorytmu A2C (advantage actor critic) lub DDPG (Deep Deterministic Policy Gradient), który będzie umiał postawić [wahadło](https://gym.openai.com/envs/Pendulum-v0/) i poruszać się [dwunożnym stworkiem](https://gym.openai.com/envs/BipedalWalker-v2). 

> Niestety nie ma żadnej automatycznej metody weryfikacji faktycznego zaimplementowania A2C poza weryfikacją kodu. W przypadku wykrycia braku implementacji A2C (a coś innego, np systemy regułowe, przeszukiwanie drzewa itd.) rozwiązanie nie zostanie zakceptowane (0 punktów).

Rozwiązania powinny być już nauczonymi agentami, lecz zgłoszenie powinno zawierać też kod i dane użyte do treningu oraz sposób odtworzenia uczenia (preferencyjnie z ustawionym seedem). **W przypadku braku kodu uczącego zadanie nie zostanie zaliczone.**

## Materiały i rady

### Co warto rozważyć
TODO

### Literatura
* [REINFORCE](http://incompleteideas.net/sutton/williams-92.pdf)
* [DPG (Deterministic Policy Gradient) off-policy actor-critic]
* [DDPG (Deep-DPG)](https://arxiv.org/abs/1509.02971)
* [A3C (asynchronous advantage actor-critic)](https://arxiv.org/pdf/1602.01783.pdf)

## Zaliczenie
* Zgłoszenie rozwiązania na platformie [Optil.io](https://www.optil.io/optilion/problem/3170)
* Termin: przed rozpoczęciem sesji 

## Punktacja
* **15** punktów; punkty będą liczone na podstawie punktów uzyskanych na obydwu roblemach, według wzoru: (pts_pendulum+1000)/70 + (pts_walker+100)/40
* **UWAGA** zadanie jest **NIEOBOWIĄZKOWE** by zaliczyć laboratorium, można zadania nie oddać i zdać (jeśli pozostałe punkty dadzą 3)
* **Spóźnienia** nieakceptowane.
