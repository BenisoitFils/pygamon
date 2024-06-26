import pygame
import pytmx
import pyscroll
from pygamon.map import MapManager
from pygamon.player import Player

class Game:
    def __init__(self):
        # Crear la ventana
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon-Aventure")

        # Generar un jugador
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

        self.pressed_old = "DOWN"

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
            self.pressed_old = 'UP'        
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
            self.pressed_old = 'DOWN' 
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
            self.pressed_old = 'LEFT' 
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
            self.pressed_old = 'RIGHT' 
        else:
            self.player.change_animation_stop('stop',self.pressed_old)

    def update(self):
        self.map_manager.update()

    def run(self):
        # Bucle principal
        clock = pygame.time.Clock()
        running = True
        while running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)
        pygame.quit()
