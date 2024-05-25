import pygame
import os

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, scale=(85, 125)):
        super().__init__()
        self.scale = scale  # Tamaño deseado para las imágenes escaladas
        
        # Cargar las imágenes individuales usando get_image
        self.images = {
            'down': {
                0: self.get_image('img/down_0.png'),
                1: self.get_image('img/down_1.png')
            },
            'up': {
                0: self.get_image('img/up_0.png'),
                1: self.get_image('img/up_1.png')
            },
            'left': {
                0: self.get_image('img/left_0.png'),
                1: self.get_image('img/left_1.png')
            },
            'right': {
                0: self.get_image('img/right_0.png'),
                1: self.get_image('img/right_1.png')
            },
            'stop': {
                'DOWN': self.get_image('img/stop_down.png'),
                'UP': self.get_image('img/stop_up.png'),
                'LEFT': self.get_image('img/stop_left.png'),
                'RIGHT': self.get_image('img/stop_right.png')
            }
        }

        self.image = self.images['stop']['DOWN']
        self.rect = self.image.get_rect()
        self.position = [x, y]

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.images_pactual = 0
        self.speed = 2
        self.animation_time = 0
        self.animation_speed = 200 

    def get_image(self, filepath):
        image = pygame.image.load(filepath).convert_alpha()
        image = pygame.transform.scale(image, self.scale)  # Redimensionar la imagen
        return image

    def save_location(self):
        self.old_position = self.position.copy()

    def change_animation(self, name):
        now = pygame.time.get_ticks()
        if now - self.animation_time > self.animation_speed:
            self.animation_time = now
            self.images_pactual = (self.images_pactual + 1) % len(self.images[name])
            self.image = self.images[name][self.images_pactual]

    def change_animation_stop(self, name, position):
        self.image = self.images[name][position]

    def move_right(self): self.position[0] += self.speed

    def move_left(self): self.position[0] -= self.speed

    def move_up(self): self.position[1] -= self.speed

    def move_down(self): self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

