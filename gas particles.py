import pygame, pymunk, sys, time, random
pygame.init()




class Ball():
	def __init__(self, pos, collision_type):
		self.body = pymunk.Body()
		self.body.position = pos
		self.body.velocity = (random.uniform(-100,100), random.uniform(-100,100))
		self.shape = pymunk.Circle(self.body, 10)
		self.shape.elasticity = 1
		self.shape.density = 1
		self.shape.collision_type = collision_type
		space.add(self.body, self.shape)


	def draw(self):
		pos_x = int(self.body.position.x)
		pos_y = int(self.body.position.y)


		if self.shape.collision_type != 1:
			pygame.draw.circle(screen, (255, 0, 0), (pos_x, pos_y), 10)
		else:
			pygame.draw.circle(screen, (0, 0, 255), (pos_x, pos_y), 10)


	def change_color(self, arbiter, space, body):
		self.shape.collision_type = 1


width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("bouncy")
clock = pygame.time.Clock()

space = pymunk.Space()#creating main pymunk physics space


balls = [Ball((random.randint(0, 600), random.randint(0, 600)), i+2) for i in range(100)]
balls.append(Ball((300,300), 1))

handlers = [space.add_collision_handler(1, i+2)for i in range(100)]

for i, handler in enumerate(handlers):
	handler.separate = balls[i].change_color

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		

	screen.fill((217, 217, 217))

	[ball.draw() for ball in balls]

	space.step(1/50)

	pygame.display.update()
	clock.tick(120)

