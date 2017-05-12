import pygame
import random
import time

pygame.init()

#spriteclass#
class rodent(pygame.sprite.Sprite):
    def __init__(self, color, width, height ):
        super(rodent, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

window_size = window_width, window_height = 800, 600
window = pygame.display.set_mode(window_size)

#variables for buttons and colors#
LEFT_BUTTON = 1
WHITE = (255, 255, 255)
BROWN = (100, 50, 25)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY_BLUE = (33, 66, 99)
LIGHT_GREY = (125, 125, 125)
PURPLE = (77, 55, 77)
colors = [LIGHT_GREY, BROWN, RED, GREEN, GREY_BLUE]
colors2 = [GREY_BLUE, RED, GREEN, BROWN, LIGHT_GREY]

#sprite variables#
grey_mouse = rodent(GREY_BLUE, 20, 20)
red_mouse = rodent(RED, 20, 20)
brown_cat = rodent(BROWN, 30, 30)
grey_mouse.rect.x = random.randrange(170, 650, 60)
grey_mouse.rect.y = random.randrange(20, 500, 60)
red_mouse.rect.x = random.randrange(170, 650, 60)
red_mouse.rect.y = random.randrange(20, 500, 60)
brown_cat.rect.x = random.randrange(165, 645, 60)
brown_cat.rect.y = random.randrange(15, 495, 60)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(grey_mouse, brown_cat, red_mouse)
all_sprites_list.draw(window)
all_sprites_list.update()

#random variables#
my_font = pygame.font.SysFont("", 30)
points = 0
catpoints = 0
y = 30

running = True

#drawing the mouseholes and mice#
for c in range(0, 8):

    x = 180

    for c2 in range(0, 8):
        pygame.draw.circle(window, WHITE, (x, y), 25, 25)
        x += 60
    y += 60
    all_sprites_list.add(grey_mouse, brown_cat)
    all_sprites_list.draw(window)
    pygame.display.update()

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        if grey_mouse.rect.collidepoint(event.pos) | red_mouse.rect.collidepoint(event.pos):
            points += 1
            y = 30

            running = True

            for c in range(0, 8):

                x = 180

                for c2 in range(0, 8):
                    pygame.draw.circle(window, WHITE, (x, y), 25, 25)
                    x += 60
                y += 60
            grey_mouse.rect.x = random.randrange(170, 650, 60)
            grey_mouse.rect.y = random.randrange(20, 500, 60)
            red_mouse.rect.x = random.randrange(170, 650, 60)
            red_mouse.rect.y = random.randrange(20, 500, 60)
            brown_cat.rect.x = random.randrange(165, 645, 60)
            brown_cat.rect.y = random.randrange(15, 495, 60)
            all_sprites_list.draw(window)
            all_sprites_list.update()
            pygame.display.update()
            print points

        if brown_cat.rect.collidepoint(event.pos):

            points = 0
            y = 30

            for c in range(0, 8):

                x = 180

                for c2 in range(0, 8):
                    pygame.draw.circle(window, WHITE, (x, y), 25, 25)
                    x += 60
                y += 60

            grey_mouse.rect.x = random.randrange(170, 650, 60)
            grey_mouse.rect.y = random.randrange(20, 500, 60)
            red_mouse.rect.x = random.randrange(170, 650, 60)
            red_mouse.rect.y = random.randrange(20, 500, 60)
            brown_cat.rect.x = random.randrange(165, 645, 60)
            brown_cat.rect.y = random.randrange(15, 495, 60)

            all_sprites_list.draw(window)
            all_sprites_list.update()
            pygame.display.update()

            if grey_mouse.rect.collidepoint(event.pos) == brown_cat.rect.collidepoint(event.pos):
                catpoints += 1

pygame.display.update()
pygame.quit()

