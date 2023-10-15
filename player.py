import pygame
from pygame.locals import *

class Player:

	def __init__(self, args):
		self.args = args

		# Posição e movimentação do personagem
		self.velx = 200
		self.scale = 5
		self.w = 16 * self.scale
		self.h = 16 * self.scale
		self.x = args['width'] // 2 - self.w // 2
		self.y = args['height'] - 100

		# Importa as imagens do player
		self.sprites = []
		spritesheet = pygame.image.load('player.png')
		for i in range(3):
			self.sprites.append(spritesheet.subsurface((i * 16, 0, 16, 16)))
			self.sprites[i] = pygame.transform.scale(self.sprites[i], (self.w, self.h))

		# Define os estados do personagem, cada estado está associado a um sprite
		self.states = {'default':0, 'left':1, 'right':2}
		self.state = 0

		# Variáveis que vão controlar o tiro
		self.recal = 1
		self.recal_time = 0

	def input(self):
		self.state = self.states['default']

		# Caso aperte para ir para esquerda
		if pygame.key.get_pressed()[K_a]:
			self.state = self.states['left']
			self.x -= self.args['delta_time'] * self.velx

		# Caso aperte para ir para direita
		elif pygame.key.get_pressed()[K_d]:
			self.state = self.states['right']
			self.x += self.args['delta_time'] * self.velx

	def verify_move(self):

		# Arruma o movimento se bater na parede
		self.x = 0 if self.x < 0 else self.x
		self.x = (self.args['width'] - self.w) if self.x >= self.args['width'] - self.w else self.x

	# Movimento do player
	def move(self):
		self.input()
		self.verify_move()

	def loop(self):

		# Movimenta o player e desconta o tempo de recall do tiro
		self.move()
		self.recal_time -= self.args['delta_time']

	def shot(self):

		# Verifica se já passou o tempo de recall
		if self.recal_time < 0:

			self.recal_time = self.recal

			# Define a posição inicial do tiro
			x = self.x + self.w // 2
			y = self.y

			# Adiciona o tiro na lista de tiros
			self.args['shots'].append(Shot(self.args, x, y))

	# Desenha o personagem na tela
	def draw(self):
		self.args['window'].blit(self.sprites[self.state], (self.x, self.y))


class Shot:

	def __init__(self, args, x, y):
		self.args = args

		# Posição inicial do tiro
		self.w = 10
		self.h = 30
		self.x = x - self.w // 2
		self.y = y - self.h
		self.rect = pygame.Rect((self.x, self.y, self.w, self.h))

		# Velocidade
		self.vely = 150

	def loop(self):

		# Move o tiro
		self.y -= self.args['delta_time'] * self.vely

		# Atualiza o retângulo do tiro
		self.rect = pygame.Rect((self.x, self.y, self.w, self.h))

	# Desenha o tiro
	def draw(self):
		pygame.draw.rect(self.args['window'], self.args['colors']['half_white'], self.rect)