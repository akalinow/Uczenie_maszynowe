[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/akalinow/Uczenie_maszynowe/blob/2022_2023)


# Uczenie maszynowe - wersja dla prowadzących
Repozytorium zawierające notatniki Jupyter będącymi podstawą ćwiczeń z Uczenia maszynowego 
(1100-3BN17, Wydział Fizyki UW)

Repozytorium zawiera gałęzie w wersjami dla studentów, oraz prowadzącego.
Wersja prowadzącego zawiera rozwiązania zadań wykonywanych na ćwiczeniach.

## Generacja wersji studenckiej

Wersja studencka jest generowana automatycznie przez wykonanie skryptu
[scripts/makeStudentsVersion.py][scripts/makeStudentsVersion.py].
Skrypt usuwa rozwiązania i ładuje nową wersję do gałęzi z usuniętym przyrostkiem "_solutions"

    "...\n", 
zostaną zastapione trzema kropkami: `...`

``` python
def classifier (X, threshold):
    "...\n", 
```

The above in student's version will become:
``` python
def classifier (X, threshold):
    ...
```

### Instrukcja:
```
cd Uczenie_maszynowe
./scripts/makeStudentsVersion.py
```

    "...\n", 

