qtd = input()
notas = raw_input().split(" ")

negativos = []

for x in notas :
	if float(x) < 0:
		negativos.append(float(x))
	else :
		continue
menor = negativos[0]

for x in negativos:
	if float(x) < menor:
		menor = float(x)
	else :
		continue
print len(negativos)
print menor		