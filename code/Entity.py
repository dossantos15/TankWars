from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_VIDA, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.nome = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_VIDA[self.nome]
        self.damage = ENTITY_DAMAGE[self.nome]
        self.ponto = ENTITY_SCORE[self.nome]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass