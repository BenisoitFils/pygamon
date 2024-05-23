import sys
import os

# Añadir el directorio del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pygame
from pygamon.game import Game

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()

