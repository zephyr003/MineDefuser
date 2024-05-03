import pygame
import random
import time
import networkx as nx
from settings import *
from book import *
#from logic_mswpr import *
pygame.init()

class Tile:
    def __init__(self, x, y, image, type, revealed = False, flagged = False, defused = True):
        self.x, self.y = x*TILESIZE, y*TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged
        self.defused = defused

    def draw(self, board_surface):
        if not self.flagged and self.revealed:      #display image if tile is revealed
            board_surface.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:    #display flag if tile is flagged
            board_surface.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:                     #display unknown tile if tile is not revealed
            board_surface.blit(tile_unknown, (self.x, self.y))

    def __repr__(self):     #to print the 'type' of the board elements in the terminal for reference
        return self.type


class Board:
    def __init__(self):
        self.board_surface = pygame.Surface((ROW*TILESIZE, HEIGHT))
        self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(ROW)] for col in range(COL)]
        #self.game_play = [[Tile(col, row, tile_unknown, ".") for row in range(ROW)] for col in range(COL)]
        self.place_mines()
        self.place_clues()
        self.stack=[]
        
    def place_mines(self): 
        self.mine_positions = []
        for i in range(AMOUNT_MINES):
            while True:
                x=random.randint(0, ROW-1)
                y=random.randint(0, COL-1)
                if self.board_list[x][y].type==".":
                    self.board_list[x][y].type="X"
                    self.board_list[x][y].image=tile_mine
                    self.board_list[x][y].defused = False
                    self.mine_positions.append((x,y))
                    break
        G=nx.erdos_renyi_graph(10,0.2)
        self.d=nx.to_dict_of_lists(G)

    def check_mines(self, x, y):       #function to calculate the number clues
        count=0
        for i in range (x-1, x+2):
            if (i<0) or (i>=ROW):
                continue
            for j in range(y-1, y+2):
                if (i==x and j==y) or (j<0) or (j>=COL):
                    continue
                if self.board_list[i][j].type=="X":
                    count+=1
        if count==0:
            self.board_list[x][y].type="/"
            self.board_list[x][y].image=tile_empty
        else:
            self.board_list[x][y].type="C"
            self.board_list[x][y].image=tile_numbers[count-1]

    def place_clues(self):      #function to place the number clues
        for x in range(ROW):
            for y in range(COL):
                if self.board_list[x][y].type!="X":
                    self.check_mines(x, y)

    def draw(self, screen):     #to display the board images
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0, 0))

    def open_tiles(self, x, y):
        self.stack.append((x, y))
        if self.board_list[x][y].type == "X":
            self.board_list[x][y].revealed = True
            self.board_list[x][y].image = tile_exploded
            return False
        elif self.board_list[x][y].type == "C":
            self.board_list[x][y].revealed = True
            return True
        
        self.board_list[x][y].revealed=True
        for row in range(max(0, x-1), min(ROW, x+2)):
            for col in range (max(0, y-1), min(COL, y+2)):
                if (row, col) not in self.stack:
                    self.open_tiles(row, col)
        return True

    def display_board(self):        #function to print stuff on the terminal
        print(self.mine_positions)
        #for i in self.board_list:
            #print(i)
        print(self.d)
        
