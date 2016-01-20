def addbuilding(player,balance_sheet,building,x,y): #test
    """Adds bulding from the building list"""
    player[2].sort()
    #print(UIDlist)
    UID = player[2][-1]
    UID = int(UID)
    UID = UID + 1
    UID = str(UID)
    player[2].append(UID)
    cost = balance_sheet[building]
    cost = cost[2]
    cost = float(cost)
    current_money = int(player[0][0]) - cost
    if current_money <= 0:
        raise ValueError('Not enough money')
    else:
        x = str(x)
        y = str(y)
        player[0][0]=current_money
        player[1][UID]=[building,'1',x,y]
        return player


def removebuilding(player,UID):
    """Removes building from the building list.

    Arguments:
    building_add: building_add list in main program
    UID: Building unique ID that want to be removed from UID list in main program

    """
    #print(UIDlist)
    #print(UID)
    player[2].remove(UID)
    player[1].pop(UID)
    return player

def upgradebuilding(balance_sheet,player,UID):
    current_building = player[1][UID][0]
    current_money = player[0][0]
    next_level = int(player[1][UID][1])+1
    print(next_level)
    next_level_index = next_level + 1
    cost = int(balance_sheet[current_building][next_level_index])
    current_money=current_money-cost
    if current_money <= 0:
        raise ValueError('Not enough money')
    else:
        player[1][UID][1]= str(next_level)
        player[0][0] = current_money
        return player

def movebuilding(player,UID,x,y):
    x = str(x)
    y = str(y)
    player[1][UID][2] = x
    player[1][UID][3] = y
    return player
