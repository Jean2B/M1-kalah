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
TEXT_COLOR = (255, 0, 0) #Pions
TEXT2_COLOR = (0, 0, 255) #Joueurs
LINE_COLOR = (80, 60, 40)
LINE_WIDTH = 15
NB_COL = 8
COL_SIZE = WIDTH/NB_COL
PIONS = [3,3,3,17,3,3,0,3,3,3,3,3,3,0]
K1 = NB_COL-2 #6, indice du kalah 1
K2 = K1*2 + 1 #13, indice du kalah 2

nom_j1 = input("Nom joueur 1 : ")
nom_j2 = input("Nom joueur 2 : ")
if (nom_j1 == ""):
    nom_j1 = "Joueur 1"
if (nom_j2 == ""):
    nom_j2 = "Joueur 2"

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Kalah' )
sysfont = pygame.font.get_default_font() #Police d'écriture
font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 24)
font3 = pygame.font.SysFont(None, 60)

def draw_lines():
    for col in range(1, NB_COL):
        pygame.draw.line(screen, LINE_COLOR, (COL_SIZE*col, 0), (COL_SIZE*col, HEIGHT), LINE_WIDTH)
    
    pygame.draw.line(screen, LINE_COLOR, (COL_SIZE, HEIGHT/2), (WIDTH-COL_SIZE, HEIGHT/2), LINE_WIDTH)

def display_text():
    for pion in range(len(PIONS)):
        imgfont = font.render(str(PIONS[pion]), True, TEXT_COLOR)
        if joueur == 0:
            if pion < K1:
                screen.blit(imgfont, (COL_SIZE*(K1-pion)+COL_SIZE/2, HEIGHT/4))
            elif pion == K1:
                screen.blit(imgfont, (COL_SIZE/2, HEIGHT/2))
            elif pion < K2:
                screen.blit(imgfont, (COL_SIZE*(pion-K1)+COL_SIZE/2, HEIGHT*3/4))
            else:
                screen.blit(imgfont, (WIDTH-COL_SIZE/2, HEIGHT/2))
            imgfont = font2.render(nom_j1, True, TEXT2_COLOR)
        elif joueur == 1:
            if pion < K1:
                screen.blit(imgfont, (COL_SIZE*(pion+1)+COL_SIZE/2, HEIGHT*3/4))
            elif pion == K1:
                screen.blit(imgfont, (WIDTH-COL_SIZE/2, HEIGHT/2))
            elif pion < K2:
                screen.blit(imgfont, (COL_SIZE*(K2-pion)+COL_SIZE/2, HEIGHT/4))
            else:
                screen.blit(imgfont, (COL_SIZE/2, HEIGHT/2))
            imgfont = font2.render(nom_j2, True, TEXT2_COLOR)
        screen.blit(imgfont, (WIDTH-COL_SIZE+LINE_WIDTH, HEIGHT-LINE_WIDTH))

def display():
    screen.fill(BG_COLOR)
    draw_lines()
    display_text()

def get_nb_pions(col):
    if joueur == 0:
        return PIONS[K1+col]
    else:
        return PIONS[col-1]
    

def semer(col):
    global rejouer
    rejouer = False
    if joueur == 0:
        pions = PIONS[K1+col]
        if ((pions+K1+col)%(K2+1) == K2):
            rejouer = True
        if pions == 0:
            return False
        for pion in range(pions):
            PIONS[(K1+1+col+pion)%(K2+1)] += 1
            PIONS[K1+col] -= 1
            delay_display(300)
    else:
        pions = PIONS[col-1]
        if ((pions+col-1)%(K2+1) == K1):
            rejouer = True
        if pions == 0:
            return False
        for pion in range(pions):
            PIONS[(col+pion)%(K2+1)] += 1
            PIONS[col-1] -= 1
            delay_display(300)
    print(PIONS)

def delay_display(ms):
    pygame.time.delay(ms)
    display()
    pygame.display.update()
    
def display_turn(ms):
    display()
    msg = "Au tour de "
    if (joueur == 0):
        msg += nom_j1
    else:
        msg += nom_j2
    imgfont = font3.render(msg, True, TEXT2_COLOR)
    text_rect = imgfont.get_rect(center=(WIDTH/2, HEIGHT/2))
    pygame.draw.rect(screen, (255,255,255), text_rect)
    screen.blit(imgfont, text_rect)
    pygame.display.update()
    pygame.time.delay(ms)
    display()

def changer_joueur():
    global joueur, rejouer
    if not rejouer:
        if joueur == 0:
            joueur = 1
        else:
            joueur = 0

joueur = 0
rejouer = False
game_over = False
running = True

display()

while running:
    for event in pygame.event.get():
        ready = True
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            ready = False
            mouseX = event.pos[0] 
            mouseY = event.pos[1] 
            clicked_col = int(mouseX // COL_SIZE)
            if clicked_col not in [0, NB_COL-1] \
                and mouseY >= HEIGHT/2 \
                and get_nb_pions(clicked_col) != 0:
                semer(clicked_col)
                delay_display(2000)
                changer_joueur()
                display_turn(2000)
        if not ready:
            break

    pygame.display.update()
    
pygame.quit()