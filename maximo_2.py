def maximo(x,y):
	if x >= y:
		return x
	elif x < y:
		return y


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
print(maximo(num1, num2))