def n_primos(num):
	if num == 2:
		return 1
	elif num == 3:
		return 2
		
	cont = 3
	primos = -1
	while cont <= num:
		cont2 = cont
		while cont2 >= 2:
			if cont%cont2 == 0:
				check = False
			else:
				check = True
			cont2 -= 1
		if check:
			primos += 1  
		cont += 1
	return primos

n = int(input("Digite um número: "))
print(n_primos(n))