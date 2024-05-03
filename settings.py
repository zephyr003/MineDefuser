import pygame
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGREY = (210, 210, 210)
BOMB_GREY = (152, 152, 152)
WINDOW_SIZE = (400, 200)
FONT_SIZE = 30
LIGHT_COLOUR = (255, 0, 0)
LIGHT_OFF = (100, 100, 100)

#game settings
TILESIZE = 80
ROW = 10
COL = 10
AMOUNT_MINES = 10
#MINES_TO_FIND = AMOUNT_MINES
WIDTH = TILESIZE * (ROW + 5)
HEIGHT = TILESIZE * COL
FPS = 60
TITLE = "MineDefuser"
FONTSIZE = 32


 
#importing images
tile_numbers = []
for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("images", f"Tile{i}.png")), (TILESIZE, TILESIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileEmpty.png")), (TILESIZE, TILESIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileExploded.png")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileFlag.png")), (TILESIZE, TILESIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileMine.png")), (TILESIZE, TILESIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileNotMine.png")), (TILESIZE, TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileUnknown.png")), (TILESIZE, TILESIZE))
button_new_game = pygame.transform.scale(pygame.image.load(os.path.join("images", "NewGameButton.png")), (TILESIZE*4, TILESIZE))
bomb_bg = pygame.image.load(os.path.join("images", "Bomb.png"))
red_mine = pygame.image.load(os.path.join("images", "redMinebloomON.png"))
green_mine = pygame.image.load(os.path.join("images", "greenMinebloomON.png"))
game_won = pygame.image.load(os.path.join("images", "game_won.png"))