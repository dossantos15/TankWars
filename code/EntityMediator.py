from code.Const import WIN_WIDTH
from code.Inimigos import Inimigos
from code.InimigoTiro import InimigoTiro
from code.Entity import Entity
from code.Jogadores import Jogadores
from code.JogadorTiro import JogadorTiro


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Inimigos):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, JogadorTiro):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, InimigoTiro):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Inimigos) and isinstance(ent2, JogadorTiro):
            valid_interaction = True
        elif isinstance(ent1, JogadorTiro) and isinstance(ent2, Inimigos):
            valid_interaction = True
        elif isinstance(ent1, Jogadores) and isinstance(ent2, InimigoTiro):
            valid_interaction = True
        elif isinstance(ent1, InimigoTiro) and isinstance(ent2, Jogadores):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.nome
                ent2.last_dmg = ent1.nome

    @staticmethod
    def __giv_ponto(inimigo: Inimigos, entity_list: list[Entity]):
        if inimigo.last_dmg == 'Jogador1Tiro':
            for ent in entity_list:
                if ent.nome == 'Jogador1':
                    ent.ponto += inimigo.ponto
        elif inimigo.last_dmg == 'Jogador2Tiro':
            for ent in entity_list:
                if ent.nome == 'Jogador2':
                    ent.ponto += inimigo.ponto

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Inimigos):
                    EntityMediator.__giv_ponto(ent, entity_list)
                entity_list.remove(ent)