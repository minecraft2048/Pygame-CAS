def addbuilding(UIDlist,building_list,balance_sheet,current_money,building,x,y): #test
    """Adds bulding from the building list"""
    print(current_money)
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
    if current_money <= 0:
        raise ValueError('Not enough money')
    else:
        x = str(x)
        y = str(y)
        building_list[UID]=[building,'1',x,y]
        return [UIDlist,building_list,current_money]

def removebuilding(building_add,UID):
    """Removes building from the building list.

    Arguments:
    building_add: building_add list in main program
    UID: Building unique ID that want to be removed from UID list in main program

    """
    #print(UIDlist)
    #print(UID)
    building_add[0].remove(UID)
    building_add[1].pop(UID)
    return building_add

def upgradebuilding(balance_sheet,building_list,UID):
    current_building = building_list[1][UID][0]
    current_money = building_list[2]
    next_level = int(building_list[1][UID][1])+1
    print(next_level)
    next_level_index = next_level + 1
    cost = int(balance_sheet[current_building][next_level_index])
    current_money=current_money-cost
    if current_money <= 0:
        raise ValueError('Not enough money')
    else:
        building_list[1][UID][1]= str(next_level)
        building_list[2] = current_money
        return building_list
