# Pseudocode:
# 1. Für jede Zahl von 2 bis 100:
#    a. Überprüfe, ob die Zahl eine Primzahl ist.
#       i. Eine Zahl ist eine Primzahl, wenn sie nur durch 1 und sich selbst teilbar ist.
#       ii. Überprüfe dies, indem du die Zahl durch jede kleinere Zahl als sie selbst teilst.
#       iii. Wenn die Zahl durch eine andere Zahl teilbar ist, ist sie keine Primzahl.
#    b. Wenn die Zahl eine Primzahl ist, drucke sie aus.

# Python-Code:
for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break
    if prime:
        print(num)