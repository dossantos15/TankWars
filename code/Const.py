import pygame

# C
C_AMARELO = (255, 255, 128)
C_BRANCO = (255, 255, 255)
C_PRETO = (0, 0, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Nivel1Bg0': 0,
    'Nivel1Bg1': 1,
    'Nivel1Bg2': 2,
    'Nivel1Bg3': 3,
    'Nivel1Bg4': 4,
    'Nivel1Bg5': 5,
    'Nivel2Bg0': 0,
    'Nivel2Bg1': 1,
    'Nivel2Bg2': 2,
    'Nivel2Bg3': 3,
    'Nivel2Bg4': 4,
    'Jogador1': 3,
    'Jogador1Tiro': 1,
    'Jogador2': 3,
    'Jogador2Tiro': 3,
    'Inimigo1': 1,
    'Inimigo1Tiro': 5,
    'Inimigo2': 1,
    'Inimigo2Tiro': 2,
}

ENTITY_VIDA = {
    'Nivel1Bg0': 999,
    'Nivel1Bg1': 999,
    'Nivel1Bg2': 999,
    'Nivel1Bg3': 999,
    'Nivel1Bg4': 999,
    'Nivel1Bg5': 999,
    'Nivel2Bg0': 999,
    'Nivel2Bg1': 999,
    'Nivel2Bg2': 999,
    'Nivel2Bg3': 999,
    'Nivel2Bg4': 999,
    'Jogador1': 150,
    'Jogador1Tiro': 1,
    'Jogador2': 150,
    'Jogador2Tiro': 1,
    'Inimigo1': 50,
    'Inimigo1Tiro': 2,
    'Inimigo2': 60,
    'Inimigo2Tiro': 2,
}

ENTITY_DAMAGE = {
    'Nivel1Bg0': 0,
    'Nivel1Bg1': 0,
    'Nivel1Bg2': 0,
    'Nivel1Bg3': 0,
    'Nivel1Bg4': 0,
    'Nivel1Bg5': 0,
    'Nivel2Bg0': 0,
    'Nivel2Bg1': 0,
    'Nivel2Bg2': 0,
    'Nivel2Bg3': 0,
    'Nivel2Bg4': 0,
    'Jogador1': 1,
    'Jogador1Tiro': 25,
    'Jogador2': 1,
    'Jogador2Tiro': 25,
    'Inimigo1': 1,
    'Inimigo1Tiro': 20,
    'Inimigo2': 1,
    'Inimigo2Tiro': 20,
}

ENTITY_SCORE = {
    'Nivel1Bg0': 0,
    'Nivel1Bg1': 0,
    'Nivel1Bg2': 0,
    'Nivel1Bg3': 0,
    'Nivel1Bg4': 0,
    'Nivel1Bg5': 0,
    'Nivel2Bg0': 0,
    'Nivel2Bg1': 0,
    'Nivel2Bg2': 0,
    'Nivel2Bg3': 0,
    'Nivel2Bg4': 0,
    'Jogador1': 0,
    'Jogador1Tiro': 0,
    'Jogador2': 0,
    'Jogador2Tiro': 0,
    'Inimigo1': 100,
    'Inimigo1Tiro': 0,
    'Inimigo2': 125,
    'Inimigo2Tiro': 0,
}

ENTITY_TIRO_DELAY = {
    'Jogador1': 20,
    'Jogador2': 15,
    'Inimigo1': 100,
    'Inimigo2': 200,
}

# M
MENU_OPTION = ('NOVO JOGO 1P',
               'NOVO JOGO 2P - COOPERATIVO',
               'NOVO JOGO 3P - COMPETITIVO',
               'PONTOS',
               'SAIR',)

# P
PLAYER_KEY_UP = {'Jogador1': pygame.K_UP,
                 'Jogador2': pygame.K_w}
PLAYER_KEY_DOWN = {'Jogador1': pygame.K_DOWN,
                    'Jogador2': pygame.K_s}
PLAYER_KEY_LEFT = {'Jogador1': pygame.K_LEFT,
                    'Jogador2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Jogador1': pygame.K_RIGHT,
                    'Jogador2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Jogador1': pygame.K_RCTRL,
                    'Jogador2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100
TEMPO_NIVEL = 20000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
PONTOS_POS = {
    'Titulo': (WIN_WIDTH / 2, 50),
    'DigiteNome': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Nome': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}