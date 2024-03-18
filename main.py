import pygame 
import time
import random

#creating a window

WIDTH,HEIGHT = 1000,600
WIN =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space Dodge")

BG =pygame.transform.scale(pygame.image.load("bj.jpg"), (WIDTH,HEIGHT))


def draw():
    WIN.blit(BG, (0, 0))
    pygame.display.update()


def main():
    run= True

    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run =False
                break

            draw()

    pygame.quit()        

if __name__ == "__main__":
    main()                        