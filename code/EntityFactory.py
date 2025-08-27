import random

from code.Fundo import Fundo
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Inimigos import Inimigos
from code.Jogadores import Jogadores


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Fundo(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Fundo(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Fundo(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Fundo(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Jogador1':
                return Jogadores('Jogador1', (10, WIN_HEIGHT / 2 - 30))
            case 'Jogador2':
                return Jogadores('Jogador2', (10, WIN_HEIGHT / 2 + 30))
            case 'Inimigo1':
                return Inimigos('Inimigo1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Inimigo2':
                return Inimigos('Inimigo2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))