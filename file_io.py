import csv
import os
import glob

filepath = os.path.join(os.getcwd(),'savefile')

def player_scan():
    player_list_raw = []
    player_list = []
    os.chdir(filepath)
    for files in glob.glob('*.csv'):
        player_list_raw.append(files)
    player_list2 = [i for i in player_list_raw if '_init_value.csv' in i]
    for i in player_list2:
        player_list.append(i.replace('_init_value.csv',''))
    return player_list


def load_balance(filename):
    balance_sheet={}
    reader_balance = csv.reader(open(filename))
    for row in reader_balance:
        key = row[0]
        if key in balance_sheet:
            # implement your duplicate row handling here
            pass
        balance_sheet[key] = row[1:]
    return balance_sheet

def load_init(filename,chosenplayer):
    player_list = {}
    reader_load = csv.reader(open(filename))
    for row in reader_load:
        key = row[0]
        if key in player_list:
            # implement your duplicate row handling here
            pass
        player_list[key] = row[1:]
    #print (player_list)
    money,pollution,trash = player_list[chosenplayer]
    money = float(money)
    pollution = float(pollution)
    trash = float(trash)
    return_list=[money,pollution,trash]
    return return_list

def load_building(filename):
    building_list={}
    UIDlist = []
    x = 0
    y = 0
    reader_load2 = csv.reader(open(filename))
    for row in reader_load2:
        key = row[0]
        if key in building_list:
            # implement your duplicate row handling here
            pass
        building_list[key] = row[1:]
        UIDlist.append(row[0])
    #print (building_list)
    UIDlist.remove('UID')
    #print (UIDlist)
    return building_list,UIDlist,x,y

def player_name2filename(player_name):
    name = []
    building = player_name + '_building.csv'
    init = player_name + '_init_value.csv'
    name =  os.path.join(filepath,building),os.path.join(filepath,init)
    return name

def init_save(filename,player_name,data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['player_name','current_money','current_pollution','current_trash']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'player_name':player_name,'current_money':data[0],'current_pollution':data[1],'current_trash':data[2]})
    return

def building_save(filename,data):
    data.pop('UID',None)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['UID','building','level','x','y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        print (data)
        for key in data:
            writer.writerow({'UID':key,'building':data[key][0],'level':data[key][1],'x':data[key][2],'y':data[key][3]})
    return

def load(player_name):
    init = {}
    filename = player_name2filename(player_name)
    building,UID,x,y = load_building(filename[0])
    return (load_init(filename[1],player_name),building,UID)

def save(player_name,init,building_list):
    filename = player_name2filename(player_name)
    init_save(filename[0],player_name,init)
    building_save(filename[1],building_list)
    return
