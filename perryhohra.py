## NASTAVENI PROSTŘEDÍ
# vkládá potřebné moduly
import pygame
import random
import math

# startuje moduly pygame
pygame.init()

## DISPLEJ
# vytváří displej/okno
screen = pygame.display.set_mode((828, 469))
# vytváří titulek s názvem na displeji
pygame.display.set_caption("Perryho hra")
# vytváří ikonku
perry2 = pygame.image.load("perry2.png")
pygame.display.set_icon(perry2)

## OBRÁZKY
# vkládá obrázek pozadí
BACKGROUND_IMAGE = pygame.image.load("background.jpg").convert()
# vkládá obrázek pozadí do levelu 2
BACKGROUND_IMAGE_2 = pygame.image.load("bg_img_3.png").convert()
# vkládá obrázek pozadí do levelu 3
BACKGROUND_IMAGE_3 = pygame.image.load("bg_img_2.png").convert()

# vkládá obrázek portalu a určuje, kde bude umístněn
portal = pygame.image.load("portal1.png")
portal_x = 700
portal_y = 140

portal2 = pygame.image.load("portal2.png")

# vkládá obrázek Perryho a určuje, kde bude umístněn
perry_image = pygame.image.load("perry.png")
perry_x = 50
perry_y = 300
# určuje, že se bude poloha obrázku měnit
perry_y_change = 0
perry_x_change = 0

# určuje, že bude na obrázku víc much (pôvodně to měli být jabka, proto se proměnné nazývají "apples" :D
apples = []
applesX = []
applesY = []
num_of_apples = 8
# přidává ke každé mouše obrázek a náhodní umístnění
for i in range(num_of_apples):
    apples.append(pygame.image.load("moucha_1.png"))
    applesX.append(random.randint(0, 735))
    applesY.append(random.randint(50, 350))

## SKÓRE
# vkládá proměnnou skóre
score_value = 0
# určuje vzhled textu skóre
font = pygame.font.Font('freesansbold.ttf', 24)
# určuje místo textu skóre
textX = 10
textY = 10


# vkládá proměnnou level
level_value = 1
font = pygame.font.Font('freesansbold.ttf', 24)
# určuje místo textu levelu
textX2 = 10
textY2 = 30

# vkládá vítězný obrázek
winner = pygame.image.load("vitez.png")

## FUNKCE ZOBRAZENÍ
# zobrazí skóre
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# zobrazí level
def show_level(x, y):
    level = font.render("LVL: " + str(level_value), True, (255, 255, 255))
    screen.blit(level, (x, y))


# zobrazí Perryho
def display_perry(x, y):
    screen.blit(perry_image, (x, y))


# zobrazí mouchy
def displayAPPLES(x, y, i):
    screen.blit(apples[i], (x, y))


# zobrazí pozadí
def display_background(x, y):
    screen.blit(BACKGROUND_IMAGE, (x, y))


# zobrazí pozadí v levelu 2
def display_bg_2(x, y):
    screen.blit(BACKGROUND_IMAGE_2, (x, y))

# zobrazí pozadí v levelu 3
def display_bg_3(x, y):
    screen.blit(BACKGROUND_IMAGE_3 , (x, y))


# zobrazí portál
def display_portal(x, y):
    screen.blit(portal, (x, y))

# zobrazí portál v levelu 2
def display_portal2(x, y):
    screen.blit(portal2, (x, y))


## FUNKCE JINÉ
# zjistí, jestli se Perry dotkl mouchy
def isCollisionApple(perry_x, perry_y, applesX, applesY):
    distance = math.sqrt((math.pow(perry_x - applesX, 2)) + (math.pow(perry_y - applesY, 2)))
    if distance < 16:
        return True
    else:
        return False


# zjistí, jestli se Perry dotkl portalu
def isCollisionPortal(perry_x, perry_y, portal_x, portal_y):
    distance = math.sqrt((math.pow(perry_x - portal_x, 2)) + (math.pow(perry_y - portal_y, 2)))
    if distance < 27:
        return True
    else:
        return False


# plus level
def lvl_up(level_value):
    level_value += 1

# zobrazí výhru
def win(x, y):
    screen.blit(winner, (x, y))


## HRA


