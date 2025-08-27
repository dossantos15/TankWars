from code.Const import ENTITY_SPEED
from code.Entity import Entity


class JogadorTiro(Entity):

    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.nome]