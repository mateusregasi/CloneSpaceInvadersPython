import pygame
from pygame.locals import *
from scene import Scene


# Classe que gerencia o menu do jogo
class Menu(Scene):

	def __init__(self, args):

		from game import Game
		from difficult import Difficult
		from ranking import Ranking

		self.args = args

		# Definindo background do menu
		self.background = args['colors']['black']

		# Margem e tamanho dos botões
		self.buttonsw = 300	# Largura dos botões
		self.buttonsh = 80	# Altura dos botões
		self.marginy = 30	# Margem y entre os botões

		# Definindo os botões
		buttons = {'Jogar':Game, 'Dificuldade':Difficult, 'Ranking':Ranking, 'Sair':'quit'}

		# Calculando a posição referencial de x e y dos botões
		quantidade = len(buttons)
		refx = args['width'] // 2 - self.buttonsw // 2
		refy = args['height'] // 2 - (self.marginy * (quantidade - 1) + self.buttonsh * quantidade) // 2

		# Criando a classe para os botões
		self.buttons = []
		for i, k in enumerate(buttons.keys()):
			self.buttons.append(
				Button(
					args, 
					k, 
					buttons[k], 
					refx, refy + i * self.buttonsh + i * self.marginy, 
					self.buttonsw, 
					self.buttonsh
				)
			)

	# Desenha as coisas na tela
	def draw(self):

		# Desenha o fundo
		self.args['window'].fill(self.args['colors']['black'])

		# Desenha os botões
		for button in self.buttons:
			button.draw()

	# Controla o loop do menu
	def loop(self):

		# Chama o loop de cada botão
		for button in self.buttons:
			button.loop()

		# Desenha as coisas na tela
		self.draw()

		# Sai do jogo se o jogador apertar ESC
		for event in pygame.event.get(exclude=True):
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					exit()
			if event.type == QUIT:
				pygame.quit()
				exit()

		# Altera o cursor do mouse e retorna ao estado original
		pygame.mouse.set_cursor(self.args['cursor'])
		self.args['cursor'] = pygame.SYSTEM_CURSOR_ARROW


# Aqui é definida a classe que vai cuidar dos botões do menu do jogo
class Button:

	def __init__(self, args, text, func, x=0, y=0, w=0, h=0):

		self.args = args

		# Aparência do texto
		self.text = text
		self.font = pygame.font.SysFont('roboto', 32)
		self.background_color = args['colors']['gray']
		self.background_hover_color = args['colors']['half_white']
		self.text_color = (255,255,255)

		# Background do texto
		self.background_rect = pygame.Rect(x, y, w, h)

		# Texto
		self.formated_text = self.font.render(self.text, True, self.text_color)
		self.text_size = self.font.size(self.text)

		# Posição do background
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.rect = pygame.Rect(x, y, w, h)

		# Posição do texto
		self.textx = self.x + (self.w // 2 - self.text_size[0] // 2)
		self.texty = self.y + (self.h // 2 - self.text_size[1] // 2)

		# Função quando o botão é pressionado
		self.func = func


	def draw(self):

		# Define a cor do background e altera o cursor se necessário
		if self.mouse_over(): 					# Alterar se o mouse tiver em cima
			cor = self.background_hover_color
			self.args['cursor'] = pygame.SYSTEM_CURSOR_HAND
		else:
			cor = self.background_color

		# Desenha o background
		pygame.draw.rect(self.args['window'], cor, self.rect)

		# Desenha o texto
		self.args['window'].blit(self.formated_text, (self.textx, self.texty))

	# Verifica se o mouse está acima do botão
	def mouse_over(self):
		return True if self.rect.collidepoint(pygame.mouse.get_pos()) else False

	# Verifica se o mouse clicou no botão
	def mouse_clicked(self):
		return True if (self.mouse_over() and pygame.mouse.get_pressed()[0]) else False

	def loop(self):

		# Verifica se clicaram em um Botão
		if self.mouse_clicked():

			# Se for uma classe, ela vai ser instanciada na próxima cena
			if type(self.func) == type:
				self.args['next_scene'] = self.func

			# Se for o botão de sair, ele vai sair do jogo
			elif type(self.func) == str:
				if self.func == 'quit':
					pygame.quit()
					exit()