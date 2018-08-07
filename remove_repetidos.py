def remove_repetidos(l1):
	l = []
	for i in l1:
		if i not in l:
			l.append(i)
	l.sort()
	return l



lista = [1,2,1,3,4,7,10]
print(remove_repetidos(lista))