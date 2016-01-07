def addbuilding(UIDlist,building_list,current_money,building,x,y): #test
    UIDlist.sort()
    UID = UIDlist[-1] + 1
    UID = str(UID)
    UIDlist.append(UID)
    building_list[UID]=[building,1,x,y]
    return UIDlist,building_list,current_money

def removebuilding(UIDlist,building_list,UID):
    UIDlist.remove(UID)
    building_list.pop(UID)
    return UIDlist,building_list

#def upgradebuilding(balance_sheet,current_money,building_list,UID):
#    levelmap = {1:}
#    next_level = int(building_list[UID][1])+1
#    return
