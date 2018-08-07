n =1
while n >= 0:
	n = int(input("Digite o valor de n ou 0 para sair: "))
	fat = 1
	while n > 1:
		fat = fat*n
		n -= 1
	print(fat)
