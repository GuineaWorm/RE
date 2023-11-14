##Place Lobsters Trap and Pickup v2
##
##------------------------------
from Scripts.utilities.items import FindItem, MoveItem
from System.Collections.Generic import List
from System import Byte, Int32

lobster_trap = 0x44D0
globaldelay = 650 #delay for item use
pickupdelay = 100000 #1 to 5 minutes, add 1000 for every trap # 300000 = 5 min
dropbag = 0x4084B4A6
i = 0
trapsOnGround = []

def drop_traps():
    pos = 1
    pX = Player.Position.X - 6
    pY = Player.Position.Y + 6
    traps = Items.FindAllByID(lobster_trap, -1,Player.Backpack.Serial, True)
    Timer.Create("First Trap",pickupdelay,"Timer Complete")
    for trap in traps:
        if "empty" in trap.Name:
            Items.UseItem(trap)
            Target.WaitForTarget(1000)
            Target.TargetExecute(pX, pY, Player.Position.Z)
            Misc.Pause(globaldelay)
            pX = pX + 2
            if pX > Player.Position.X + 6:
                pX = Player.Position.X - 6
                pY = pY - 2
        filter = Items.Filter()
        filter.Enabled = True
        filter.RangeMax = 10
        filter.OnGround = 1
        filter.Graphics = List[Int32]([0x44CB])
        trapsInRange = Items.ApplyFilter(filter)
        for temp in trapsInRange:
            if temp.Serial not in trapsOnGround:
                trapsOnGround.append(temp.Serial)
                print(str(trapsOnGround))
                
        #Misc.Pause(300000) #5minutes
        #Misc.Pause(60000)
        
def get_traps():
    filter = Items.Filter()
    filter.Enabled = True
    filter.RangeMax = 10
    filter.OnGround = 1
    filter.Graphics = List[Int32]([0x44CB])
    trapsInRange = Items.ApplyFilter(filter)
    for item in trapsInRange:
        if "lobster trap" in item.Name:
            Items.UseItem(item.Serial)
            Misc.Pause(globaldelay)
            if Journal.Search("must wait to perform"):
                Journal.Clear()
                get_traps()
            if Player.Weight > 500:
                clear_traps()
    return
        
def clear_traps(): 
    Misc.Pause(globaldelay)         
    fulltrap = Items.FindAllByID(lobster_trap, -1,Player.Backpack.Serial, True)
    for tempvar in fulltrap:
        if "lobster trap" in tempvar.Name:
            if "empty" not in tempvar.Name:
                Items.UseItem(tempvar.Serial)
                Misc.Pause(globaldelay)
                if Journal.Search("must wait to perform"):
                    Journal.Clear()
                    clear_traps()
                if Player.Weight > 500:
                    check_weight()
    return

def check_weight():
    crabs = List[Int32]([0x44D1,0x44D2,0x44D3,0x44D4,0x44C6,0x44C4,0x4305,0x4307,0x4306,0x44C3])
    for x in range(len(crabs)):
        temp = Items.FindByID(crabs[x],-1,Player.Backpack.Serial,False,False)
        while temp != None:
            MoveItem(Items,Misc,temp,dropbag)
            temp = Items.FindByID(crabs[x],-1,Player.Backpack.Serial,False,False)
    return

clear_traps()    
check_weight()                 
drop_traps()
while Timer.Check("First Trap") == True:
    Misc.Pause(1000)
get_traps()
clear_traps() 
check_weight() 