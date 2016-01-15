import csv
import time
import numpy
import math
#variables


level2statmap={'1':[15,19,23],'2':[16,20,24],'3':[17,21,25],'4':[18,22,26]}
UIDlist = []



#main compute function  TODO: When done, only this should be in the kernel

def simulate_core(UID,building_list,balance_sheet,init_money,init_pollution,init_waste):
    #print(UID)
    #print(building_list)
    building,buildinglvl,x,y=building_list[UID]
    #print(building)
    #print(buildinglvl)
    buildlist=balance_sheet[building]
    #print(buildlist)
    money_index,pollution_index,waste_index=level2statmap[buildinglvl]
    money = buildlist[money_index]
    pollution = buildlist[pollution_index]
    waste = buildlist[waste_index]
    #print(float(money))
    #print(float(pollution))
    #print(float(waste))
    money=init_money+ float(money)
    pollution=init_pollution+ float(pollution)
    waste=init_waste+ float(waste)
    return(money,pollution,waste)

def simulate(UIDlist,building_list,balance_sheet,money,pollution,trash):
    for UID in UIDlist:
        money,pollution,trash = simulate_core(UID,building_list,balance_sheet,money, pollution, trash)
        #print('Money-in is: '+str(money))
        #print('Pollution-in is: '+ str(pollution))
        #print('Trash-in is: '+ str(trash))
    money= round(max(0,money),2)    #keeps the value >= 0 and 2 decimal points 
    pollution= round(max(0,pollution),2)
    trash= round(max(0,trash),2)
    return(money,pollution,trash)
