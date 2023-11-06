# Demander la valeur max
max_value = int(input("Entrez la valeur maximale: "))

# Initialiser la liste des nombres premiers
primes = []

# Dictionnaire pour la décomposition
factors = {}

# Boucler de 2 à max_value
for i in range(2, max_value + 1):

    # Tester si le nombre est premier
    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break

    # Si premier, l'ajouter à la liste
    if is_prime:
        primes.append(i)
        print(i)

    # Sinon, calculer et enregistrer sa décomposition
    else:
        f = []
        for p in primes:
            if i % p == 0:
                f.append(p)
                i = i / p
        factors[i] = f
        print(factors[i])

# Enregistrer les nombres premiers
with open("primes.csv", "w") as f:
    f.write(",".join(str(p) for p in primes))

# Enregistrer la décomposition
import csv

with open("factors.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(primes)
    for num, fact in factors.items():
        row = [num]
        for p in primes:
            row.append(fact.count(p))
        writer.writerow(row)
