import pygame.time

from Graphic_Functions import *

draw_robot(base_1, head_1, armset_1, legset_1, stance="dancing", stance_sequence=15)
screen.blit(middle_layer, (0,0))
pygame.display.update()

interval = 75
sequence = 0
clock = pygame.time.Clock()
spot = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()

    dt = pygame.time.get_ticks()
    if dt > interval:
        middle_layer.fill((0))
        screen.fill((0))
        draw_robot(base_1, head_1, armset_1, legset_1, stance="terrible walking animation", stance_sequence=sequence, placement=(spot, 500))
        interval = dt + 75
        sequence += 1
        spot += 1
        if sequence == 18:
            sequence = 0
    screen.blit(lowest_layer, (0,0))
    screen.blit(middle_layer, (0,0))
    pygame.display.update()