#určí, kdy hra běží, a co se děje, když hra běží
running = True
while running:
    # popíše level 1
    if level_value == 1:
        screen.fill((0, 0, 0))
    # popíše, jaké změny vyvolají ruzné klávesy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    perry_x_change = 2
                if event.key == pygame.K_LEFT:
                    perry_x_change = -2
                if event.key == pygame.K_SPACE:
                    perry_y_change = -2
            if event.type == pygame.KEYUP:
                perry_y_change = 2
                perry_x_change = 0

        # dá Perrymu hranice, ať není mimo displej
        perry_y += perry_y_change
        if perry_y <= 0:
            perry_y = 0
        if perry_y >= 375:
            perry_y = 375

        perry_x += perry_x_change
        if perry_x <= -20:
            perry_x = -20
        if perry_x >= 740:
            perry_x = 740

        # vykoná funkci, která zobrazí obrázky pozadí a Perryho
        display_background(0, 0)
        display_perry(perry_x, perry_y)

        # vykoná funkci, která zobrazí a náhodně umístní mouchy
        for i in range(num_of_apples):
            displayAPPLES(applesX[i], applesY[i], i)

        # připočítá bod do skóre, vždy když se dotkne Perry mouchy
        collisionApple = isCollisionApple(perry_x, perry_y, applesX[i], applesY[i])
        if collisionApple:
            score_value += 1
            applesX[i] = random.randint(0, 735)
            applesY[i] = random.randint(50, 150)

        # zobrazí portal pokud je skóre více než požadované číslo
        if score_value > 9:
            display_portal(portal_x, portal_y)
            portal_x = 700
            portal_y = 140

        # zobrazí nový level po doteku s portalem
        collisionPortal = isCollisionPortal(perry_x, perry_y, portal_x, portal_y)
        if collisionPortal and score_value > 9:
            level_value += 1
            score_value = 0
            perry_x = 10
            perry_y = 10

        #zobrazí skóre a level
        show_score(textX, textY)
        show_level(textX2, textY2)

        # uplatní všechny provedené kliky a změny, aby byli na displeji vidět
        pygame.display.update()

    #LEVEL DVA
    elif level_value == 2:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    perry_x_change = 2
                if event.key == pygame.K_LEFT:
                    perry_x_change = -2
                if event.key == pygame.K_SPACE:
                    perry_y_change = -2
            if event.type == pygame.KEYUP:
                perry_y_change = 2
                perry_x_change = 0

        perry_y += perry_y_change
        if perry_y <= 0:
            perry_y = 0
        if perry_y >= 375:
            perry_y = 375

        perry_x += perry_x_change
        if perry_x <= -20:
            perry_x = -20
        if perry_x >= 740:
            perry_x = 740

        display_bg_2(0, 0)
        display_perry(perry_x, perry_y)

        for i in range(num_of_apples):
            displayAPPLES(applesX[i], applesY[i], i)

        collisionApple = isCollisionApple(perry_x, perry_y, applesX[i], applesY[i])
        if collisionApple:
            score_value += 1
            applesX[i] = random.randint(0, 735)
            applesY[i] = random.randint(50, 150)

        if score_value > 9:
            display_portal2(portal_x, portal_y)
            portal_x = 700
            portal_y = 140

        collisionPortal = isCollisionPortal(perry_x, perry_y, portal_x, portal_y)
        if collisionPortal and score_value > 9:
            level_value += 1
            score_value = 0
            perry_x = 10
            perry_y = 10

        show_score(textX, textY)
        show_level(textX2, textY2)
        pygame.display.update()

# LEVEL 3
    elif level_value == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    perry_x_change = 2
                if event.key == pygame.K_LEFT:
                    perry_x_change = -2
                if event.key == pygame.K_SPACE:
                    perry_y_change = -2
            if event.type == pygame.KEYUP:
                perry_y_change = 2
                perry_x_change = 0

        perry_y += perry_y_change
        if perry_y <= 0:
            perry_y = 0
        if perry_y >= 375:
            perry_y = 375

        perry_x += perry_x_change
        if perry_x <= 0:
            perry_x = 0
        if perry_x >= 740:
            perry_x = 740

        display_bg_3(0, 0)
        display_perry(perry_x, perry_y)

        for i in range(num_of_apples):
            displayAPPLES(applesX[i], applesY[i], i)

        collisionApple = isCollisionApple(perry_x, perry_y, applesX[i], applesY[i])
        if collisionApple:
            score_value += 1
            applesX[i] = random.randint(0, 735)
            applesY[i] = random.randint(50, 150)


        if score_value > 9:
            win(0, 0)

        collisionPortal = isCollisionPortal(perry_x, perry_y, portal_x, portal_y)
        if collisionPortal and score_value > 2:
            perry_x = 10
            perry_y = 10
            score = 0

        show_score(textX, textY)
        pygame.display.update()



pygame.quit()

