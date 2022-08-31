import pymunk
import pymunk.pygame_util
import pygame

GRAY = (220, 220, 220)
space = pymunk.Space()
space.gravity = 0, 900
b0 = space.static_body

class App:
    size = 700, 240
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    

            self.screen.fill(GRAY)
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.001)

            print(circle.body.position)

        pygame.quit()

if __name__ == '__main__':
    p0, p1 = (0, 100), (700, 240)
    segment2 = pymunk.Segment(b0, (700,0), (700, 240),4)
    segment2.elasticity = 0.1

    segment = pymunk.Segment(b0, p0, p1, 4)
    segment.elasticity = 1
    segment.friction = 0.5



    body = pymunk.Body(mass=1, moment=10)
    body.position = (100, 0)



    circle = pymunk.Circle(body, radius=30)
    circle.elasticity = 0.95
    circle.friction = 0.5
    space.add(body, circle, segment, segment2)

    App().run()