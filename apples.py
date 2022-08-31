import pygame, pymunk, sys, time
pygame.init()


def create_apple(space, pos):
	body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
	body.position = pos
	shape = pymunk.Circle(body,20)
	space.add(body, shape)
	return shape

def draw_apples(apples):
	for apple in apples:
		pos_x = int(apple.body.position.x)
		pos_y = int(apple.body.position.y)
		apple_rect = apple_surface.get_rect(center = (pos_x, pos_y))
		screen.blit(apple_surface, apple_rect)
		


def create_ball(space, pos):
	body = pymunk.Body(body_type = pymunk.Body.STATIC)
	body.position = pos
	shape = pymunk.Circle(body,15)
	space.add(body, shape)
	return shape

def draw_balls(balls):
	for ball in balls:
		pos_x = int(ball.body.position.x)
		pos_y = int(ball.body.position.y)
		pygame.draw.circle(screen, (52, 101, 235), (pos_x, pos_y), 15)


width = 550
height = 550

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("apples!!!!")
clock = pygame.time.Clock()

space = pymunk.Space()#creating main pymunk physics space
space.gravity = (0, 75)#sets x and y gravity

apple_surface = pygame.image.load("assets/apple.png")
apple_surface = pygame.transform.scale(apple_surface, (40, 40))

#arrays to store the apples and ball objects
apples = []
balls = []

#creating the initial 2 balls when the game starts
balls.append(create_ball(space, (300, 300)))
balls.append(create_ball(space, (100, 400)))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			apples.append(create_apple(space, event.pos))

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
			balls.append(create_ball(space, event.pos))

	

	#deleting apples outside visible area
	for apple in apples:
		if apple.body.position.y > height:
			apples.remove(apple)
		if apple.body.position.y < 0:
			apples.remove(apple)


	print(len(apples), len(balls))

	screen.fill((217, 217, 217))

	draw_apples(apples)
	draw_balls(balls)
	space.step(1/40)

	pygame.display.update()
	clock.tick(120)

