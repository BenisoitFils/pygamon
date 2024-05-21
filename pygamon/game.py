import pygame
import pytmx
import pyscroll
from pygamon.map import MapManager
from pygamon.player import Player




class Game:
    def __init__(self):
        # creer la fenetre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon-Aventure")


        #generer un joueur

        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)


    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')





    def update(self):
        self.map_manager.update()







        """if self.player == 'world' and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_house()
            self.map = 'house'


        if self.player == 'house' and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_world()
            self.map = 'world'"""






    def run(self):
        # boucle
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