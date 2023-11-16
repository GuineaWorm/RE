##Place Lobsters Trap and Pickup
##
##------------------------------
from Scripts.utilities.items import FindItem, MoveItem
from System.Collections.Generic import List
from System import Byte, Int32

lobster_trap = 0x44CF
globaldelay = 600 #delay for item useage
pickupdelay = 60100 #1 to 5 minutes, add 1000 for every trap # 300000 = 5 min
dropbag = 0x403810B3
i = 0


def drop_traps():
    pos = 1
    pX = Player.Position.X - 8
    pY = Player.Position.Y + 2
    traps = Items.FindAllByID(lobster_trap, -1,Player.Backpack.Serial, True)
    for trap in traps:
        if "empty" in trap.Name:
            Items.UseItem(trap)
            Target.WaitForTarget(1000)
            if pos == 1:
                pX = pX + 2
                if pX > (Player.Position.X + 6):
                    pX = Player.Position.X - 6
                    pY = pY + 2
                    if pY > (Player.Position.Y + 6):
                        pos = 2
                        pY = Player.Position.Y - 2
                        pX = Player.Position.X - 8
            if pos == 2:
                pX = pX + 2
                if pX > (Player.Position.X + 6):
                    pX = Player.Position.X - 6
                    pY = pY - 2
            Target.TargetExecute(pX, pY, Player.Position.Z)
            Misc.Pause(globaldelay)
        #Misc.Pause(300000) #5minutes
        #Misc.Pause(60000)
        
def get_traps():
    filter = Items.Filter()
    filter.Enabled = True
    filter.RangeMax = 10
    filter.OnGround = True
    trapsInRange = Items.ApplyFilter(filter)
    for item in trapsInRange:
        if "lobster trap" in item.Name:
            Items.UseItem(item.Serial)
            Misc.Pause(globaldelay)
            if Journal.Search("must wait to perform"):
                Journal.Clear()
                get_traps()
        
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

def check_weight():
    crabs = List[Int32]([0x44D1,0x44D2,0x44D3,0x44D4])
    if Player.Weight > 300:
        for x in range(4):
            temp = Items.FindByID(crabs[x],-1,Player.Backpack.Serial,False,False)
            while temp != None:
                MoveItem(Items,Misc,temp,dropbag)
                temp = Items.FindByID(crabs[x],-1,Player.Backpack.Serial,False,False)

check_weight()                 
drop_traps()
Misc.Pause(pickupdelay)
get_traps()
clear_traps() 
 