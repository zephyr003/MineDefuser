import random, pygame
from time import sleep

import pygame.locals
import pygame.locals
from settings import *
screen_is_active=True
def mini_main():
    global screen,bomb,serial_no,serial_text,x,y,n,n1,games,book_manual,left_arrow,right_arrow, screen_is_active
    global show_book,pg_no,greenON,ledOFF,redON,game_over,t,timer_duration,clock,timer_value,book,book_manual
    global timer0,timer1,timer2,timer3,timer4,timer5,timer6,timer7,timer8,timer9, timerDecimal,timerColon, serial, s
    global bookpg1,bookpg2,bookpg3,bookpg4,bookpg5
    pygame.init()

    screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
    bomb=pygame.image.load("images/BOMB.png")
    serial_no = random.randint(100000000000,999999999999)
    serial_text=str(serial_no)
    x = 360
    y = 193
    screen_is_active = True
    n = random.randint(1,4)
    n1 = 4
    games = [ 'symbols', 'memory', 'ceasar', 'wires']

    timer0=pygame.image.load("images/timer0.png")
    timer1=pygame.image.load("images/timer1.png")
    timer2=pygame.image.load("images/timer2.png")
    timer3=pygame.image.load("images/timer3.png")
    timer4=pygame.image.load("images/timer4.png")
    timer5=pygame.image.load("images/timer5.png")
    timer6=pygame.image.load("images/timer6.png")
    timer7=pygame.image.load("images/timer7.png")
    timer8=pygame.image.load("images/timer8.png")
    timer9=pygame.image.load("images/timer9.png")
    timerColon=pygame.image.load("images/timerColon.png")
    timerDecimal=pygame.image.load("images/timerDecimal.png")

    book = pygame.image.load("images/book.png")
    bookpg1 = pygame.image.load("images/bookpg1.png")
    bookpg2 = pygame.image.load("images/bookpg2.png")
    bookpg3 = pygame.image.load("images/bookpg3.png")
    bookpg4 = pygame.image.load("images/bookpg4.png")
    bookpg5 = pygame.image.load("images/bookpg5.png")
    book_manual = [bookpg1,bookpg2,bookpg3,bookpg4,bookpg5]

    left_arrow=pygame.image.load("images/left_arrow.png")
    right_arrow=pygame.image.load("images/right_arrow.png")

    show_book = False   
    pg_no = 0

    serial0 = pygame.image.load("images/serial0.png")
    serial1 = pygame.image.load("images/serial1.png")
    serial2 = pygame.image.load("images/serial2.png")
    serial3 = pygame.image.load("images/serial3.png")
    serial4 = pygame.image.load("images/serial4.png")
    serial5 = pygame.image.load("images/serial5.png")
    serial6 = pygame.image.load("images/serial6.png")
    serial7 = pygame.image.load("images/serial7.png")
    serial8 = pygame.image.load("images/serial8.png")
    serial9 = pygame.image.load("images/serial9.png")
    serial =  pygame.image.load("images/serial.png")
    s={"0":serial0,"1":serial1,"2":serial2,"3":serial3,"4":serial4,"5":serial5,"6":serial6,"7":serial7,"8":serial8,"9":serial9}

    greenON = pygame.image.load("images/greenON.png")
    ledOFF = pygame.image.load("images/ledOFF.png")
    redON = pygame.image.load("images/redON.png")

    game_over = pygame.image.load("images/game_over.png")

    t={"0":timer0,"1":timer1,"2":timer2,"3":timer3,"4":timer4,"5":timer5,"6":timer6,"7":timer7,"8":timer8,"9":timer9,":":timerColon,".":timerDecimal}
    timer_duration = 120000
    clock = pygame.time.Clock()
    timer_value = timer_duration 
    defused=choose_game()
    return defused

