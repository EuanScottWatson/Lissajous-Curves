import pygame, os, math
from pygame.locals import *


class Circle:
    def __init__(self, x, y, d_theta):
        self.x = x
        self.y = y
        self.draw_x = x
        self.draw_y = y - 50
        self.angle = 0
        self.delta_theta = d_theta

    def update(self):
        self.angle = (self.angle + self.delta_theta) % (2 * math.pi)
        self.draw_x = self.x + 50*math.cos(self.angle)
        self.draw_y = self.y + 50*math.sin(self.angle)


class Lissajous:
    def __init__(self):
        self.x_circles = []
        self.y_circles = []

        for i in range(5):
            self.x_circles.append(Circle(210 + 120 * i, 70, math.pi / 2**(4+i)))
            self.y_circles.append(Circle(70, 210 + 120 * i, math.pi / 2**(4+i)))

    def display(self, screen):
        for i in range(len(self.x_circles)):
            circle_x = self.x_circles[i]
            circle_y = self.y_circles[i]
            pygame.draw.circle(screen, (255, 255, 255), (circle_x.x, circle_x.y), 50, 1)
            pygame.draw.circle(screen, (255, 255, 255), (int(circle_x.draw_x), int(circle_x.draw_y)), 3, 0)
            pygame.draw.circle(screen, (255, 255, 255), (circle_y.x, circle_y.y), 50, 1)
            pygame.draw.circle(screen, (255, 255, 255), (int(circle_y.draw_x), int(circle_y.draw_y)), 3, 0)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True

    def display_screen(self, screen):
        screen.fill((0, 0, 0))

        self.display(screen)

        pygame.display.update()
        pygame.display.flip()

    def run_logic(self):
        for i in range(len(self.x_circles)):
            self.x_circles[i].update()
            self.y_circles[i].update()


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Arcade Machine")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    width, height = 760, 760

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    game = Lissajous()

    while not done:
        done = game.events()
        game.run_logic()
        game.display_screen(screen)

        clock.tick(60)


if __name__ == "__main__":
    main()
