import math

def calc_delta(a,b,c):
	return b ** 2 - 4 * a * c

def raizes(a,b,c):
	delta = calc_delta(a,b,c)
	if delta < 0:
		print("esta equação não possui raízes reais")
	elif delta == 0:
		x1 = (-b+math.sqrt(delta))/2*a
		print("a raiz desta equação é", x1)
	elif delta > 0:
		x1 = (-b+math.sqrt(delta))/2*a
		x2 = (-b-math.sqrt(delta))/2*a
	if x1 <= x2:
		print("as raízes da equação são %.2f e %.2f" %(x1,x2))
	else:
		print("as raízes da equação são %.2f e %.2f" %(x2,x1))



a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
raizes(a,b,c)

