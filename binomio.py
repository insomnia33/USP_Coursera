def fat(num):
	fat = 1
	while n > 1:
		fat = fat*num
		num -= 1
	return fat
		
def binomio(n, k):
	return fat(n)//(fat(k)*(fat(n-k)))


n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

print("O número binomial é ", binomio(n, k))