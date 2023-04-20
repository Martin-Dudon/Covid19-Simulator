import pygame
from math import log10
from random import random as rand, uniform, randint
from pygame.locals import K_ESCAPE, K_a, K_z, K_r, K_t, K_d, KEYDOWN, QUIT

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Modèle d'épidémie")

C = pygame.time.Clock()

def maybe(num):
    '''sert surtout à gérer le début de l'épidémie où la progression des variables est lente
    arrondit à un entier proche de manière aléatoire en se basant sur la partie décimale du nombre à arrondir'''
    return int(num) + (rand() < num%1)

def add_text(pos,text,font=None,size=20,col=(0,0,0),bgcolor=(255,255,255)):
    screen.blit(pygame.font.SysFont(font,size).render(text,True,col,bgcolor),pos)

healthy, sick, dead, frame, rzero, recovered, days, lockdown_eff, lockdown_level, closed_borders, arrival_time, compliance, compl_factors, budget, research_speed, research_progress, research_bonus, keyon, game_ended = (
9999,1,0,0,3,0,0,1,0,False,randint(20,40),100,(0.05,0.03,-0.03,-0.05,-0.08,-0.15),1e6,0,0,0,False,False)
'''
initialisation de toutes les variables nécessaires :
    9999 personnes saines, 1 malade, 0 mort, 0 guéris
    "frame" n°0, jour 0
    r0 (nombre moyen de contaminations par 1 malade): 3
    confinement niveau 0, efficacité (puissance par niveau) 1, population obéissante à 100%
    frontières ouvertes, nouvelle arrivée de malades dans 20-40 jours
    budget 1000000 (10**6)
    obéissance augmente de 0,05/0,03/-0,03/-0,05/-0,08/-0,15 par jour au niveau 0/1/2/3/4/5 de confinement (affecte aussi la vitesse des campagnes de vaccination)

séparer chaque affectation si besoin de modifier ces valeurs
'''

running = True
while running:

    keyon = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

            if event.key == K_a:
                if not keyon and lockdown_level != 5:
                    budget -= 1e4*1.2**lockdown_level
                    lockdown_level += 1
            if event.key == K_z:
                if not keyon and lockdown_level:
                    budget += 5_000*1.1**lockdown_level
                    lockdown_level -= 1
            if event.key == K_r:
                if research_speed < 10 and not keyon:
                    research_speed += 1
            if event.key == K_t:
                if not keyon and research_speed:
                    research_speed -= 1
            if event.key == K_d:
                if not keyon:
                    closed_borders = not closed_borders
            keyon = True

    frame += 1
    if frame%10 == 0 and not game_ended:
        days += 1
        ##tous les calculs liés à l'épidémie
        d = maybe(sick/500) #morts
        rec = maybe(sick/max(15,30-days)) #guérisons
        ninf = maybe(min(healthy*0.15,sick*rzero/15)) #nouveaux cas
        healthy += rec-ninf
        sick -= rec-ninf+d
        dead += d
        if not sick and days < 40:
            sick = 1 #on ajoute 1 malade si la maladie est éliminée sous 40 jours
        arrival_time -= 0 if closed_borders else 1
        budget -= 125 if closed_borders else 0
        if not arrival_time:
            arrival_time = randint(35,49)
            sick *= uniform(1.05,1.1)
            sick = int(sick)
        recovered += maybe(rec*(healthy-recovered)/(healthy-recovered/3))
        recovered = max(recovered,healthy + sick)

        compliance += compl_factors[lockdown_level]
        budget -= 100*research_speed
        research_progress += research_speed + research_bonus
        research_bonus += 0.01 if research_speed else 0
        if research_progress >= 5000 or not sick:
            research_speed, research_bonus = 0,0
            game_ended = True


        if compliance > 105: compliance = 105
        lockdown_eff = compliance/100*min(1,days/(50))
        lockdown_factor = 1-0.15*lockdown_level*lockdown_eff
        rzero = (3*healthy-recovered)/healthy*lockdown_factor #l'épidémie se propage plus lentement si confinement activé

    screen.fill((240,20,0))
    add_text((0,0),f'Jour {days}',size=50)
    add_text((0,40),f'{healthy} personnes saines',size=50)
    add_text((0,80),f'{sick} malades',size=50)
    add_text((0,120),f'{dead} morts',size=50)
    add_text((0,160),f'Budget : {int(budget)}',size=50)
    add_text((0,200),f'Confinement niveau {lockdown_level}',size=50)
    add_text((0,240),f'Vaccin complété à {research_progress/50}%',size=50)
    if game_ended:
        add_text((200,200),'Vous avez gagné',size=80)
    pygame.display.flip()
    C.tick(30)

pygame.quit()
