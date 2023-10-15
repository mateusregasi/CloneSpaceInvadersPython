import pygame
from pygame.locals import *

class Game:
	
	def __init__(self, args):
		from player import Player
		self.args = args

		# Defina o fundo
		self.background = args['colors']['black']

		# Inicia os players
		self.player = Player(args)

		# Inicia a lista de tiros e inimigos
		self.args['shots'] = []
		self.args['enemies'] = []

	def loop(self):

		# Pinta a janela
		self.args['window'].fill(self.background)

		# Condição de saída do jogo
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()

			if event.type == KEYDOWN:

				if event.key == K_SPACE:
					self.player.shot()

		# Aplica movimentação no personagem
		self.player.loop()

		# Aplica movimentação nos tiros e nos inimigos
		for shot in self.args['shots']:
			shot.loop()
		for enemy in self.args['enemies']:
			enemy.loop()

		# Desenha as coisas na tela
		self.draw()

	def draw(self):

		# Desenha o personagem
		self.player.draw()

		# Desenha os tiros se tiver
		for shot in self.args['shots']:
			shot.draw()