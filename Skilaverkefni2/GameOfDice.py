import pygame
import random


class Dice:
    def __init__(self):
        self.number = 0

    def throw(self):
        self.number = random.randint(1, 6)
        return self.number


class DiceThrower:
    def __init__(self, how_many=5):
        self.number_of_dice = how_many
        self.dice = Dice()
        self.dice_list = [-1 for i in range(self.number_of_dice)]

    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = self.dice.throw()
        return self.dice_list

    def rethrow(self, rethrow_list=[]):
        if 0 < len(rethrow_list) <= self.number_of_dice:
            if min(rethrow_list) >= 0 and max(rethrow_list) <= self.number_of_dice - 1:
                for item in rethrow_list:
                    self.dice_list[item] = self.dice.throw()
            return self.dice_list
        else:
            return self.throw()

pygame.init()

window_size = window_width, window_height = 640, 400
window = pygame.display.set_mode(window_size)

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

player_array = []
computer_array = []
player_dice = DiceThrower()
computer_dice = DiceThrower()

box_position = 120

pygame.display.set_caption("Game of Dice")

my_font = pygame.font.SysFont("", 30)
label_3 = my_font.render("Throw All", 1, WHITE)
label_4 = my_font.render("Throw One", 1, WHITE)
label_5 = my_font.render("Play", 1, WHITE)
complete = my_font.render("Finish", 1, WHITE)

running = True

for b in range(0, 5):
    computer = pygame.draw.rect(window, colors[b], pygame.Rect(box_position, 30, 60, 60))
    player = pygame.draw.rect(window, colors2[b], pygame.Rect(box_position, 120, 60, 60))
    box_position += 90
    pygame.display.update()


play = pygame.draw.rect(window, PURPLE, pygame.Rect(120, 240, 120, 60))
throw_one = pygame.draw.rect(window, PURPLE, pygame.Rect(270, 240, 120, 60))
throw_all = pygame.draw.rect(window, PURPLE, pygame.Rect(420, 240, 120, 60))
finish = pygame.draw.rect(window, RED, pygame.Rect(270, 310, 120, 60))

window.blit(label_3, (430, 260))
window.blit(label_4, (275, 260))
window.blit(label_5, (155, 260))
window.blit(complete, (295, 330))
pygame.display.update()

while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        if play.collidepoint(event.pos):
            word_px = 140
            word_cx = 140
            com_box_position = 120
            pc_box_position = 120

            player_array = player_dice.throw()
            computer_array = computer_dice.throw()

            for ins in range(0, 5):
                label_2 = my_font.render(str(computer_array[ins]), 1, WHITE)
                computer = pygame.draw.rect(window, colors[ins], pygame.Rect(com_box_position, 30, 60, 60))
                window.blit(label_2, (word_cx, 50))
                word_cx += 90
                com_box_position += 90

            for ins in range(0, 4):
                label = my_font.render(str(player_array[ins]), 1, WHITE)
                player = pygame.draw.rect(window, colors2[ins], pygame.Rect(pc_box_position, 120, 60, 60))
                window.blit(label, (word_px, 140))
                word_px += 90
                pc_box_position += 90

            pygame.display.update()

        if throw_one.collidepoint(event.pos):
            throw = Dice()
            player_array[4] = throw.throw()

        if throw_all.collidepoint(event.pos):
            word_x = 140
            box_position = 120
            player_array = player_dice.throw()

            for ins in range(0, 4):
                label = my_font.render(str(player_array[ins]), 1, WHITE)
                player = pygame.draw.rect(window, colors2[ins], pygame.Rect(box_position, 120, 60, 60))
                window.blit(label, (word_x, 140))
                word_x += 90
                box_position += 90
            pygame.display.update()

        if finish.collidepoint(event.pos):

            pc_points = sum(player_array)
            com_points = sum(computer_array)

            print "You have " + str(pc_points) + " points."
            print "The Computer has " + str(com_points) + " points."

            if pc_points > com_points:
                print "You Win!"

            if com_points > pc_points:
                print "You Lose!"

            if com_points == pc_points:
                print "It's a tie."


pygame.display.update()
pygame.quit()
