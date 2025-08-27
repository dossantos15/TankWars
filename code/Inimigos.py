from code.Const import ENTITY_SPEED, ENTITY_TIRO_DELAY
from code.InimigoTiro import InimigoTiro
from code.Entity import Entity


class Inimigos(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.tiro_delay = ENTITY_TIRO_DELAY[self.nome]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.nome]

    def tiro(self):
        self.tiro_delay -= 1
        if self.tiro_delay == 0:
            self.tiro_delay = ENTITY_TIRO_DELAY[self.nome]
            return InimigoTiro(name=f'{self.nome}Tiro', position=(self.rect.centerx, self.rect.centery))
        return None