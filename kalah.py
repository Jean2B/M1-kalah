# -*- coding: utf-8 -*-
"""
M1 DFS - Jean & Félicien BERTRAND
"""

import pygame
import numpy as np

pygame.init()

#Sauvegarde
SAVEFILE = "kalah1.txt"

#Résolution
WIDTH = 1000
HEIGHT = 400
FPS = 60

#Couleurs
BG_COLOR = (255, 180, 100)
TEXT_COLOR = (255, 0, 0) #Pions
TEXT2_COLOR = (0, 0, 255) #Joueurs
TEXT3_COLOR = (64, 0, 128) #Pions cliquables
LINE_COLOR = (80, 60, 40)
#Nombre et taille des lignes et colonnes
LINE_WIDTH = 15
NB_COL = 8
COL_SIZE = WIDTH/NB_COL
#Initialisation des cases
K1 = NB_COL-2 #6, indice du kalah 1
K2 = K1*2 + 1 #13, indice du kalah 2

#Initialisation des pions
def set_pions():
    N = 3
    diff = input("Sélectionner la difficulté du jeu (1/2/3/4) : ")
    if (diff in ["1","2","3","4"]):
        N = int(diff) + 2
    else:
        print("Difficulté 1 par défaut")
    return [N,N,N,N,N,N,0,N,N,N,N,N,N,0]

PIONS_INIT = set_pions()

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
    for pion in range(len(pions)):
        imgfont = font.render(str(pions[pion]), True, TEXT_COLOR)
        imgfont2 = font.render(str(pions[pion]), True, TEXT3_COLOR)
        if joueur == 0:
            if pion < K1:
                screen.blit(imgfont, (COL_SIZE*(K1-pion)+COL_SIZE/2, HEIGHT/4))
            elif pion == K1:
                screen.blit(imgfont, (COL_SIZE/2, HEIGHT/2))
            elif pion < K2:
                if pions[pion] == 0: #Pions non cliquables
                    screen.blit(imgfont, (COL_SIZE*(pion-K1)+COL_SIZE/2, HEIGHT*3/4))
                else: #Pions cliquables
                    screen.blit(imgfont2, (COL_SIZE*(pion-K1)+COL_SIZE/2, HEIGHT*3/4))
            else:
                screen.blit(imgfont, (WIDTH-COL_SIZE/2, HEIGHT/2))
            imgfont = font2.render(nom_j1, True, TEXT2_COLOR)
        elif joueur == 1:
            if pion < K1:
                if pions[pion] == 0: #Pions non cliquables
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
        return pions[K1+col]
    else:
        return pions[col-1]
    

def semer(col):
    global pions,rejouer
    rejouer = False
    if joueur == 0:
        #Nombre de pions dans la case choisie
        nb_pions = pions[K1+col]
        #Vérification case vide
        if nb_pions == 0:
            return False
        #Vérification si le joueur rejoue
        pion_final = (nb_pions+K1+col)%(K2+1) #Indice du dernier pion posé
        if (pion_final == K2):
            rejouer = True
        #Pions semés
        for pion in range(nb_pions):
            pions[(K1+1+col+pion)%(K2+1)] += 1
            pions[K1+col] -= 1
            delay_display(300)
        #Vérification s'il y a récolte
        if pion_final > K1 and pion_final < K2 and (pions[pion_final] == 1):
            pions[K2] += pions[pion_final] + pions[K2-1-pion_final]
            pions[pion_final] = 0
            pions[K2-1-pion_final] = 0
            delay_display(300)
            
    else:
        #Nombre de pions dans la case choisie
        nb_pions = pions[col-1]
        #Vérification case vide
        if nb_pions == 0:
            return False
        #Vérification si le joueur rejoue
        pion_final = (col+nb_pions-1)%(K2+1) #Indice du dernier pion posé
        if (pion_final == K1):
            rejouer = True
        #Pions semés
        for pion in range(nb_pions):
            pions[(col+pion)%(K2+1)] += 1
            pions[col-1] -= 1
            delay_display(300)
        #Vérification s'il y a récolte
        if pion_final < K1 and (pions[pion_final] == 1):
            pions[K1] += pions[pion_final] + pions[K2-1-pion_final]
            pions[pion_final] = 0
            pions[K2-1-pion_final] = 0
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
        joueur = (joueur+1)%2

def end_check():
    end = False
    somme_j0 = 0
    somme_j1 = 0
    for pion in range(len(pions)):
        if pion < K1:
            somme_j1 += pions[pion]
        elif pion > K1 and pion < K2:
            somme_j0 += pions[pion]
    if somme_j0 == 0:
        for pion in range(K1):
            pions[K1] += pions[pion]
            pions[pion] = 0
            delay_display(300)
        end = True
    elif somme_j1 == 0:
        for pion in range(K1+1,K2):
            pions[K2] += pions[pion]
            pions[pion] = 0
            delay_display(300)
        end = True
    return end

def display_end():
    display()
    if pions[K1] < pions[K2]:
        msg = nom_j1 + " a gagné"
    elif pions[K1] > pions[K2]:
        msg = nom_j2 + " a gagné"
    else:
        msg = "Égalité"
    imgfont = font3.render(msg, True, TEXT2_COLOR)
    text_rect = imgfont.get_rect(center=(WIDTH/2, HEIGHT/2))
    pygame.draw.rect(screen, (255,255,255), text_rect)
    screen.blit(imgfont, text_rect)

pions = PIONS_INIT.copy()
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
                print(pions)
        
        if event.type == pygame.KEYDOWN and ready:
            #Bouton R : restart
            if event.key == pygame.K_r:
                ready = False
                pions = PIONS_INIT.copy()
                joueur = (joueur+1)%2
                rejouer = False
                game_over = False
                running = True
                display_turn(1000)
            
            #Bouton S : save
            if event.key == pygame.K_s:
                file = open(SAVEFILE, "w")
                savemsg = f'{pions}\t{joueur}\t{rejouer}\t{game_over}\t{nom_j1}\t{nom_j2}'
                file.write(savemsg)
                print("Sauvegardé dans", SAVEFILE)
                file.close()
            
            #Bouton L : load
            if event.key == pygame.K_l:
                file = open(SAVEFILE, "r")
                savelist = file.read().split('\t')
                pions = savelist[0].split("\t")[0][1:-1].split(", ")
                pions = [int(pion) for pion in pions]
                joueur = int(savelist[1])
                rejouer = savelist[2] == 'True'
                game_over = savelist[3] == 'True'
                nom_j1 = savelist[4]
                nom_j2 = savelist[5]
                if game_over:
                    display_end()
                else:
                    display_turn(1000)
                file.close()
            ready_tick = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()