import sys
from datetime import datetime

import pygame

from pygame import Surface, Rect
from pygame.constants import K_RETURN, KEYDOWN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import PONTOS_POS, MENU_OPTION, C_BRANCO, C_PRETO
from code.DBProxy import DBProxy


class Ponto:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/PontoBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, jogador_ponto: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.ponto_text(40, 'VOCÊ GANHOU!', C_PRETO, PONTOS_POS['Titulo'])
            text = 'Digite o nome do Jogador 1 (4 caracteres):'
            ponto = jogador_ponto[0]
            if game_mode == MENU_OPTION[0]:
                ponto = jogador_ponto[0]
            if game_mode == MENU_OPTION[1]:
                ponto = (jogador_ponto[0] + jogador_ponto[1]) / 2
                text = 'Digite o nome da equipe (4 caracteres):'
            if game_mode == MENU_OPTION[2]:
                if jogador_ponto[0] >= jogador_ponto[1]:
                    ponto = jogador_ponto[0]
                else:
                    ponto = jogador_ponto[1]
                    text = 'Digite o nome do Jogador 2 (4 caracteres):'
            self.ponto_text(20, text, C_PRETO, PONTOS_POS['DigiteNome'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'ponto' : ponto, 'date' : get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.ponto_text(20, name, C_BRANCO, PONTOS_POS['Nome'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.ponto_text(48, 'OS 10 MELHORES', C_PRETO, PONTOS_POS['Titulo'])
        self.ponto_text(20, '        NOME        PONTOS        DATA        ', C_PRETO, PONTOS_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_ponto = db_proxy.retrieve_top10()
        db_proxy.close()

        for jogador_ponto in list_ponto:
            id_, name, ponto, date = jogador_ponto
            self.ponto_text(20, f'{name}, {ponto:05d}, {date}', C_PRETO, PONTOS_POS[list_ponto.index(jogador_ponto)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def ponto_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f"{current_date} - {current_time}"