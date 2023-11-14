from System.Collections.Generic import List
from System import Int32 
from System import Byte 
from Scripts.utilities.items import FindItem, MoveItem

Timer.Create("heal", 1, "Heal Timer Initialized.")

beetlebag = 0x401F2B7D
beetle = 0x0003DA97
keep = List[Int32]([0x1081,0x09F1,0x09B9,0x0DF8,0x1BD1,0x1609,0x4077])
trash = List[Int32]([])
primary = True
eoo = True
knife = Items.FindByID(0x2D20,-1,Player.Backpack.Serial) #harvester's blade

ignore = []

from Scripts.glossary.colors import colors

def skin():

    filter = Items.Filter()
    filter.RangeMax = 2
    filter.Enabled = True
    filter.IsCorpse = True
    filter.OnGround = True
    filter.Movable = False

    corpses = Items.ApplyFilter(filter)
    if corpses:
        for corpse in corpses:
            if Player.InRangeItem(corpse,2):
                if not corpse.Serial in ignore:
#                    Misc.SendMessage( 'in corpse list', colors[ 'red' ] )
                    #timer(100)
                    #Misc.Pause(100)
                    if knife is not None:
#                        Misc.SendMessage( 'Found knife, attempting to cut corpse', colors[ 'red' ] )
                        Items.UseItem(knife)
                        Target.WaitForTarget(5000)
                        Target.TargetExecute(corpse)
                        timer(500)
                        Items.Message(corpse, 255, "**SKINNED**") 
                        #Misc.Pause(1000)
                        if Player.Weight > 449:
                            if Player.Mount:
                                #go through keep and put on beetle
                                Mobiles.UseMobile(Player.Serial)
                                Misc.Pause(600)  
                                for x in range(len(keep)):
                                    temp = Items.FindByID(keep[x],-1,Player.Backpack.Serial,False,False)
                                    while temp != None:
                                        MoveItem(Items,Misc,temp,beetlebag)
                                        temp = Items.FindByID(keep[x],-1,Player.Backpack.Serial,False,False) 
                                timer(600)
                                #Misc.Pause(600)
                                Mobiles.UseMobile(beetle)
                                timer(600)
                                #Misc.Pause(600)
                            #go through trash and place on last corpse
                            if Player.DistanceTo(corpse) < 2:
                                for x in range(len(trash)):
                                    temp = Items.FindByID(trash[x],-1,Player.Backpack.Serial,False,False)
                                    while temp != None:
                                        MoveItem(Items,Misc,temp,corpse)
                                        temp = Items.FindByID(trash[x],-1,Player.Backpack.Serial,False,False)
                            #if Player.DistanceTo(corpse) > 1:
                            #    for x in range(len(trash)):
                            #        temp = Items.FindByID(trash[x],-1,Player.Backpack.Serial,False,False)
                            #        while temp != None:
                            #            Items.MoveOnGround(temp, 0, Player.Position.X - 1, Player.Position.Y - 1)
                            #            temp = Items.FindByID(trash[x],-1,Player.Backpack.Serial,False,False)
                    ignore.append(corpse.Serial) 

def attack(range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5])) # Noto by color ie: Blue 1, green 2, greynuetral 3, greycriminal 4, orange 5, red 6, yellow 7 # required import at top of script "from System import Byte"
    enemies = Mobiles.ApplyFilter(fil)
    for enemy in enemies:
        Player.Attack(enemy.Serial)
    if range == 1:
            Misc.Pause(100)
    return

def heal():
    bandage = Items.FindByID(0x0E21,-1,Player.Backpack.Serial,False,False)
    if Player.Hits < Player.HitsMax and Timer.Check("heal") == False:
        Items.UseItem(bandage)
        Target.WaitForTarget(500,True)
        Target.Self()
        Timer.Create("heal", 2500, "Heal Timer Deactivated.")
    return
    
def timer(delay):
    Timer.Create("delay", delay, "Timer Deactivated.")
    while Timer.Check("delay") != False:
        attack(15)
        attack(1)
        heal()
    return
    
while True:
    skin()
    attack(15)
    attack(1)
    heal()
    #Misc.Pause(2000)