#import necessary stuff like pygame

import csv
import time
import kernel
import file_io
import pygame

from pygame.locals import *

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

#test variables

#define pygame variable

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
STATE = None #MAINMENU, LOAD

chosenplayer = 'asdf'

#load balance sheet

balance_sheet = file_io.load_balance('balance_sheet.csv')
#print(balance_sheet)

#load savefile

player = file_io.load(chosenplayer)
print (player)
init = player[0]
building_list = player[1]
UIDlist = player[2]
money,pollution,trash = init
#print(init)
print(building_list)
print(UIDlist)

#main loop

#while True:
#    money,pollution,trash = kernel.simulate(UIDlist,building_list,balance_sheet,money,pollution,trash)
#    print('Money is: '+str(money))
#    print('Pollution is: '+ str(pollution))
#    print('Trash is: '+ str(trash))
#    if money <= 0 or pollution >= 100 or trash >= 100:
#        print("Game over")
#        break
#    time.sleep(0.1)
