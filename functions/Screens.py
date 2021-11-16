import pygame
pygame.display.init()

screen_height = pygame.display.Info().current_h
screen_width = pygame.display.Info().current_w
screen = pygame.display.set_mode((screen_width, screen_height))

lowest_layer = pygame.surface.Surface((screen_width, screen_height))
middle_layer = pygame.surface.Surface((screen_width, screen_height), pygame.SRCALPHA, 32)
top_layer = pygame.surface.Surface((screen_width, screen_height), pygame.SRCALPHA, 32)

lowest_layer.fill((255,255,255))
