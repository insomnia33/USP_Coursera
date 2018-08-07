largura = int(input("digite a largua: "))
altura = int(input("digite a altura: "))

while altura >0:
	i = 0
	while i < largura:
		print("#", end="")
		i += 1
	altura -= 1
	print()