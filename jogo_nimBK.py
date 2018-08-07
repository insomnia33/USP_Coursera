global camp
global rodada
camp = True
rodada = 1

def usuario_escolhe_jogada(n,m):
	m = m
	remove = int(input("\nQuantas peças você vai tirar? "))
	if remove > m or remove < 0:
		print("\nOops! Jogada inválida! Tente de novo.")
		usuario_escolhe_jogada(n,m)
	else:
		n = n-remove
		if remove == 1:
			print("Você tirou uma peça.")
			if n == 1:
				print("Agora resta apenas uma peça no tabuleiro.")
				computador_escolhe_jogada(n,m)
			else:
				print("Agora restam apenas %d peças no tabuleiro." %n)
				computador_escolhe_jogada(n,m)
		else:
			print("Você tirou %d peças." %remove)
			if n == 1:
				print("Agora resta apenas uma peça no tabuleiro.")
				computador_escolhe_jogada(n,m)
			else:
				print("Agora restam %d peças no tabuleiro." %n)
				computador_escolhe_jogada(n,m)

def computador_escolhe_jogada(n,m):
	global rodada
	global camp
	cont = n
	while cont > 0:
		if n <= m:
			remove = n
			if remove == 1:
				print("\nO computador tirou uma peça.")
				print("Fim do jogo! O computador ganhou!")
				if camp == True:
					rodada = rodada + 1
					campeonato()
				else:
					quit()
			else:
				print("\nO computador tirou %d peças." %remove)
				print("Fim do jogo! O computador ganhou!")
				if camp == True:
					rodada = rodada + 1
					campeonato()
				else:
					quit()
		elif cont%(m+1) == 0:
			remove = n-cont
			if remove == 1:
				print("\nO computador tirou uma peça.")
				if cont == 1:
					print("Agora resta apenas uma peça no tabuleiro.")
					usuario_escolhe_jogada((n-remove), m)
				else:
					print("Agora restam %d peças no tabuleiro" %(cont))
					usuario_escolhe_jogada((n-remove), m)
			else:
				if cont == 1:
					print("Agora resta apenas uma peça no tabuleiro.")
					usuario_escolhe_jogada((n-remove), m)
				else:
					print("\nO computador tirou %d peça(s)." %remove)
					print("Agora restam %d peças no tabuleiro" %(cont))
					usuario_escolhe_jogada((n-remove), m)	

		else:
			cont -= 1

def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	if n%(m+1) == 0:
		print("\nVocê começa!")
		usuario_escolhe_jogada(n,m)
	else:
		print("\nComputador começa!")
		computador_escolhe_jogada(n,m)

def campeonato():
	global rodada
	if rodada > 3:
		print("\n**** Final do campeonato! ****")
		print("\nPlacar: Você 0 X 3 Computador")
		quit()
	else:
		print("\n**** Rodada %d ****\n" %rodada)
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
		if n%(m+1) == 0:
			print("\nVocê começa!")
			usuario_escolhe_jogada(n,m)
		else:
			print("\nComputador começa!")
			computador_escolhe_jogada(n,m)


def start():
	global camp
	opcao = int(input("\nBem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
	if opcao == 1:
		print("\nVoce escolheu uma partida isolada!")
		camp = False
		partida()
	elif opcao == 2:
		print("\nVoce escolheu um campeonato!")
		camp = True
		campeonato()
	else:
		start()
	

start()