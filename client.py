import pygame
import random

pygame.init()

infoObject = pygame.display.Info()
width = infoObject.current_w
height = infoObject.current_h

#FONTS
font1=pygame.font.SysFont('arial',80,bold=True)
font2=pygame.font.SysFont('arial',18,bold=True)
font3=pygame.font.SysFont('arial',60,bold=True,italic=True)

#COLOR
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Player:

    def __init__(self, name):
        self.credit = 100
        self.debit = 0
        self.name = name
        self.private_key = random.randint(10, 100000000)
        self.public_key = random.randrange(10, 100000000)

def LandingPage(win, player, image):
    win.fill(white)
    # image
    win.blit(image, (0, 0))

    # text
    text = font3.render('Name: ' + str(player.name), 1, black, white)  # 1 is for bold or italics (check)
    win.blit(text, (10, 10))
    text = font3.render('1: Transaction ', 1, black, white)
    win.blit(text, (10, 100))
    text = font3.render('2: Display Blockchain ', 1, black, white)
    win.blit(text, (10, 190))
    text = font3.render('3: Peer To peer ', 1, black, white)
    win.blit(text, (10, 280))
    text = font3.render('4: Blockchain security ', 1, black, white)
    win.blit(text, (10, 370))
    text = font3.render('5: Generate sha256 hash', 1, black, white)
    win.blit(text, (10, 460))

    pygame.display.update()

def welcome(win, player, image):

    win.fill(white)
    win.blit(image, (0,0))

    #texts
    text = font1.render('WELCOME TO HASH THE CASH', 1, black, white)

    # text1 = font3.render('made by:', True, white)
    # text2 = font3.render('Pranav', True, (0, 191, 255))
    # text3 = font3.render('Hardik', True, (0, 191, 255))
    # text4 = font3.render('Gokul', True, (0, 191, 255))

    midx = 25
    midy = height/2 - 300

    win.blit(text, (midx, midy))
    # win.blit(text1, (midx, midy + 100))
    # win.blit(text2, (midx, midy + 200))
    # win.blit(text3, (midx, midy + 300))
    # win.blit(text4, (midx, midy + 400))

    pygame.display.update()

def main(p):
    run = True

    clock = pygame.time.Clock()

    image = pygame.transform.scale(pygame.image.load(r'C:\Users\Isha Pranav\Desktop\miniProj\miniProject\images\bit.jpg'), (width, height))

    welcome(win, p, image)

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
                    
                if event.key == pygame.K_r:
                    LandingPage(win, p, image)

                if event.key == pygame.K_1:
                    transaction()
                if event.key == pygame.K_2:
                    
                if event.key == pygame.K_3:

                if event.key == pygame.K_4:

                if event.key == pygame.K_5:


p=Player('Pranav')
main(p)

