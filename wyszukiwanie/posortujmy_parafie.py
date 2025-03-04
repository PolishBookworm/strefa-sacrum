import csv
#id parafii to numer wiersza w którym ta parafia sie znajduje, numerujemy od 0


file = csv.reader(open("daneprzyklad.csv", "r", encoding='utf-8'), delimiter=';')

parafie = []
i = 0
for par in file:
	parafie.append(f"{par[0]}~{i}")
	i += 1

parafie.sort()

result = []
for par in parafie:
	tmp = par.split("~")
	result.append(int(tmp[1]))

print(*result)