# -*- coding: utf-8 -*-
"""
M1 DFS - Jean & Félicien BERTRAND
"""

import pygame
import numpy as np
pygame.init()

WIDTH = 1000
HEIGHT = 400

BG_COLOR = (255, 180, 100)
TEXT_COLOR = (255, 0, 0)
LINE_COLOR = (80, 60, 40)
LINE_WIDTH = 15
NB_COL = 8
COL_SIZE = WIDTH/NB_COL


screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Kalah' )
sysfont = pygame.font.get_default_font() #Police d'écriture
font = pygame.font.SysFont(None, 48)
screen.fill( BG_COLOR )

def draw_lines():
    for col in range(1, NB_COL):
        pygame.draw.line(screen, LINE_COLOR, (COL_SIZE*col, 0), (COL_SIZE*col, HEIGHT), LINE_WIDTH)
    
    pygame.draw.line(screen, LINE_COLOR, (COL_SIZE, HEIGHT/2), (WIDTH-COL_SIZE, HEIGHT/2), LINE_WIDTH)

def display_text(texte, x, y):
    imgfont = font.render(texte, True, TEXT_COLOR)
    screen.blit(imgfont, (x,y))

draw_lines()
display_text("0", COL_SIZE/2, HEIGHT/2)
display_text("0", WIDTH-COL_SIZE/2, HEIGHT/2)
display_text("3", COL_SIZE+COL_SIZE/2, HEIGHT/4)
display_text("3", COL_SIZE*2+COL_SIZE/2, HEIGHT/4)
display_text("3", COL_SIZE*3+COL_SIZE/2, HEIGHT/4)
display_text("3", COL_SIZE*4+COL_SIZE/2, HEIGHT/4)
display_text("3", COL_SIZE*5+COL_SIZE/2, HEIGHT/4)
display_text("3", COL_SIZE*6+COL_SIZE/2, HEIGHT/4)
display_text("3", COL_SIZE+COL_SIZE/2, HEIGHT*3/4)
display_text("3", COL_SIZE*2+COL_SIZE/2, HEIGHT*3/4)
display_text("3", COL_SIZE*3+COL_SIZE/2, HEIGHT*3/4)
display_text("3", COL_SIZE*4+COL_SIZE/2, HEIGHT*3/4)
display_text("3", COL_SIZE*5+COL_SIZE/2, HEIGHT*3/4)
display_text("3", COL_SIZE*6+COL_SIZE/2, HEIGHT*3/4)


game_over = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    
pygame.quit()