class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.Surface((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(tile_exploded)
        self.MINES_TO_FIND=AMOUNT_MINES
        self.MINES_DIFFUSED=AMOUNT_MINES
        self.clock = pygame.time.Clock()
        self.new_game = False
        self.game_over=False

    def new(self):      #create new game
        self.board = Board()
        self.board.display_board()

    def run(self):      #game loop
        self.playing = True
        self.defusing = False
        self.exploded = False
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            if self.found_all_mines():
                time.sleep(3)
                print("sleep over")
        while self.defusing:
            self.clock.tick(FPS)
            self.event2()
            self.draw2()
        else:
            self.end_screen()
    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw(self):     #display stuff
        self.win.fill(WHITE)
        self.screen.fill(LIGHTGREY)
        self.board.draw(self.screen)
        #self.draw_text(f"Total mines:10", text_font, BLACK, (ROW+0.5)*TILESIZE, TILESIZE*2)
        self.draw_text(f"Mines to flag:{self.MINES_TO_FIND}", text_font, BLACK, (ROW+1)*TILESIZE, TILESIZE*2)
        self.draw_text(f"Mines to defuse:{self.MINES_DIFFUSED}", text_font, BLACK, (ROW+1)*TILESIZE, TILESIZE*3)
        self.new_game_rect = pygame.Rect(TILESIZE*(ROW+0.5), TILESIZE*7, TILESIZE*4, TILESIZE)
        self.screen.blit(button_new_game, (TILESIZE*(ROW+0.5), TILESIZE*7))
        self.win.blit(self.screen, (350, 140))
        pygame.display.flip()

    def found_all_mines(self):
        for row in self.board.board_list:
            for tile in row:
                if not tile.revealed and tile.type != "X":
                    return False
        return True
    
    def defused_all_mines(self):
        for row in self.board.board_list:
            for tile in row:
                if not tile.defused:
                    return False
        return True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:       #exiting game when clicking X
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                tile_x=(position[0]-350)//TILESIZE
                tile_y=(position[1]-140)//TILESIZE
                if event.button==3:
                    if tile_x<10 and tile_y<10:
                        if not self.board.board_list[tile_x][tile_y].revealed:
                            self.board.board_list[tile_x][tile_y].flagged = not self.board.board_list[tile_x][tile_y].flagged
                            if self.board.board_list[tile_x][tile_y].flagged:
                                self.MINES_TO_FIND = self.MINES_TO_FIND-1
                            else:
                                self.MINES_TO_FIND = self.MINES_TO_FIND+1
                        else:
                            for row in range(max(0, tile_x-1), min(ROW, tile_x+2)):
                                for col in range (max(0, tile_y-1), min(COL, tile_y+2)):
                                    if not self.board.board_list[row][col].revealed and not self.board.board_list[row][col].flagged:
                                        if not self.board.open_tiles(row, col):
                                            for r in self.board.board_list:
                                                for tile in r:
                                                    if tile.flagged and tile.type!="X":
                                                        tile.flagged=False
                                                        tile.revealed=True
                                                        tile.image=tile_not_mine
                                                    elif tile.type=="X":
                                                        tile.revealed=True
                                                        #tile.image=tile_mine
                                            self.playing=False
                                            self.exploded=True
                                            
                if event.button==1:
                    if tile_x<10 and tile_y<10:
                        if not self.board.board_list[tile_x][tile_y].flagged:
                            if not self.board.open_tiles(tile_x, tile_y):
                                for row in self.board.board_list:
                                    for tile in row:
                                        if tile.flagged and tile.type!="X":
                                            tile.flagged=False
                                            tile.revealed=True
                                            tile.image=tile_not_mine
                                        elif tile.type=="X":
                                            tile.revealed=True
                                            #tile.image=tile_mine
                                self.playing=False
                                self.exploded=True                                          
                    elif tile_x>=10:
                        if self.new_game_rect.collidepoint((position[0]-350, position[1]-140)):
                            print("Collidepoint")
                            self.new_game = True
                            self.end_screen()
                            
                if self.found_all_mines():
                    #self.done=True
                    self.playing=False
                    self.defusing = True
                    for row in self.board.board_list:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged=True
                    self.MINES_TO_FIND=0
                    
    def end_screen(self):
        while True:
            if not self.new_game:
                #if not self.playing and not self.defusing and not self.exploded:
                    #pygame.quit()
                    #quit(0)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:       #exiting game when clicking X
                        pygame.quit()
                        quit(0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        pos_x, pos_y = (position[0]-350), position[1]-140
                        if (position[0]-350)//TILESIZE>=10:
                            if self.new_game_rect.collidepoint((pos_x, pos_y)):
                                print("Collidepoint after explode")
                                self.new_game = True
                                self.end_screen()
            else:
                AMOUNT_MINES = 10
                self.MINES_TO_FIND = AMOUNT_MINES
                self.MINES_DIFFUSED = AMOUNT_MINES
                self.new_game = False
                game.new()
                game.run()

    def event2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                tile_x=(position[0]-350)//TILESIZE
                tile_y=(position[1]-140)//TILESIZE
                print(tile_x, tile_y)
                if event.button==1:
                    if tile_x<10 and tile_y<10:
                        tile=self.board.board_list[tile_x][tile_y]
                        if not tile.defused:
                            tile.defused = mini_main()
                            self.game_over=not(tile.defused)
                            if not self.game_over:
                                if tile.defused:
                                    self.MINES_DIFFUSED-=1
                                    self.board.board_surface.blit(green_mine, (tile.x, tile.y))
                                    idx = self.board.mine_positions.index((tile_x, tile_y))
                                    print(idx, ":", self.board.d[idx])
                                    for idx2 in self.board.d[idx]:
                                        print("idx2:",self.board.mine_positions[idx2])
                                        x2, y2=self.board.mine_positions[idx2]
                                        tile2=self.board.board_list[x2][y2]
                                        print(tile2.defused)
                                        if not tile2.defused:
                                            tile2.defused=True
                                            self.MINES_DIFFUSED-=1
                                            self.board.board_surface.blit(green_mine, (tile2.x, tile2.y))
                                            self.board.d.pop(idx2)
                                else:
                                    #self.game_over=False
                                    self.defusing=False
                                    print("You lost MineDefuser")
                                    
                    self.screen.blit(self.board.board_surface, (0, 0))
                    self.win.blit(self.screen, (350, 140))
                    pygame.display.update()
                if self.defused_all_mines():
                    time.sleep(2)
                    self.playing=False
                    self.defusing = False
                    print("You won MineDefuser")

        #print(self.game_over)
    def draw2(self):
        if self.game_over:
            self.win.fill(WHITE)
            self.win.blit(game_over, (196,0))
        else:
            self.screen.fill(LIGHTGREY)
            for row in self.board.board_list:
                for tile in row:
                    self.board.board_surface.blit(tile_empty, (tile.x, tile.y))
            for i in self.board.d:
                x1, y1 = self.board.mine_positions[i]
                for j in self.board.d[i]:
                        x2, y2 = self.board.mine_positions[j]
                        center_x1 = x1 * TILESIZE + TILESIZE // 2
                        center_y1 = y1 * TILESIZE + TILESIZE // 2
                        center_x2 = x2 * TILESIZE + TILESIZE // 2
                        center_y2 = y2 * TILESIZE + TILESIZE // 2
                        pygame.draw.line(self.board.board_surface, (70, 4, 102), (center_x1, center_y1), (center_x2, center_y2), 15)
            self.draw_text(f"Mines to flag:{self.MINES_TO_FIND}", text_font, BLACK, (ROW+1)*TILESIZE, TILESIZE*2)
            self.draw_text(f"Mines to defuse:{self.MINES_DIFFUSED}", text_font, BLACK, (ROW+1)*TILESIZE, TILESIZE*3)
            img = text_font.render("To defuse mine click on the mine", True, BLACK)
            self.win.blit(img, (550, 100))
            for row in self.board.board_list:
                for tile in row:
                    if not tile.defused:
                        self.board.board_surface.blit(red_mine, (tile.x, tile.y))
                    elif tile.defused and tile.type=="X":
                        self.board.board_surface.blit(green_mine, (tile.x, tile.y))

            self.screen.blit(self.board.board_surface, (0, 0))
            self.win.blit(self.screen, (350, 140))
        pygame.display.update()
        

text_font = pygame.font.SysFont("Arial", FONTSIZE)              
game = Game()
while True:
    game.new()
    game.run()