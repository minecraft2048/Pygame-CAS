import pygame
import time
import random

import csv
import time
import kernel
import file_io
import pygame
import threading

from pygame.locals import *


pygame.init()

display_width = 800 #Window size
display_height = 600
#define simulation variables

balance_sheet={}
player_list={}
building_list={}
UIDlist = []
money=0
pollution=0
trash=0
init = 0
asdf = 0
chosenplayer = 'asdf'

black = (0,0,0) #Color definition, maps color name to RGB tuple
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #initialize screen
pygame.display.set_caption('Hello game') #Program name
clock = pygame.time.Clock()

def clamp(n, minn, maxn):
    '''Keep values in between values
        Arguments:
        n: Value
        minn: Minimum value
        maxn: Maximum value
    '''
    return max(min(maxn, n), minn)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

def text_write(msg,x,y):
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.Font("freesansbold.ttf", 15)
    # render text
    label = myfont.render("Some text!", 1, (0,0,0))
    gameDisplay.blit(label, (x, y))

def button(msg,x,y,w,h,ic,ac,action=None):
        ''' Makes button in the screen and draw it
            Arguments:
            msg: Text for the button
            x: X coordinate in pixels
            y: Y coordinate in pixels
            w: Button width in pixels
            h: Button height in pixels
            ic: The button inital color
            ac: Button color on hover
            font: Text font
            action: Function name without ()
        '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
        else:
                pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

def bar(x,y,w,h,color_init,color_border,color_bg=white,border_thickness=1,percent=100,msg=None):
    ''' Creates bar like loading bar
        Arguments:
        x : X coordinate
        y : Y coordinate
        w : Bar length
        h : Bar height
        color_init: The initial color of the bar
        color_border: The color of the border
        color_bg: Background color of the bar when it is empty
        border_thickness: Border thickness in pixels
        percent: How many percent does the bar fill inside the border
        msg: The text inside the bar
    '''
    w_inner = w * clamp((percent/100),0,1)
    pygame.draw.rect(gameDisplay,color_border,(x-border_thickness,y-border_thickness,w+(border_thickness*2),h+(border_thickness*2)))
    pygame.draw.rect(gameDisplay,color_bg,(x,y,w,h))
    pygame.draw.rect(gameDisplay,color_init,(x,y,w_inner,h))
    smallText = pygame.font.Font('freesansbold.ttf',15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    return

def value_bar(x,y,w,h,value,max_value,color_init,color_border,color_bg,border_thickness=1):
    ''' Creates status bar
        Arguments:
        x : X coordinate
        y : Y coordinate
        w : Bar length
        h : Bar height
        value: Current value
        max_value: Maximum value
        color_init: The initial color of the bar
        color_border: The color of the border
        color_bg: Background color of the bar when it is empty
        border_thickness: Border thickness in pixels
    '''
    msg = str(value) + '/' + str(max_value)
    percent = value/max_value*100
    bar(x, y, w, h, color_init, color_border, color_bg, border_thickness, percent, msg)

#load balance sheet

balance_sheet = file_io.load_balance('balance_sheet.csv')
player = file_io.load(chosenplayer)
print (player)
init = player[0]
building_list = player[1]
UIDlist = player[2]
money,pollution,trash = init
#print(init)
print(building_list)
print(UIDlist)


def main_loop():
    balance_sheet={}
    player_list={}
    building_list={}
    UIDlist = []
    money=0
    pollution=0
    trash=0
    init = 0
    asdf = 0
    chosenplayer = 'asdf'

    balance_sheet = file_io.load_balance('balance_sheet.csv')
    player = file_io.load(chosenplayer)
    print (player)
    init = player[0]
    building_list = player[1]
    UIDlist = player[2]
    money,pollution,trash = init
    #print(init)
    print(building_list)
    print(UIDlist)
    frame = 0
    crashed = False
    gameDisplay.fill(white)
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            #print(event)

        value_bar(150,200,100,20,money,800,green,black,white,border_thickness=1)
        frame = frame + 1
        if frame == 60: #Clock divider because threading is hard
            money,pollution,trash = kernel.simulate(UIDlist,building_list,balance_sheet,money,pollution,trash)
            #print('Money is: '+str(money))
            #print('Pollution is: '+ str(pollution)).
            #print('Trash is: '+ str(trash))
            frame = 0
        #print(secondframe)
#        bar(150, 200, 100, 20, green,black,white,3, frame,'100/100')
        print(frame)
        text_write('Hello World!',200,200)
        button("Quit",550,450,100,50,red,bright_red,print('test'))
        pygame.display.update()
        clock.tick(60)

main_loop()
pygame.quit()
quit()
