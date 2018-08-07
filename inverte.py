lista = []
check = 1
while check != 0:
	check = int(input("Digite um número: "))
	if check == 0:
		break
	lista.append(check)
lista.reverse()

for item in lista:
	print(item)