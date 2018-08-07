a = int(input("Digite um número: "))
soma = 0
while a > 0:
	soma = soma+a%10
	a = a//10
print(soma)
