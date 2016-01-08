def addbuilding(UIDlist,building_list,balance_sheet,current_money,building,x,y): #test
    UIDlist.sort()
    #print(UIDlist)
    UID = UIDlist[-1]
    UID = int(UID)
    UID = UID + 1
    UID = str(UID)
    UIDlist.append(UID)
    cost = balance_sheet[building]
    cost = cost[2]
    cost = float(cost)
    current_money = current_money - cost
    x = str(x)
    y = str(y)
    building_list[UID]=[building,'1',x,y]
    return [UIDlist,building_list,current_money]

def removebuilding(building_add,UID):
    """Removes building from the building list"""
    #print(UIDlist)
    #print(UID)
    building_add[0].remove(UID)
    building_add[1].pop(UID)
    return [building_add[0],building_add[1]]

def upgradebuilding(balance_sheet,current_money,building_list,UID):
    next_level = int(building_list[UID][1])+1
    print(next_level)
#    return
