import pygame
import random

WIDTH = 800
HEIGHT = 600

clouds = []

for i in range(8):
    clouds.append([
        random.randint(0, WIDTH),
        random.randint(20, 180),
        random.randint(60, 120)
    ])

birds = []

for i in range(10):
    birds.append([
        random.randint(0, WIDTH),
        random.randint(50, 250)
    ])


def drawSky(screen):

    for y in range(HEIGHT):
        c = int(255 - y * 0.2)
        pygame.draw.line(screen, (80, 170, c), (0, y), (WIDTH, y))


def drawSun(screen):

    pygame.draw.circle(screen, (255, 220, 0), (680, 90), 45)


def drawMountains(screen):

    pygame.draw.polygon(
        screen,
        (90, 90, 90),
        [(0, 400), (120, 230), (250, 400)]
    )

    pygame.draw.polygon(
        screen,
        (110, 110, 110),
        [(180, 400), (360, 170), (520, 400)]
    )

    pygame.draw.polygon(
        screen,
        (100, 100, 100),
        [(450, 400), (650, 200), (800, 400)]
    )


def drawGrass(screen):

    pygame.draw.rect(screen, (50, 170, 50), (0, 400, WIDTH, 200))


def drawRoad(screen):

    pygame.draw.rect(screen, (60, 60, 60), (0, 500, WIDTH, 100))

    for i in range(20):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (i * 50, 547, 25, 6)
        )


def drawClouds(screen):

    for c in clouds:

        pygame.draw.circle(screen, (255,255,255), (c[0], c[1]), 25)
        pygame.draw.circle(screen, (255,255,255), (c[0]+25, c[1]), 30)
        pygame.draw.circle(screen, (255,255,255), (c[0]+50, c[1]), 25)

        c[0] += 1

        if c[0] > WIDTH + 80:
            c[0] = -80


def drawTrees(screen):

    for i in range(12):

        x = 40 + i * 65

        pygame.draw.rect(screen, (100,60,20), (x,350,10,50))

        pygame.draw.circle(screen, (30,140,30), (x+5,340), 20)


def drawBuildings(screen):

    for i in range(5):

        x = 100 + i * 130

        pygame.draw.rect(screen, (120,120,150), (x,260,70,140))

        for r in range(4):
            for c in range(2):

                pygame.draw.rect(
                    screen,
                    (255,255,120),
                    (x+12+c*25,280+r*25,12,15)
                )


def drawBirds(screen):

    for b in birds:

        pygame.draw.arc(screen,(0,0,0),(b[0],b[1],20,10),0,3.14,2)

        b[0]+=2

        if b[0]>WIDTH:
            b[0]=-20