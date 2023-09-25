import pygame

class Sprite():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.h = h
		self.w = w
		self.px = 0
		self.py = 0
	
	def setPrevious(self):
		self.px = self.x
		self.py = self.y
	
	def getOut(self, p):
		if (((self.px + self.w) <= p.x) & ((self.x + self.w) >= p.x)):
			self.x = p.x - self.w
		if ((self.px >= (p.x + p.w)) & (p.x <= (p.x + p.w))):
			self.x = p.x + p.w
		if (((self.py + self.h) <= p.y) & ((self.y + self.h) >= p.y)):
			self.y = p.y - self.h
		if (self.py >= (p.y + p.h)):
			self.y = p.y + p.h
	
	def isPlayer(self):
		return False
	def isEnemy(self):
		return False
	def update(self):
		return

class Player(Sprite):
	
	def __init__(self, x, y, w, h):
		super().__init__(x, y, w, h)
		self.health = []
		self.image = pygame.image.load("images/heart.png")
		self.vert_velocity = 0
	
	def isPlayer(self):
		return True
	def isEnemy(self):
		return False
	def update(self):
		if self.vert_velocity < 100:
			self.y = self.vert_velocity
		else:
			if self.vert_velocity > 0:
				self.vert_velocity -= 3.14
	
class Enemy(Sprite):
	def __init__(self, x, y, w, h):
		super().__init__(x, y, w, h)
	
	def isPlayer(self):
		return False
	def isEnemy(self):
		return True
	def update(self):
		return

class Model():
	def __init__(self):
		self.sprites = []
		self.player = Player(0 , 0, 50, 50)
		self.enemy = Enemy(255, 0, 50, 50)
		self.sprites.append(self.player)
		self.sprites.append(self.enemy)
		self.counter = 0
	
	def update(self):
		for sprite in self.sprites:
			sprite.update()
			if(self.isCollision(sprite, self.player)):
				if sprite.isEnemy():
					self.player.getOut(sprite)
					
				
	
	def isCollision(self, t, b):
		if (b.x + b.w <= t.x):
			return False
		if (b.x >= t.x + t.w):
			return False
		if (b.y + b.h <= t.y):
			return False
		if (b.y >= t.y + t.h):
			return False
		else:
			return True

class Controller():
	def __init__(self, model):
		self.model = model

	def update(self):
		self.model.player.setPrevious()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.model.player.x -= 5
		if keys[pygame.K_RIGHT]:
			self.model.player.x += 5
		if keys[pygame.K_SPACE]:
			self.model.player.vert_velocity += 5
		

		
class Main():
    
	def __init__(self):
		pygame.init()

		model = Model()
		controller = Controller(model)

		BLACK = (0, 0, 0)
		WHITE = (255, 255, 255)

		screen = pygame.display.set_mode((1280, 860), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
		pygame.display.set_caption("Game")

		screen_width = screen.get_width()
		screen_height = screen.get_height()

		end = False
		clock = pygame.time.Clock()

		while not end:
			model.update()
			controller.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					end = True
				elif event.type == pygame.VIDEORESIZE:
					screen_width = event.w
					screen_height = event.h
			
			screen.fill(WHITE)
			pygame.draw.rect(screen, BLACK, (model.player.x, (screen_height - model.player.h) - model.player.y, model.player.w, model.player.h))
			pygame.draw.rect(screen, (252, 3, 7), (model.enemy.x, (screen_height - model.enemy.h) - model.enemy.y, model.enemy.w, model.enemy.h))

			pygame.display.flip()

			clock.tick(60)

if __name__=="__main__":
	main = Main()