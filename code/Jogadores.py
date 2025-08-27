import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_TIRO_DELAY
from code.Entity import Entity
from code.JogadorTiro import JogadorTiro


class Jogadores(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.tiro_delay = ENTITY_TIRO_DELAY[self.nome]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.nome]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.nome]
        if pressed_key[PLAYER_KEY_DOWN[self.nome]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.nome]
        if pressed_key[PLAYER_KEY_LEFT[self.nome]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.nome]
        if pressed_key[PLAYER_KEY_RIGHT[self.nome]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.nome]
        pass

    def tiro(self):
        self.tiro_delay -= 1
        if self.tiro_delay == 0:
            self.tiro_delay = ENTITY_TIRO_DELAY[self.nome]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.nome]]:
                return JogadorTiro(nome=f'{self.nome}Tiro', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None