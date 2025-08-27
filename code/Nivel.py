import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BRANCO, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TEMPO_NIVEL
from code.Inimigos import Inimigos
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Jogadores import Jogadores


class Nivel:
    def __init__(self, window: Surface, name: str, game_mode: str, jogador_ponto: list[int]):
        self.tempo = TEMPO_NIVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        jogador = (EntityFactory.get_entity('Jogador1'))
        jogador.ponto = jogador_ponto[0]
        self.entity_list.append(jogador)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            jogador = (EntityFactory.get_entity('Jogador2'))
            jogador.ponto = jogador_ponto[1]
            self.entity_list.append(jogador)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, jogador_ponto: list[int]):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Jogadores, Inimigos)):
                    tiro = ent.tiro()
                    if tiro is not None:
                        self.entity_list.append(tiro)
                if ent.name == 'Jogador1':
                    self.nivel_text(14, f'Jogador 1 - Vida: ({ent.health}) | Pontos: {ent.ponto}', C_BRANCO, (10, 25))
                if ent.name == 'Jogador2':
                    self.nivel_text(14, f'Jogador 2 - Vida: ({ent.health}) | Pontos: {ent.ponto}', C_BRANCO, (10, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Inimigo1', 'Inimigo2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.tempo -= TIMEOUT_STEP
                    if self.tempo == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Jogadores) and ent.name == 'Jogador1':
                                jogador_ponto[0] = ent.ponto
                            if isinstance(ent, Jogadores) and ent.name == 'Jogador2':
                                jogador_ponto[1] = ent.ponto
                        return True

                found_jogador = False
                for ent in self.entity_list:
                    if isinstance(ent, Jogadores):
                        found_jogador = True

                if not found_jogador:
                    return False

            self.nivel_text(14, f'{self.name} - Tempo: {self.tempo / 1000:.1f}s', C_BRANCO, (10, 5))
            self.nivel_text(14, f'fps: {clock.get_fps():.0f}', C_BRANCO, (10, WIN_HEIGHT - 35))
            self.nivel_text(14, f'entidades: {len(self.entity_list)}', C_BRANCO, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def nivel_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)