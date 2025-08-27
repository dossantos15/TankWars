import sys
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Nivel import Nivel
from code.Menu import Menu
from code.Ponto import Ponto


class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            ponto = Ponto(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                jogador_ponto = [0, 0]
                nivel = Nivel(self.window, 'Nivel1', menu_return, jogador_ponto)
                nivel_return = nivel.run(jogador_ponto)
                if nivel_return:
                    nivel = Nivel(self.window, 'Nivel2', menu_return, jogador_ponto)
                    nivel_return = nivel.run(jogador_ponto)
                    if nivel_return:
                        ponto.save(menu_return, jogador_ponto)

            elif menu_return == MENU_OPTION[3]:
                ponto.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pygame.quit()
                sys.exit()