import pygame, pymunk, sys, time
pygame.init()

bounce_sound = pygame.mixer.Sound('assets/bounce_sound.wav')


#not being used rn
def create_square(space, pos, vertices):
	body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
	body.position = pos
	shape = pymunk.Poly(body, vertices)
	shape.elasticity = 0.1
	shape.friction = 0.5
	
	space.add(body, shape)
	return shape, pos

def draw_squares(squares):
	for square in squares:
		print(square[0].body.position)
		p1 = int(square[0].body.position.x)
		p2 = int(square[0].body.position.y)
		pos = square[1][0]
		print(square)
		sq = pygame.Rect(p1,p2, 50, 50)
		pygame.draw.rect(screen, (255, 0, 0),sq)
		



def create_ball(space, pos):
	body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
	body.position = pos
	shape = pymunk.Circle(body,20)
	shape.elasticity = 1
	shape.friction = 0.5
	shape.collision_type = 1
	space.add(body, shape)
	return shape

def draw_balls(balls):
	for ball in balls:
		pos_x = int(ball.body.position.x)
		pos_y = int(ball.body.position.y)
		pygame.draw.circle(screen, (52, 101, 235), (pos_x, pos_y), 20)
		


def create_line(space, p1, p2):
	body = pymunk.Body(body_type = pymunk.Body.STATIC)
	shape = pymunk.Segment(body, p1, p2, 5)
	shape.elasticity = 1
	shape.friction = 0.5
	shape.collision_type = 2
	space.add(body, shape)
	return p1, p2, shape

def draw_lines(lines):
	for line in lines:
		p1 = line[0]
		p2 = line[1]

		pygame.draw.line(screen, (0, 255, 0) , p1, p2 , 12)


def collide(arbiter, space, data):
	global balls
	
	bounce_sound.play()

	return True


width = 800
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("bouncy!!")
clock = pygame.time.Clock()

space = pymunk.Space()#creating main pymink physics space
space.gravity = (0, 75)

squares = []
balls = []
lines = []

handler = space.add_collision_handler(1, 2)
handler.begin = collide

#squares.append(create_square(space, (50,50),[(-30, -30), (30, -30), (30, 30), (-30, 30)]))
lines.append(create_line(space,(0, 250),(800, 400)))

start_pos = (0, 0)
line_color = (217, 217, 217)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		

		#seein for left click and spawning balls
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			balls.append(create_ball(space, event.pos))
		

		#drawing lines code
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
			start_pos = event.pos	
			
			line_color = (0, 255, 0)
			
		if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
			end_pos = event.pos
			lines.append(create_line(space, start_pos, end_pos))

			#preview line color is turned to bg color so that it's not seen when user does not want to draw a line
			line_color = (217, 217, 217)

	
	
	screen.fill((217, 217, 217))

	#to display preview of the line that the player is drawing.
	end_pos= pygame.mouse.get_pos()
	pygame.draw.line(screen, line_color, start_pos, end_pos, 12)

	draw_squares(squares)
	draw_balls(balls)
	draw_lines(lines)

	space.step(1/50)

	pygame.display.update()
	clock.tick(120)

