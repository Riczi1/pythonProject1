import random
#generowanie listy
lista = [random.randint(1, 100) for _ in range(100)]
print(lista)

#sposób 1
licznik = 0
for liczba in lista:
    if liczba > 50:
        licznik += 1

print(f"Ilość liczb większych niż 50: {licznik}")

#sposób 2
licznik = len([x for x in lista if x > 50])

print(f"Ilość liczb większych niż 50: {licznik}")

#sposób 3
licznik = len(list(filter(lambda x: x > 50, lista)))

print(f"Ilość liczb większych niż 50: {licznik}")

#sposób 4
licznik = sum(1 for liczba in lista if liczba > 50)

print(f"Ilość liczb większych niż 50: {licznik}")

