import pygame
import random

pygame.init()

infoObject = pygame.display.Info()
width = infoObject.current_w
height = infoObject.current_h

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

font1 = pygame.font.SysFont('comicsans', 40)

print(pygame.FULLSCREEN)

class Player:

    def __init__(self, name):
        self.credit = 100
        self.debit = 0
        self.name = name
        self.private_key = random.randint(10, 100000000)
        self.public_key = random.randrange(10, 100000000)


def redrawWindow(win, player, image):
    win.fill((255,255,255))
    #image
    win.blit(image, (0, 0))

    #text
    text = font1.render('Name: '+str(player.name), 1, (255, 0, 0))
    win.blit(text, (10, 10))
    text = font1.render('Credit: ' + str(player.credit), 1, (255, 0, 0))
    win.blit(text, (10, 40))
    text = font1.render('Debit: ' + str(player.debit), 1, (255, 0, 0))
    win.blit(text, (10, 70))
    text = font1.render('Public Key: ' + str(player.public_key), 1, (255, 0, 0))
    win.blit(text, (10, 100))
    text = font1.render('Private Key: ' + str(player.private_key), 1, (255, 0, 0))
    win.blit(text, (10, 130))

    pygame.display.update()

def main(p):
    run = True

    clock = pygame.time.Clock()

    image = pygame.transform.scale(pygame.image.load(r'C:\Users\Isha Pranav\Desktop\miniProj\miniProject\images\bit.jpg'), (width, height))

    while run:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                    pygame.quit()

            redrawWindow(win, p, image)

p=Player('Pranav')
main(p)

