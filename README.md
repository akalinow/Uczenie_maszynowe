[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/akalinow/uczenie_maszynowe)


# Uczenie maszynowe - wersja dla prowadzących
Repozytorium zawierające notatniki Jupyter będącymi podstawą ćwiczeń z Uczenia maszynowego 
(1100-3BN17, Wydział Fizyki UW)

Repozytorium zawiera gałęzie w wersjami dla studentów, oraz prowadzącego.
Wersja prowadzącego zawiera rozwiązania zadań wykonywanych na ćwiczeniach.

## Generacja wersji studenckiej

Wersja studencka jest generowana automatycznie przez wykonanie skryptu
[scripts/makeStudentsVersion.py][scripts/makeStudentsVersion.py].
Skrypt usuwa rozwiązania i ładuje nową werjsę go gałęzi z usuniętym przrostkiem "_solutions"

Framgenty komórek znajdujące się między znacznikami `#BEGIN SOLUTION` oraz `#END SOLUTION`
zostaną zastapione trzema kropkami: `...`

``` python
def classifier (X, threshold):
    ### BEGIN SOLUTION
    return X > threshold
    ### END SOLUTION
```

The above in student's version will become:
``` python
def classifier (X, threshold):
    ### YOUR CODE HERE
```

### Instrukcja:
```
cd Uczenie_maszynowe
./scripts/makeStudentsVersion.py
```


```
awk '/#BEGIN/{p=1}/#END/{p=0;print "\t\"...\\n\",";next}!p' Tests.nbconvert.ipynb > Tests.ipynb
```

