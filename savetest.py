#import necessary stuff like pygame

import csv
import time
import file_io

#define variables

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

chosenplayer = 'asdf'
saveplayer = 'qwer'

#load balance sheet

balance_sheet = file_io.load_balance('balance_sheet.csv')
#print(balance_sheet)

#load savefile

asdf = file_io.load(chosenplayer)
init = asdf[0]
building_list = asdf[1]
UIDlist = asdf[2]
money,pollution,trash = init
print(init)
print(asdf)


#print(building_list)
#print(UIDlist)

#save to savefile

file_io.save(saveplayer,[money,pollution,trash],building_list)
