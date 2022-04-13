#  AI - Project1_team4
## Traveling Salesman Problem


### Requirements
> pandas
> 
> scikit-learn
> 
> matplotlib
> 
> click




# How to use python main.py
## 1. Complete Random Search

```
python main.py
```


> or


```
python main.py --option=1
```


## 2. Genetic TSP
> run as default(sol=10, gen=1000)


```
python main.py --option=2
```


> or

```
python main.py --option=2 --s=10 --g=1000
```


## 3. Genetic TSP with Tree Search
> run as default(k=10, sol=10, gen=1000)
```
python main.py --option=3
```

> or

```
python main.py --option=3 --k=10 --s=10 --g=1000
```

4. Crossover method default is PMX
> But can choose crossover method to use 'order'

```
python main.py --option=2 --c='order'
```
