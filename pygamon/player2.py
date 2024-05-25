import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('personaje3.png')
       # self.scale = (30, 57)  # Definir el tamaño deseado para las imágenes escaladas
        self.image = self.get_image(115, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

        self.images = { 
            'down': {
                0: self.get_image(0, 0),
                1: self.get_image(250, 0)
            },
            'up': {
                0: self.get_image(0, 362),
                1: self.get_image(242, 362)
            },
            'left': {
                0: self.get_image(0, 115),
                1: self.get_image(242, 115)
            },
            'right': {
                0: self.get_image(0,235),
                1: self.get_image(242, 235)
            },
            'stop': {
                'DOWN': self.get_image(115, 0),
                'UP': self.get_image(115, 362),
                'LEFT': self.get_image(115, 115),
                'RIGHT': self.get_image(115, 235)
            }
        }

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.images_pactual = 0
        self.speed = 2
        self.animation_time = 0
        self.animation_speed = 200 

    def save_location(self):
        self.old_position = self.position.copy()

    def change_animation(self, name):
        now = pygame.time.get_ticks()
        if now - self.animation_time > self.animation_speed:
            self.animation_time = now
            self.images_pactual = (self.images_pactual + 1) % len(self.images[name])
            self.image = self.images[name][self.images_pactual]
            self.image.set_colorkey((0, 0, 0))
    
    def change_animation_stop(self, name, position):
        self.image = self.images[name][position]
        self.image.set_colorkey((0, 0, 0))

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

    def get_image(self, x, y):
        image = pygame.Surface([45, 85])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 45, 85))
        #image = pygame.transform.scale(image, self.scale)  # Escalar la imagen
        return image
