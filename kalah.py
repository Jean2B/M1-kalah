# -*- coding: utf-8 -*-
"""
M1 DFS - Jean & Félicien BERTRAND
"""

import pygame
import numpy as np

pygame.init()

#Résolution
WIDTH = 1000
HEIGHT = 400
FPS = 60

#Couleurs
BG_COLOR = (255, 180, 100)
TEXT_COLOR = (255, 0, 0) #Pions
TEXT2_COLOR = (0, 0, 255) #Joueurs
TEXT3_COLOR = (64, 0, 128) #Pions cliquables
#Nombre et taille des lignes et colonnes
LINE_COLOR = (80, 60, 40)
LINE_WIDTH = 15
NB_COL = 8
#Initialisation des pions et cases
COL_SIZE = WIDTH/NB_COL
PIONS = [3,3,3,3,3,3,0,3,3,3,3,3,3,0]
K1 = NB_COL-2 #6, indice du kalah 1
K2 = K1*2 + 1 #13, indice du kalah 2

clock = pygame.time.Clock()

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
        imgfont2 = font.render(str(PIONS[pion]), True, TEXT3_COLOR)
        if joueur == 0:
            if pion < K1:
                screen.blit(imgfont, (COL_SIZE*(K1-pion)+COL_SIZE/2, HEIGHT/4))
            elif pion == K1:
                screen.blit(imgfont, (COL_SIZE/2, HEIGHT/2))
            elif pion < K2:
                if PIONS[pion] == 0: #Pions non cliquables
                    screen.blit(imgfont, (COL_SIZE*(pion-K1)+COL_SIZE/2, HEIGHT*3/4))
                else: #Pions cliquables
                    screen.blit(imgfont2, (COL_SIZE*(pion-K1)+COL_SIZE/2, HEIGHT*3/4))
            else:
                screen.blit(imgfont, (WIDTH-COL_SIZE/2, HEIGHT/2))
            imgfont = font2.render(nom_j1, True, TEXT2_COLOR)
        elif joueur == 1:
            if pion < K1:
                if PIONS[pion] == 0: #Pions non cliquables
                    screen.blit(imgfont, (COL_SIZE*(pion+1)+COL_SIZE/2, HEIGHT*3/4))
                else: #Pions cliquables
                    screen.blit(imgfont2, (COL_SIZE*(pion+1)+COL_SIZE/2, HEIGHT*3/4))
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
        #Nombre de pions dans la case choisie
        pions = PIONS[K1+col]
        #Vérification case vide
        if pions == 0:
            return False
        #Vérification si le joueur rejoue
        pion_final = (pions+K1+col)%(K2+1) #Indice du dernier pion posé
        if (pion_final == K2):
            rejouer = True
        #Pions semés
        for pion in range(pions):
            PIONS[(K1+1+col+pion)%(K2+1)] += 1
            PIONS[K1+col] -= 1
            delay_display(300)
        #Vérification s'il y a récolte
        if pion_final > K1 and pion_final < K2 and (PIONS[pion_final] == 1):
            PIONS[K2] += PIONS[pion_final] + PIONS[K2-1-pion_final]
            PIONS[pion_final] = 0
            PIONS[K2-1-pion_final] = 0
            delay_display(300)
            
    else:
        #Nombre de pions dans la case choisie
        pions = PIONS[col-1]
        #Vérification case vide
        if pions == 0:
            return False
        #Vérification si le joueur rejoue
        pion_final = (col+pions-1)%(K2+1) #Indice du dernier pion posé
        if (pion_final == K1):
            rejouer = True
        #Pions semés
        for pion in range(pions):
            PIONS[(col+pion)%(K2+1)] += 1
            PIONS[col-1] -= 1
            delay_display(300)
        #Vérification s'il y a récolte
        if pion_final < K1 and (PIONS[pion_final] == 1):
            PIONS[K1] += PIONS[pion_final] + PIONS[K2-1-pion_final]
            PIONS[pion_final] = 0
            PIONS[K2-1-pion_final] = 0
            delay_display(300)

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

def end_check():
    end = False
    somme_j0 = 0
    somme_j1 = 0
    for pion in range(len(PIONS)):
        if pion < K1:
            somme_j1 += PIONS[pion]
        elif pion > K1 and pion < K2:
            somme_j0 += PIONS[pion]
    if somme_j0 == 0:
        for pion in range(K1):
            PIONS[K1] += PIONS[pion]
            PIONS[pion] = 0
            delay_display(300)
        end = True
    elif somme_j1 == 0:
        for pion in range(K1+1,K2):
            PIONS[K2] += PIONS[pion]
            PIONS[pion] = 0
            delay_display(300)
        end = True
    return end

def display_end():
    if PIONS[K1] < PIONS[K2]:
        msg = nom_j1 + " a gagné"
    elif PIONS[K1] > PIONS[K2]:
        msg = nom_j2 + " a gagné"
    else:
        msg = "Égalité"
    imgfont = font3.render(msg, True, TEXT2_COLOR)
    text_rect = imgfont.get_rect(center=(WIDTH/2, HEIGHT/2))
    pygame.draw.rect(screen, (255,255,255), text_rect)
    screen.blit(imgfont, text_rect)

joueur = 0 #Numéro du joueur à qui c'est le tour
rejouer = False #True si le joueur peut rejouer
game_over = False #True si la partie est terminée
running = True #True tant que le jeu tourne
ready = True #True tant qu'il est possible de cliquer (hors des animations)
ready_tick = 0 #Ticks du jeu en cours

display()

while running:
    for event in pygame.event.get():
        if not ready:
            #Délai avant d'accepter les clics
            ready = (pygame.time.get_ticks() > ready_tick + (FPS/2))
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and ready:
            #Appel des fonctions lors d'un tour
            mouseX = event.pos[0] 
            mouseY = event.pos[1] 
            clicked_col = int(mouseX // COL_SIZE)
            if clicked_col not in [0, NB_COL-1] \
                and mouseY >= HEIGHT/2 \
                and get_nb_pions(clicked_col) != 0:
                ready = False
                semer(clicked_col)
                delay_display(2000)
                game_over = end_check()
                if game_over:
                    display_end()
                else:
                    changer_joueur()
                    display_turn(2000)
                    ready_tick = pygame.time.get_ticks()
                print(PIONS)

    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()