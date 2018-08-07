def maximo(x,y,z):
	if x >= y and x >= z:
		return x
	elif y >= x and y >= z:
		return y
	elif z >= x and z >= y:
		return z


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

print(maximo(num1, num2, num3))