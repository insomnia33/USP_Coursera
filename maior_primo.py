def maior_primo(x):
	num = 3
	primo = 3
	while num <= x:
		primo = eh_primo(num, primo)
		num += 1
	return primo

def eh_primo(y, z):
	aux = y - 1
	while aux > 1:
		if y%aux == 0:
			primo = False
			return z
		else:
			primo = True
			aux -= 1
	if primo:
		return y

		
num1 = int(input("Digite um número maior ou igual a 2: "))
print(maior_primo(num1))
