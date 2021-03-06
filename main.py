import os
import pygame, random, sys
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(200, 70)

fps = 30
width = 600
height = 600
new_asteroid_tick = 40

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Пояс астероидов')
pygame.mouse.set_visible(False)

player = None
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()