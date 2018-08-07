import math

xa = int(input("Digite a primeira coordenada: "))
ya = int(input("Digite a primeira coordenada: "))
xb = int(input("Digite a primeira coordenada: "))
yb = int(input("Digite a primeira coordenada: "))
dist = math.sqrt((xb-xa)**2+(yb-ya)**2)
if dist >= 10:
	print("longe")
else:
	print("perto")