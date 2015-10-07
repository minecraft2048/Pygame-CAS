import csv
import time

#variables


level2statmap={'1':[14,18,22],'2':[15,19,23],'3':[16,20,24],'4':[17,21,25]}
UIDlist = []



#main compute function  TODO: When done, only this should be in the kernel

def simulate_core(UID,building_list,balance_sheet,init_money,init_pollution,init_waste):
    building,buildinglvl=building_list[UID]
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
    return(money,pollution,trash)
