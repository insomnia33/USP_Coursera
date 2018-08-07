def soma_elementos(l1):
	aux = 0
	for i in l1:
		aux += i
	return aux

lista = [1,2,3,4,5,6,7,8,9]
print(soma_elementos(lista))