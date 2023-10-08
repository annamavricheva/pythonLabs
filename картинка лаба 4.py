import pygame
from pygame.draw import *

pygame.init()

FPS = 30

#фон и картинка

screen = pygame.display.set_mode((1100, 600))
pygame.draw.rect(screen, (204,255, 255), (0, 0, 1100, 300), 0) #небо
pygame.draw.rect(screen, (0, 255, 0), (0, 300, 1100, 300), 0) #земля

#ствол
pygame.draw.rect(screen, (51, 0, 25), (730, 230, 25, 150), 0)

#крона

pygame.draw.circle(screen, (51, 102, 0), (740,145), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (740,145), 33, 1)
pygame.draw.circle(screen, (51, 102, 0), (700,180), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (700,180), 33, 1)
pygame.draw.circle(screen, (51, 102, 0), (780,180), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (780,180), 33, 1)
pygame.draw.circle(screen, (51, 102, 0), (740,200), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (740,200), 33, 1)
pygame.draw.circle(screen, (51, 102, 0), (710,230), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (710,230), 33, 1)
pygame.draw.circle(screen, (51, 102, 0), (770,230), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (770,230), 33, 1)

#дом

pygame.draw.rect(screen, (255,153, 51), (140, 240, 270, 200), 0)
pygame.draw.rect(screen, (0,0, 0), (140, 240, 270, 200), 1)
pygame.draw.rect(screen, (0,128, 255), (235, 310, 80, 60), 0)
pygame.draw.polygon(screen,( 255, 51, 51), ((140,240), (410,240), (275, 150)))
pygame.draw.polygon(screen,( 0, 0, 0), ((140,240), (410,240), (275, 150)), 1)

#облачко

pygame.draw.circle(screen, (255, 255, 255), (470,110), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (470,110), 33, 1)
pygame.draw.circle(screen, (255, 255, 255), (510,110), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (510,110), 33, 1)
pygame.draw.circle(screen, (255, 255, 255), (550,110), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (550,110), 33, 1)
pygame.draw.circle(screen, (255, 255, 255), (590,110), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (590,110), 33, 1)
pygame.draw.circle(screen, (255, 255, 255), (550,80), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (550,80), 33, 1)
pygame.draw.circle(screen, (255, 255, 255), (510,80), 33, 0)
pygame.draw.circle(screen, (0, 0, 0), (510,80), 33, 1)

#солнышко

pygame.draw.circle(screen, (255, 255, 0), (970,80), 60, 0)
pygame.draw.circle(screen, (0, 0, 0), (970,80), 60, 1)







pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
