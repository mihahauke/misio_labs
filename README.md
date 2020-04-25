# Metody Inteligencji Sztucznej i Obliczeniowej
![MISIO](bear.png)
This repository contains resources necessary to complete Artificial Intelligence courses (MISiO) at Poznan University of Technology.

* [Grades 2020](https://docs.google.com/spreadsheets/d/1gf9hsB2qr4GsQVrZCliCZHcrqlIQ0Bst1mKypeQk57M/edit?usp=sharing)
* [Grades 2019](https://docs.google.com/spreadsheets/d/1Okp2dJ20mIQSQEw2SzQ-COdBgvsHNPtdypPQ5ROZcxA/edit?usp=sharing) 

# Python Package
To run some of the tasks a special python package will be needed. To install it use:

```
git clone https://github.com/mihahauke/misio_labs
cd misio
sudo pip3 install .
```
or:
```
sudo pip3 install git+https://github.com/mihahauke/misio_labs
```
or if you don't have root access:
```
pip3 install git+https://github.com/mihahauke/misio_labs --user 
```

# Grading
## tl;dr:
* you have to do **all** tasks
* delays are penalized
* cheating and sharing code will result in grade **2/2** 

## Full 
>> "Unless stated otherwise in the task description" applies to all of the following points.
* **each** task has to be completed to <span style="color:green">pass</span>
 the course; failure to do so will result in <span style="color:red">**FAILING**</span> (getting grade 2) regardless of points scored on other tasks; 
* a task is considered completed if a solution is submitted and it scores at least **30%** of achievable points (before potential delay penalty);
* attendance is **officially** mandatory (as per University code); in case of any doubts about scoring/cheating lack of attendance may result in disadvantageous consideration
* solutions submitted before the start of the next class; every started week of delay results in cummulative **-20%** penalty, some examples:
    * 15/15 (100%), 5 weeks of delay, task accepted,
    points gained: 15 *(1-0.2*5) = 0
    * 10/15 (66.66%), 2 weeks of delay, task accepted,
    points gained: 10 *(1-0.2*2) = 6
    * 4.5/15 (30%), 1 week of delay, task accepted,
    points gained: (1-0.2*1) *4.5 = 3.6
    * 4.5/15 (30%), 2 weeks of delay, task accepted,
    points gained: (1-0.2*2)*4.5 =2.7
    * 4/15 (<30%), no delay, task not accepted, Failing grade (2),
* sharing your code or solutions is prohibited (you may however share your thoughts and ideas)
* submitting someone else's solutions or its parts will result in grade **2/2** and any legal repercussions available

## In case of FAILING:
Complete every task and you get whatever is determined by your points (no penalties for delays).


# [Lab 1 Intelligent agents](lab1) (10 pts)
Introduction to artificial intelligence basics: agents, environments, rationality etc. 
This task uses python's [aima3](https://github.com/Calysto/aima3) library for AIMA(Artificial Intelligence Modern Approach).

# [Lab 2 Uncertain Wumpus](lab2) (15pts)
Practical example of uncertainty in Artificial Intelligence.

# [Lab 3 Lost Wumpus](lab3) (15pts)
Using histogram filter for navigation.

# [Lab 4 MDP AIMA](lab4) (10pts)
Introduction to **Markov Decision Processes** (MDPs) which are a fundamental framework for modern AI algorithms.

# [Lab 5 MDP Wumpus Store](lab5) (15pts)
More Markov Decision Processes.

# [Lab 6 Q-Learning](lab6)(15pts)
Reinforcement Learning using one of the most popular and well known algorithm: Q-learning

# [Lab 7 Actor-critic](lab7)(15pts)
Reinforcement Learning: actor-critic (continuous action-spaces)

# Authors
* Michał Kempka

# Acknowledgements 
Big portions of the cirriculum was designed by **[Wojciech Jaśkowski](https://scholar.google.pl/citations?user=89a-n3YAAAAJ&hl=en)** and based on AI course on Berkley.
