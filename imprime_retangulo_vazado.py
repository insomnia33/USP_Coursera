largura = int(input("digite a largua: ")) 
altura = int(input("digite a altura: ")) 
i = altura
while i > 0:
	if i == 1 or i == altura:
		j = 1
		while j <= largura:
			print("#", end="")
			j += 1
	else:
		j = 1
		while j <= largura:
			if j == 1 or j == largura:
				print("#", end="")
				j += 1
			else:
				print(" ", end="")
				j += 1
	i -= 1
	print()
