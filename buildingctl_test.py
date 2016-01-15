#Test case for buildingctl.py

import buildingctl
import file_io

#define test variables

balance_sheet={}
player_list={}
building_list={}
building_add = []
UIDlist = []
money=10
pollution=0
trash=0
init = 0
asdf = 0
chosenplayer = 'asdf'

#load balance sheet

balance_sheet = file_io.load_balance('balance_sheet.csv')

#load savefilev for testing

player = file_io.load(chosenplayer)
print (player)
init = player[0]
building_list = player[1]
UIDlist = player[2]
money,pollution,trash = init
#print(init)
#print(building_list)
#print(UIDlist)d

#test buildingctl.addbuilding - Add building

player = buildingctl.addbuilding(player,balance_sheet,'power_plant', 1, 2)
print(player)

#UIDlist,building_list,money = building_add


#test buildingctl.removebuilding - Remove building

player = buildingctl.removebuilding(player, '3')
print(player)

#test buildingctl.upgradebuilding - Upgrade building

player = buildingctl.upgradebuilding(balance_sheet, player, '2')
print(player)
