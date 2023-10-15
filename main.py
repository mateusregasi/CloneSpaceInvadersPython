import pygame
from pygame.locals import QUIT
from menu import Menu

pygame.init()

# Constantes do programa
args = {}								# Essa variável args é muito importante, 
args['width'] = args['height'] = 600  	# porque ela vai ser referenciada em todo 
args['colors'] = {						# o programa para fazer o controle
	'black':(0,5,5),					# do fluxo do mesmo
	'half_white':(191,205,224),
	'white':(254,252,253),
	'dark_gray':(59,51,85),
	'gray':(93,93,129)
}
# A paleta de cores foi escolhida nesse site: https://coolors.co/000505-3b3355-5d5d81-bfcde0-fefcfd
args['cursor'] = pygame.SYSTEM_CURSOR_ARROW

# Janela
args['window'] = pygame.display.set_mode((args['width'], args['height']))
pygame.display.set_caption('Space Invaders')

# Definindo os argumentos
args['next_scene'] = None
args['current_scene'] = Menu(args)

# Game Loop
after_time = 0
while True:

	# Cria o Delta Time
	before_time = after_time
	after_time = pygame.time.get_ticks()
	args['delta_time'] = (after_time - before_time) / 1000

	# Loop da cena
	args['current_scene'].loop()

	# Troca de cena caso seja solicitado por outra parte do programa
	if args['next_scene']:
		args['current_scene'] = args['next_scene'](args)
		args['next_scene'] = None

	# Atualiza a tela
	pygame.display.flip()