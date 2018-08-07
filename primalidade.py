num = int(input("Digite um número inteiro: "))
aux = num - 1
while aux > 1:
	if num%aux == 0:
		primo = False
		aux = 0
	else:
		aux -= 1
		primo = True
		
if primo:
	print("primo")
else:
	print("não primo")


		