def wires():
    global show_book, x, y, pg_no
    def sum(tuple1:tuple, tuple2:tuple):
        return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])

    def get_wire(cursor_pos):
        for real_wires_index in range(NO_OF_WIRES):
            rect = real_wire_rects[real_wires_index]
            if rect.collidepoint(cursor_pos):
                wire = real_wires[real_wires_index]
                cut_wire = CORRESP_CUT_WIRE[wire]
                position = ALL_WIRE_POS[real_wires_index]
                pos_y = position[1]

                pygame.draw.rect( screen, (152, 152, 152), (193+410, pos_y, 277, 46) )

                screen.blit(cut_wire, position)
                return real_wires_index

    def get_last_occurrence(wire):
        index = None
        reverse_real_wires = real_wires[::-1]
        for real_wire in reverse_real_wires:
            if real_wire == wire:
                index = NO_OF_WIRES - reverse_real_wires.index(wire) - 1

        return index
    
    def fifth_number(serial_no):
        fifth_digit = (serial_no // 10000000) % 10
        if fifth_digit % 2 != 0:
            return True
        else:
            return False

    def fourth_number(serial_no):
        fourth_digit = (serial_no // 100000000) % 10
        if fourth_digit % 2 != 0:
            return True
        else:
            return False
    
    def is_odd(serial_no):
        if serial_no%2!=0:
            return True
        else:
            return False
        
    def get_win_condition():
        win_condition = None

        if NO_OF_WIRES == 3:
            if red_wire not in real_wires:
                win_condition = 1
            elif real_wires[-1] == white_wire:
                win_condition = 2
            elif real_wires.count(blue_wire)>1:
                win_condition = get_last_occurrence(blue_wire)
            else:
                win_condition = 2
        
        elif NO_OF_WIRES == 4:
            if real_wires.count(red_wire)>1 and fifth_number(serial_no):
                win_condition = get_last_occurrence(red_wire)
            elif real_wires[-1] == yellow_wire and red_wire not in real_wires:
                win_condition = 0
            elif real_wires.count(blue_wire) == 1:
                win_condition = 0
            elif real_wires.count(yellow_wire) > 1:
                win_condition = 3
            else:
                win_condition = 1

        elif NO_OF_WIRES == 5:
            if real_wires[-1] == black_wire and fourth_number(serial_no):
                win_condition = 3
            elif real_wires.count(red_wire) == 1 and real_wires.count(yellow_wire) > 1:
                win_condition = 0
            elif black_wire not in real_wires:
                win_condition = 1
            else:
                win_condition = 0
        
        elif NO_OF_WIRES == 6:
            if yellow_wire not in real_wires and is_odd(serial_no):
                win_condition = 2
            elif real_wires.count(yellow_wire) == 1 and real_wires.count(white_wire) > 1:
                win_condition = 3
            elif red_wire not in real_wires:
                win_condition = 5
            else:
                win_condition = 3
        
        return win_condition

    screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)

    holder = pygame.image.load("images/HOLDER.png")
    red_wire = pygame.image.load("images/RED.png")
    blue_wire = pygame.image.load("images/BLUE.png")
    yellow_wire = pygame.image.load("images/YELLOW.png")
    white_wire = pygame.image.load("images/WHITE.png")
    black_wire = pygame.image.load("images/BLACK.png")
    cut_redwire = pygame.image.load("images/REDcut.png")
    cut_bluewire = pygame.image.load("images/BLUEcut.png")
    cut_yellowwire = pygame.image.load("images/YELLOWcut.png")
    cut_whitewire = pygame.image.load("images/WHITEcut.png")
    cut_blackwire = pygame.image.load("images/BLACK.png")

    BOMB_POS = (BOMB_X, BOMB_Y) = (410, 243)

    HOLDER_WRT_BOMB = (82, 83)
    HOLDER_POS = sum( BOMB_POS, HOLDER_WRT_BOMB )

    FIRST_WIRE_WRT_BOMB = (177, 104)
    FIRST_WIRE_POS = sum( BOMB_POS, FIRST_WIRE_WRT_BOMB )
    WIRE_POS_ADDENT = 70.80

    ALL_WIRES = (red_wire, black_wire, blue_wire, yellow_wire, white_wire)
    ALL_CUT_WIRES = (cut_redwire, cut_blackwire, cut_bluewire, cut_yellowwire, cut_whitewire)

    ALL_WIRE_POS = tuple( 
        sum(FIRST_WIRE_POS, (0, WIRE_POS_ADDENT*holder_no)) 
        for holder_no in range(0, 6)
    )
    CORRESP_CUT_WIRE = {
        wire : cut_wire
        for wire, cut_wire in zip( ALL_WIRES, ALL_CUT_WIRES )
    }

    NO_OF_WIRES = random.randint(3, 6)

    real_wires = [ 
        random.choice(ALL_WIRES) 
        for wire_no in range(NO_OF_WIRES) 
    ]

    real_wire_rects = [ 
        wire.get_rect() 
        for wire in real_wires 
    ]

    wire_to_cut = get_win_condition()

    colour_dict = {
        red_wire : 'red',
        black_wire : 'black',
        blue_wire : 'blue',
        yellow_wire : 'yellow',
        white_wire : 'white'
    }

    for index in range(NO_OF_WIRES):
        rect = real_wire_rects[index]
        rect.topleft = ALL_WIRE_POS[index]

    run = True
    screen_is_active = True
    while run:
        global show_book
        screen.fill((255, 255, 255))
        screen.blit(bomb, BOMB_POS)
        screen.blit(holder, HOLDER_POS)
        screen.blit(ledOFF,(669+x,283+y))
        screen.blit(serial,(50+x,50+y))
        
        screen.blit(book,(310+x,y-110))

        first_serial_pos =[1084,694]
        for i in range(len(serial_text)):
            for j in s:
                if j==serial_text[i]:
                    screen.blit(s[j],first_serial_pos)
                    first_serial_pos[0]+=24
        
        global timer_value
        timer_value -= clock.get_time()
        # Ensure timer value doesn't go below 0
        timer_value = max(timer_value, 0)
        timer_string = format_time(timer_value)
        first_digit_pos = [703+x,126+y]
        for i in range(len(timer_string)):
            for j in t:
                if j==timer_string[i]:
                    if i == 5:
                        screen.blit(timerDecimal,first_digit_pos)
                        first_digit_pos[0]+=12
                    elif timer_string[i] in "0123456789":
                        screen.blit(t[j],first_digit_pos)
                        first_digit_pos[0]+=47
                    else:
                        screen.blit(t[j],first_digit_pos)
                        first_digit_pos[0]+=12
        clock.tick(30)
        if timer_value == 0:
            print("Time's up!")
            screen.fill((255,255,255))
            screen.blit(game_over,(196,0))
            pygame.display.update()
            sleep(3)
            run = False
            return False

        index = 0
        for wire in real_wires:
            pos = ALL_WIRE_POS[index]
            screen.blit(wire, pos)
            index += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and screen_is_active:
                cursor_pos = pygame.mouse.get_pos()
                real_wire_index = get_wire(cursor_pos)
                if real_wire_index == wire_to_cut:
                    screen.blit(greenON,(669+x,283+y))
                    pygame.display.update()
                    print('YIPPEE!!! YOU DIDNT EXPLODE :3')
                    sleep(3)
                    screen_is_active = False
                    run = False
                    return True
                elif real_wire_index != None and real_wire_index != wire_to_cut:
                    screen.blit(redON,(669+x,283+y))
                    pygame.display.update()
                    sleep(2)
                    print('AWWW :( issoke just get better at the game idiot :3')
                    screen_is_active = False
                    screen.fill((255,255,255))
                    screen.blit(game_over,(196,0))
                    pygame.display.update()
                    sleep(3)
                    run = False
                    return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                show_book = True
        if show_book:
            screen.blit(book_manual[pg_no],(710+x,y-150))

            screen.blit(left_arrow,(660+x,315+y))
            left_arrow_rect = left_arrow.get_rect()
            left_arrow_rect.topleft = (660+x,315+y)
            screen.blit(right_arrow,(1410+x,315+y))
            right_arrow_rect = left_arrow.get_rect()
            right_arrow_rect.topleft = (1410+x,315+y)

            while show_book:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        run = False
                        show_book = False
                    elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        cursor_pos = pygame.mouse.get_pos()
                        if left_arrow_rect.collidepoint(cursor_pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                            pg_no = (pg_no-1)%len(book_manual)
                        elif right_arrow_rect.collidepoint(cursor_pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                            pg_no = (pg_no+1)%len(book_manual)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        show_book = False
                        break
                    screen.blit(book_manual[pg_no],(710+x,y-150))
                    pygame.display.update()
        pygame.display.update()

def symbols():
    global show_book, x, y, pg_no
    a=pygame.image.load("images/A.png")
    ae=pygame.image.load("images/ae.png")
    b=pygame.image.load("images/b.png")
    blackstar=pygame.image.load("images/blackstar.png")
    c=pygame.image.load("images/c.png")
    epsilon=pygame.image.load("images/epsilon.png")
    h=pygame.image.load("images/h.png")
    halfR=pygame.image.load("images/halfR.png")
    lambda1=pygame.image.load("images/lambda.png")
    n=pygame.image.load("images/n.png")
    o=pygame.image.load("images/o.png")
    omega=pygame.image.load("images/omega.png")
    para=pygame.image.load("images/para.png")
    phi=pygame.image.load("images/phi.png")
    question=pygame.image.load("images/question.png")
    six=pygame.image.load("images/six.png")
    smiley=pygame.image.load("images/smiley.png")
    snake=pygame.image.load("images/snake.png")
    spider=pygame.image.load("images/spider.png")
    star=pygame.image.load("images/star.png")
    stitch=pygame.image.load("images/stitch.png")
    theta=pygame.image.load("images/theta.png")
    w=pygame.image.load("images/w.png")
    weirdcleft=pygame.image.load("images/weirdcleft.png")
    weirdcright=pygame.image.load("images/weirdcright.png")
    x0=pygame.image.load("images/x.png")
    xi=pygame.image.load("images/XI.png")
    presseda=pygame.image.load("images/pressedA.png")
    pressedae=pygame.image.load("images/pressedae.png")
    pressedb=pygame.image.load("images/pressedb.png")
    pressedblackstar=pygame.image.load("images/pressedblackstar.png")
    pressedc=pygame.image.load("images/pressedc.png")
    pressedepsilon=pygame.image.load("images/pressedepsilon.png")
    pressedh=pygame.image.load("images/pressedh.png")
    pressedhalfR=pygame.image.load("images/pressedhalfR.png")
    pressedlambda1=pygame.image.load("images/pressedlambda.png")
    pressedn=pygame.image.load("images/pressedn.png")
    pressedo=pygame.image.load("images/pressedo.png")
    pressedomega=pygame.image.load("images/pressedomega.png")
    pressedpara=pygame.image.load("images/pressedpara.png")
    pressedphi=pygame.image.load("images/pressedphi.png")
    pressedquestion=pygame.image.load("images/pressedquestion.png")
    pressedsix=pygame.image.load("images/pressedsix.png")
    pressedsmiley=pygame.image.load("images/pressedsmiley.png")
    pressedsnake=pygame.image.load("images/pressedsnake.png")
    pressedspider=pygame.image.load("images/pressedspider.png")
    pressedstar=pygame.image.load("images/pressedstar.png")
    pressedstitch=pygame.image.load("images/pressedstitch.png")
    pressedtheta=pygame.image.load("images/pressedtheta.png")
    pressedw=pygame.image.load("images/pressedw.png")
    pressedweirdcleft=pygame.image.load("images/pressedweirdcleft.png")
    pressedweirdcright=pygame.image.load("images/pressedweirdcright.png")
    pressedx0=pygame.image.load("images/pressedx.png")
    pressedxi=pygame.image.load("images/pressedXI.png")

    buttonHolder = pygame.image.load("images/buttonHolder.png")

    all_symbols={a:presseda,ae:pressedae,b:pressedb,blackstar:pressedblackstar,c:pressedc,
                 epsilon:pressedepsilon,h:pressedh,halfR:pressedhalfR,
                 lambda1:pressedlambda1,n:pressedn,o:pressedo,omega:pressedomega,para:pressedpara,
                 phi:pressedphi,question:pressedquestion,six:pressedsix,
                 smiley:pressedsmiley,snake:pressedsnake,spider:pressedspider,star:pressedstar,
                 stitch:pressedstitch,theta:pressedtheta,w:pressedw,weirdcleft:pressedweirdcleft,
                 weirdcright:pressedweirdcright,x0:pressedx0,xi:pressedxi}
    symbol_pos=[(251+x,215+y), (381+x,215+y), (251+x,345+y), (381+x,345+y)]

    l1=[o,a,lambda1,n,spider,x0,weirdcleft]
    l2=[epsilon,o,weirdcleft,theta,star,x0,question]
    l3=[c,w,theta,xi,halfR,lambda1,star]
    l4=[six,para,b,spider,xi,question,smiley]
    l5=[phi,smiley,b,weirdcright,para,snake,blackstar]
    l6=[six,epsilon,stitch,ae,phi,h,omega]

    all_lists=[l1,l2,l3,l4,l5,l6]
    real_sequence=random.choice(all_lists)
    real_sequence1=real_sequence[:]
    indices=[]
    ingame_sequence=[]

    for i in range(4):
        symbol=random.choice(real_sequence)
        ingame_sequence.append(symbol)
        indices.append(real_sequence1.index(symbol))
        real_sequence.remove(ingame_sequence[-1])

    ordered_indices=sorted(indices)
    #print(ordered_indices)

    symbol_rects=[]
    for i in ingame_sequence:
        symbol_rects.append(i.get_rect())

    for index in range(4):
        rect = symbol_rects[index]
        rect.topleft = symbol_pos[index]

    def get_symbol(index):
        return  ingame_sequence[index]

    def check_if_correct(clicked_symbol, win_condition):
        for i in ordered_indices:
            if clicked_symbol==real_sequence1[i]:
                print("YEPPP")
                ordered_indices.remove(i)
                if (not ordered_indices):
                    return 1
                break
            else:
                return -1
            
    run = True
    screen_is_active = True
    win_condition = 0
    while run:
        screen.fill((255, 255, 255))
        screen.blit(bomb,(50+x,50+y))
        screen.blit(buttonHolder,(50+x,50+y))
        screen.blit(ledOFF,(669+x,283+y))
        screen.blit(serial,(50+x,50+y))

        screen.blit(book,(310+x,y-110))

        first_serial_pos =[1084,694]
        for i in range(len(serial_text)):
            for j in s:
                if j==serial_text[i]:
                    screen.blit(s[j],first_serial_pos)
                    first_serial_pos[0]+=24

        global timer_value
        timer_value -= clock.get_time()

        # Ensure timer value doesn't go below 0
        timer_value = max(timer_value, 0)
        timer_string = format_time(timer_value)
        first_digit_pos = [703+x,126+y]
        for i in range(len(timer_string)):
            for j in t:
                if j==timer_string[i]:
                    if i == 5:
                        screen.blit(timerDecimal,first_digit_pos)
                        first_digit_pos[0]+=12
                    elif timer_string[i] in "0123456789":
                        screen.blit(t[j],first_digit_pos)
                        first_digit_pos[0]+=47
                    else:
                        screen.blit(t[j],first_digit_pos)
                        first_digit_pos[0]+=12
        clock.tick(30)
        if timer_value == 0:
            print("Time's up!")
            screen.fill((255,255,255))
            screen.blit(game_over,(196,0))
            pygame.display.update()
            sleep(3)
            run = False
            return False
        
        for i in range(4):
            screen.blit(ingame_sequence[i] , symbol_pos[i])
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and screen_is_active:
                cursor_pos = pygame.mouse.get_pos()
                for i in symbol_rects:
                    if  i.collidepoint(cursor_pos):
                        index=symbol_rects.index(i)
                        pressed_symbol=get_symbol(index)
                        pressed_pos = symbol_pos[index]
                        screen.blit(all_symbols[pressed_symbol],pressed_pos)
                        pygame.display.update()
                        win_condition = check_if_correct(pressed_symbol, win_condition)
                        if (win_condition == 1):
                            screen.blit(greenON,(669+x,283+y))
                            pygame.display.update()
                            print("You win")
                            sleep(2)
                            screen_is_active = False
                            run = False
                            return True
                        elif (win_condition == -1):
                            screen.blit(redON,(669+x,283+y))
                            pygame.display.update()
                            print("You lose")
                            sleep(2)
                            screen_is_active = False
                            screen.fill((255,255,255))
                            screen.blit(game_over,(196,0))
                            #screen.blit(try_again,(750,720))
                            #try_again_rect = try_again.get_rect()
                            #try_again_rect.topleft = (750,720)
                            pygame.display.update()
                            #pygame.draw.rect(screen,(0,0,0),try_again_rect)
                            #if try_again_rect.collidepoint(cursor_pos):
                                #print("CLIEKCED")
                            sleep(3)
                            run = False
                            return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                show_book = True
        if show_book:
            screen.blit(book_manual[pg_no],(710+x,y-150))

            screen.blit(left_arrow,(660+x,315+y))
            left_arrow_rect = left_arrow.get_rect()
            left_arrow_rect.topleft = (660+x,315+y)
            screen.blit(right_arrow,(1410+x,315+y))
            right_arrow_rect = left_arrow.get_rect()
            right_arrow_rect.topleft = (1410+x,315+y)

            while show_book:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        run = False
                        show_book = False
                    elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        cursor_pos = pygame.mouse.get_pos()
                        if left_arrow_rect.collidepoint(cursor_pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                            pg_no = (pg_no-1)%len(book_manual)
                        elif right_arrow_rect.collidepoint(cursor_pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                            pg_no = (pg_no+1)%len(book_manual)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        show_book = False
                        break
                    screen.blit(book_manual[pg_no],(710+x,y-150))
                    pygame.display.update()
        pygame.display.update()
def ceasar():
    global show_book, x, y, pg_no
    word_dict = {0:["slick", "3.510 MHz"], 1:["trick", "3.520 MHz"], 2:["boxes", "3.530 MHz"], 3:["leaks", "3.540 MHz"], 4:["flick", "3.550 MHz"], 5:["break", "3.560 MHz"], 6:["steak", "3.570 MHz"], 7:["sting", "3.580 MHz"], 8:["beats", "3.590 MHz"]}
    letter = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"}
    freq_list = ["3.500", "3.510", "3.520", "3.530", "3.540", "3.550", "3.560", "3.570", "3.580", "3.590", "3.600"]
    pygame.init()

    TIMEREVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMEREVENT, 1000)

    num = random.randint(1, 3)
    x0 = num
    y0 = 4
    colour_on = True
    colour_break = False

    word_num = random.randint(0, 8)
    enc_word = ""
    #print(word_dict[word_num][0].upper())
    for l in word_dict[word_num][0].upper():
        enc_word = enc_word + letter[((ord(l)-65+num)%26)]

    win = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    
    POS_X = 220+x
    WORD_POS_Y = 410+y
    FREQ_POS_Y = 230+y
    
    freq_x = POS_X+105
    freq_y = FREQ_POS_Y+20
    word_x = POS_X+115
    word_y = WORD_POS_Y+20
    

    word_rect = pygame.Rect(POS_X, WORD_POS_Y, 320, 80)

    text_font = pygame.font.SysFont("Arial", FONTSIZE)
    word_img = text_font.render(enc_word, True, WHITE, BLACK)

    freq = "3.500 MHz"
    freq_indx = 0
    freq_img = text_font.render(freq, True, WHITE, BLACK)
    

    timer_surface =  pygame.Surface((200, 30))
    
    pygame.display.update()
    LIGHT = ledOFF
    playable = True
    running = True
    while running:
        win.fill(WHITE)
        timer_surface.fill(WHITE)
        win.blit(bomb_bg, (50+x, 50+y))
        win.blit(LIGHT,(669+x,283+y))
        pygame.draw.rect(win, BLACK, word_rect)
        win.blit(word_img, (word_x, word_y))
        pygame.draw.rect(win, BLACK, pygame.Rect(POS_X, FREQ_POS_Y, 320, 80))
        win.blit(freq_img, (freq_x, freq_y))
        pygame.draw.polygon(win, BLACK, ([POS_X-20, FREQ_POS_Y+5], [POS_X-20, FREQ_POS_Y+75], [POS_X-60, FREQ_POS_Y+40]), 0)
        pygame.draw.polygon(win, BLACK, ([POS_X+340, FREQ_POS_Y+5], [POS_X+340, FREQ_POS_Y+75], [POS_X+380, FREQ_POS_Y+40]), 0)

        screen.blit(serial,(50+x,50+y))

        win.blit(book,(440+x,y))
        book_rect =  book.get_rect()
        book_rect.topleft = (440+x,y)

        first_serial_pos =[1084,694]
        for i in range(len(serial_text)):
            for j in s:
                if j==serial_text[i]:
                    screen.blit(s[j],first_serial_pos)
                    first_serial_pos[0]+=24

        global timer_value
        timer_value -= clock.get_time()

        # Ensure timer value doesn't go below 0
        timer_value = max(timer_value, 0)
        timer_string = format_time(timer_value)
        first_digit_pos = [703+x,126+y]
        for i in range(len(timer_string)):
            for j in t:
                if j==timer_string[i]:
                    if i == 5:
                        win.blit(timerDecimal,first_digit_pos)
                        first_digit_pos[0]+=12
                    elif timer_string[i] in "0123456789":
                        win.blit(t[j],first_digit_pos)
                        first_digit_pos[0]+=47
                    else:
                        win.blit(t[j],first_digit_pos)
                        first_digit_pos[0]+=12
        clock.tick(30)

        if timer_value == 0:
            print("Time's up!")
            screen.fill((255,255,255))
            screen.blit(game_over,(196,0))
            pygame.display.update()
            sleep(3)
            running = False
            return False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == TIMEREVENT and playable:
                if colour_on==True and colour_break == False:
                    LIGHT = redON
                    colour_break = True
                    x0-=1
                    if x0==0:
                        colour_on = False
                        x0=num
                elif colour_on == True and colour_break == True:
                    LIGHT = ledOFF
                    colour_break = False
                else:
                    LIGHT = ledOFF
                    y0-=1
                    if y0==0:
                        colour_on = True
                        y0=4
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pygame.draw.polygon(win, BLACK, ([POS_X-20, FREQ_POS_Y+5], [POS_X-20, FREQ_POS_Y+75], [POS_X-60, FREQ_POS_Y+40]), 0).collidepoint(pos) and playable:
                    freq_indx = (freq_indx-1)%len(freq_list)
                    freq = f"{freq_list[freq_indx]} MHz"
                    freq_img = text_font.render(freq, True, WHITE, BLACK)
                if pygame.draw.polygon(win, BLACK, ([POS_X+340, FREQ_POS_Y+5], [POS_X+340, FREQ_POS_Y+75], [POS_X+380, FREQ_POS_Y+40]), 0).collidepoint(pos) and playable:
                    freq_indx = (freq_indx+1)%len(freq_list)
                    freq = f"{freq_list[freq_indx]} MHz"
                    freq_img = text_font.render(freq, True, WHITE, BLACK)
                if word_rect.collidepoint(pos) and playable:
                    playable = False
                    if word_dict[word_num][1] == freq:
                        win.blit(greenON,(669+x,283+y))
                        pygame.display.update()
                        print("win")
                        pygame.display.update()
                        sleep(2)
                        running = False
                        return True
                    else:
                        win.blit(redON,(669+x,283+y))
                        pygame.display.update()
                        print("Lose")
                        pygame.display.update()
                        sleep(2)
                        screen.fill((255,255,255))
                        screen.blit(game_over,(196,0))
                        pygame.display.update()
                        sleep(3)
                        running = False
                        return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                show_book = True
        if show_book:
            screen.blit(book_manual[pg_no],(710+x,y-150))

            screen.blit(left_arrow,(660+x,315+y))
            left_arrow_rect = left_arrow.get_rect()
            left_arrow_rect.topleft = (660+x,315+y)
            screen.blit(right_arrow,(1410+x,315+y))
            right_arrow_rect = left_arrow.get_rect()
            right_arrow_rect.topleft = (1410+x,315+y)

            while show_book:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        running = False
                        show_book = False
                    elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        cursor_pos = pygame.mouse.get_pos()
                        if left_arrow_rect.collidepoint(cursor_pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                            pg_no = (pg_no-1)%len(book_manual)
                        elif right_arrow_rect.collidepoint(cursor_pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                            pg_no = (pg_no+1)%len(book_manual)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        show_book = False
                        break
                    screen.blit(book_manual[pg_no],(710+x,y-150))
                    pygame.display.update()
        pygame.display.update()
def memory():
    global show_book, x, y, pg_no
    strike_no = 0
    def sum(tuple1: tuple, tuple2: tuple):
        return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

    def set_new_stage():
        global real_display, real_buttons, real_button_rects, stage_no
        if stage_no < 5:
            real_display = random.choice(ALL_DISPLAYS)

            all_buttons_to_pop = list(ALL_BUTTONS)
            real_buttons = [
                all_buttons_to_pop.pop(random.randint(0, 3 - button_no))
                for button_no in range(4)
            ]
            real_button_rects = [
                button.get_rect()
                for button in real_buttons
            ]
            for index in range(4):
                rect = real_button_rects[index]
                rect.topleft = ALL_BUTTON_POS[index]

    def advance_stage(index, label):
        global stage_no
        stage_data.append((index, label))
        set_new_stage()
        stage_no += 1

    def get_win_condition():
        win_label = None
        win_index = None

        if stage_no == 1:
            if real_display == display1:
                win_index = 1
            elif real_display == display2:
                win_index = 1
            elif real_display == display3:
                win_index = 2
            elif real_display == display4:
                win_index = 3

        elif stage_no == 2:
            if real_display == display1:
                win_label = 4
            elif real_display == display2:
                win_index = stage_data[0][0]
            elif real_display == display3:
                win_index = 0
            elif real_display == display4:
                win_index = stage_data[0][0]

        elif stage_no == 3:
            if real_display == display1:
                win_label = stage_data[1][1]
            elif real_display == display2:
                win_label = stage_data[0][1]
            elif real_display == display3:
                win_index = 2
            elif real_display == display4:
                win_label = 4

        elif stage_no == 4:
            if real_display == display1:
                win_index = stage_data[0][0]
            elif real_display == display2:
                win_index = 0
            elif real_display == display3:
                win_index = stage_data[1][0]
            elif real_display == display4:
                win_index = stage_data[1][0]

        elif stage_no == 5:
            if real_display == display1:
                win_label = stage_data[0][1]
            elif real_display == display2:
                win_label = stage_data[1][1]
            elif real_display == display3:
                win_label = stage_data[3][1]
            elif real_display == display4:
                win_label = stage_data[2][1]

        return win_index, win_label
    
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    display1 = pygame.image.load('images/DISPLAY 1.png')
    display2 = pygame.image.load('images/DISPLAY 2.png')
    display3 = pygame.image.load('images/DISPLAY 3.png')
    display4 = pygame.image.load('images/DISPLAY 4.png')
    button1 = pygame.image.load('images/BUTTON 1.png')
    button2 = pygame.image.load('images/BUTTON 2.png')
    button3 = pygame.image.load('images/BUTTON 3.png')
    button4 = pygame.image.load('images/BUTTON 4.png')

    strike = pygame.image.load("images/cross.png")
    strike_pos= [(790+x,326+y),(870+x,326+y),(950+x,326+y)]

    BOMB_POS = (BOMB_X, BOMB_Y) = (410, 243)

    DISPLAY_WRT_BOMB = (175, 150)
    DISPLAY_POS = sum(BOMB_POS, DISPLAY_WRT_BOMB)

    FIRST_BUTTON_WRT_BOMB = (175, 311)
    FIRST_BUTTON_POS = sum(BOMB_POS, FIRST_BUTTON_WRT_BOMB)
    BUTTON_POS_ADDENT = 79

    ALL_DISPLAYS = (display1, display2, display3, display4)
    ALL_BUTTONS = (button1, button2, button3, button4)

    ALL_BUTTON_POS = tuple(
        sum(FIRST_BUTTON_POS, (BUTTON_POS_ADDENT * button_no, 0))
        for button_no in range(0, 6)
    )

    CORRESP_LABEL = {
        ALL_BUTTONS[index]: index + 1
        for index in range(4)
    }

    global real_display, all_buttons_to_pop, real_buttons, real_button_rects
    real_display, all_buttons_to_pop, real_buttons, real_button_rects = None, None, None, None

    global stage_no
    stage_no = 1
    stage_data = []
    lives = 3  # Initialize lives

    set_new_stage()

    run = True

    while run:
        screen.fill((255, 255, 255))
        screen.blit(bomb, BOMB_POS)
        screen.blit(real_display, DISPLAY_POS)
        screen.blit(ledOFF,(669+x,283+y))
        screen.blit(serial,(50+x,50+y))

        screen.blit(book,(310+x,y-110))

        first_serial_pos =[1084,694]
        for i in range(len(serial_text)):
            for j in s:
                if j==serial_text[i]:
                    screen.blit(s[j],first_serial_pos)
                    first_serial_pos[0]+=24

        for i in range(strike_no):
            screen.blit(strike,strike_pos[i])
        
        index = 0

        global timer_value
        timer_value -= clock.get_time()

        # Ensure timer value doesn't go below 0
        timer_value = max(timer_value, 0)
        timer_string = format_time(timer_value)
        first_digit_pos = [703+x,126+y]
        for i in range(len(timer_string)):
            for j in t:
                if j==timer_string[i]:
                    if i == 5:
                        screen.blit(timerDecimal,first_digit_pos)
                        first_digit_pos[0]+=12
                    elif timer_string[i] in "0123456789":
                        screen.blit(t[j],first_digit_pos)
                        first_digit_pos[0]+=47
                    else:
                        screen.blit(t[j],first_digit_pos)
                        first_digit_pos[0]+=12
        clock.tick(30)
        if timer_value == 0:
            print("Time's up!")
            run = False
        for button in real_buttons:
            pos = ALL_BUTTON_POS[index]
            screen.blit(button, pos)
            index += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            
            elif stage_no >= 6:
                screen.blit(greenON,(669+x,283+y))
                pygame.display.update()
                print('YIPPEEE YOU WIN :3')
                sleep(3)
                run = False
                return True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = pygame.mouse.get_pos()
                for index in range(4):
                    rect = real_button_rects[index]
                    button = real_buttons[index]
                    label = CORRESP_LABEL[button]
                    if rect.collidepoint(cursor_pos):
                        win_index, win_label = get_win_condition()
                        print('Stage :', stage_no, '|| Pos =', index + 1, 'Label =', label)
                        if win_index is None:
                            if win_label == label:
                                advance_stage(index, label)
                            else:
                                lives -= 1  # Decrement lives
                                if lives == 0:  # Check if lives are zero
                                    screen.blit(redON,(669+x,283+y))
                                    screen.blit(strike,strike_pos[2])
                                    pygame.display.update()
                                    print('You lose! Better luck next time!')
                                    sleep(2)
                                    screen.fill((255,255,255))
                                    screen.blit(game_over,(196,0))
                                    pygame.display.update()
                                    sleep(3)
                                    run = False
                                else:
                                    print('AWW GET BETTER AT THE GAME IDIOT ^ ^')
                                    strike_no+=1
                                    print(f'Lives left: {lives}')
                        elif win_label is None:
                            if win_index == index:
                                advance_stage(index, label)
                            else:
                                lives -= 1  # Decrement lives
                                if lives == 0:  # Check if lives are zero
                                    screen.blit(redON,(669+x,283+y))
                                    screen.blit(strike,strike_pos[2])
                                    pygame.display.update()
                                    print('You lose! Better luck next time!')
                                    sleep(2)
                                    screen.fill((255,255,255))
                                    screen.blit(game_over,(196,0))
                                    pygame.display.update()
                                    sleep(3)
                                    run = False
                                else:
                                    print('AWW GET BETTER AT THE GAME IDIOT ^ ^')
                                    strike_no+=1
                                    print(f'Lives left: {lives}')
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                show_book = True
        if show_book:
            screen.blit(book_manual[pg_no],(710+x,y-150))

            screen.blit(left_arrow,(660+x,315+y))
            left_arrow_rect = left_arrow.get_rect()
            left_arrow_rect.topleft = (660+x,315+y)
            screen.blit(right_arrow,(1410+x,315+y))
            right_arrow_rect = left_arrow.get_rect()
            right_arrow_rect.topleft = (1410+x,315+y)

            while show_book:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        run = False
                        show_book = False
                    elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        cursor_pos = pygame.mouse.get_pos()
                        if left_arrow_rect.collidepoint(cursor_pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                            pg_no = (pg_no-1)%len(book_manual)
                        elif right_arrow_rect.collidepoint(cursor_pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                            pg_no = (pg_no+1)%len(book_manual)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        show_book = False
                        break
                    screen.blit(book_manual[pg_no],(710+x,y-150))
                    pygame.display.update()
        pygame.display.update()

# Function to convert time to a formatted string
def format_time(milliseconds):
    # Convert milliseconds to seconds
    seconds = milliseconds // 1000
    remaining_milliseconds = ( milliseconds % 1000 ) // 10

     # Calculate minutes and remaining seconds
    minutes = seconds // 60
    seconds %= 60

    # Format the time as MM:SS
    return f"{minutes:02d}:{seconds:02d}:{remaining_milliseconds:02d}"

def choose_game():
    global games, n1
    game = random.choice(games)
    if game == 'wires':
        win = wires()
        if (not win):
            return False
        else:
            return True
    elif game == 'symbols':
        win = symbols()
        if (not win):
            return False
        else: 
            return True
    elif game == 'ceasar':
        win = ceasar()
        if (not win):
            return False
        else:
            return True
    elif game == 'memory':
        win = memory()
        if (not win):
            return False
        else:
            return True
    games.remove(game)
    n1-=1
#mini_main()
pygame.quit()