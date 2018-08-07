num = int(input("Digite um número inteiro: "))
cond = True
while num//10 != 0:
	rest1 = num%10
	num = num//10
	rest2 = num%10
	if rest1 == rest2:
		print("sim")
		cond = False
if cond:
	print("não")		



