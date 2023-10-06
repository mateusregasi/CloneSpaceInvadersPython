import pygame
from abc import ABCMeta, abstractmethod

# Cria uma classe abstrada para as demais cenas do jogo
class Scene:

	def __init__(self, args, background):

		self.args = args
		self.background = background

	@property
	def background(self):
		return self.background

	@background.setter
	def background(self, background):
		if type(background) == tuple:
			self._background = tuple
		elif type(background) == str:
			self.background = pygame.image.load(background)
	
	@abstractmethod
	def loop():
		pass

	@abstractmethod
	def draw():
		pass