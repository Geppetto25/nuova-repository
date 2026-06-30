    ### APPUNTI PYGAME ###

import pygame
import sys

# Inizializza Pygame
pygame.init()
clock = pygame.time.Clock()

# Imposta dimensioni della finestra
larghezza = 800
altezza = 600
schermo = pygame.display.set_mode((larghezza, altezza))

# Imposta il titolo della finestra
pygame.display.set_caption("La mia prima finestra Pygame")

# Colore di sfondo (RGB)
colore_sfondo = (30, 30, 30)

# Ciclo principale del gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Riempie lo schermo con il colore di sfondo
    schermo.fill(colore_sfondo)

    #le cose riguardanti il gioco vanno scritte con questa indentatura

    # Aggiorna lo schermo
    pygame.display.flip()
    clock.tick(60)



#Rettangolo ed ellisse usano un rettangolo di riferimento: (x, y, larghezza, altezza)

pygame.draw.rect(schermo, (255, 0, 0), (100, 100, 200, 150), border_radius=5)

pygame.draw.ellipse(schermo, (0, 0, 255), (400, 100, 150, 80))


#Cerchio usa un centro e un raggio

pygame.draw.circle(schermo, (0, 255, 0), (300, 300), 50)


#Linea richiede due punti e uno spessore

pygame.draw.line(schermo, (255, 255, 0), (50, 50), (200, 200), 5)


#Poligono è super flessibile: basta una lista di coordinate

pygame.draw.polygon(schermo, (255, 0, 255), [(100, 100), (150, 50), (200, 100)])


#Arco è come un ellisse parziale, ma richiede angoli in radianti

pygame.draw.arc(schermo, (0, 255, 0), (100, 100, 200, 100), math.radians(0), math.radians(180), 5)

import math #va importato per l'arco


#PERSONAGGIO PRONTO
# Dimensioni del rettangolo
rect_width = 60
rect_height = 60

#colore
blu = (0, 120, 255)

# Calcolo posizione centrata
screen_rect = screen.get_rect()
rect_x = screen_rect.centerx - rect_width // 2
rect_y = screen_rect.centery - rect_height // 2

# Crea il rettangolo
player_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


#personaggio
# Dimensioni del rettangolo
rect_width = 30
rect_height = 30
rect_vel = 1.5

# Calcolo posizione centrata
rect_x = (larghezza - rect_width) // 2
rect_y = (altezza - rect_height) // 2

#lavora con griglie invece che pixel

def draw_grid(screen, width, height, block_size):
    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

def draw_object(schermo, colonna, riga, block_size):
    x = colonna * block_size
    y = riga * block_size
    rect = pygame.Rect(x, y, block_size, block_size)
    pygame.draw.rect(schermo, (255, 0, 0), rect)

def draw_sprite(schermo, sprite, colonna, riga, block_size):
    x = colonna * block_size
    y = riga * block_size
    schermo.blit(sprite, (x, y))



#importa immagini
sprite_image = pygame.image.load(r"C:\Users\mimmo\Downloads\francesco\download\sprite.png").convert_alpha()
#scala e ridimenziona immagini
sprite_image = pygame.transform.scale(sprite_image, (32, 64))



#MOVIMENTI
    #tutto indentato con while true
    # Movimento giocatore
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and rect_x > 0:
        rect_x -= rect_vel
    if keys[pygame.K_d] and rect_x < larghezza - rect_width:
        rect_x +=rect_vel
    if keys[pygame.K_w] and rect_y > 0:
        rect_y -= rect_vel
    if keys[pygame.K_s] and rect_y < altezza - rect_height:
        rect_y +=rect_vel




    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Hai premuto la barra spaziatrice!")

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            print("Hai rilasciato la barra spaziatrice!")

    #mouse
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Sinistro
            print("Clic sinistro")
        elif event.button == 3:  # Destro
            print("Clic destro")

    1 = sinistro
    2 = centrale (rotella)
    3 = destro
    4 = scroll su
    5 = scroll giù

    if event.type == pygame.MOUSEMOTION:
      print("Posizione:", event.pos)
    
    # Movimento ostacolo
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = 0
        obstacle_x = random.randint(0, WIDTH - obstacle_size)

    # Collisione
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_size, obstacle_size)
    if player_rect.colliderect(obstacle_rect):
        print("Hai perso!")
        pygame.quit()
        sys.exit()


# TESTI
#font
title_font = pygame.font.SysFont(None, 90)
#testi
b_click = b_font.render('Click', True, (0, 0, 0))
#posizionamento su schermo
schermo.blit(text, ((larghezza - larghezza//10), (altezza//18 )))
#get rect
bitcoin_rect = t_bitcoin.get_rect(center=(50 + (250//2),(altezza//5)*2 + 25 + 25))
