from System.Collections.Generic import List
from System import Int32 
from Scripts.utilities.items import FindItem, MoveItem
beetle = 0x0003DA97
keep = List[Int32]([0x1081,0x09F1,0x09B9,0x0DF8,0x1BD1,0x1609,0x4077])
trash = List[Int32]([])

ignore = []

from Scripts.glossary.colors import colors

def lootRopes():

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
                    knife = Items.FindByID(0x2D20,-1,Player.Backpack.Serial) #skinning knife
                    Misc.Pause(100)
                    if knife is not None:
#                        Misc.SendMessage( 'Found knife, attempting to cut corpse', colors[ 'red' ] )
                        Items.UseItem(knife)
                        Target.WaitForTarget(5000)
                        Target.TargetExecute(corpse)
                        Misc.Pause(1000)
                        if Player.Weight > 449:
                            if Player.Mount:
                                #go through keep and put on beetle
                                Mobiles.UseMobile(Player.Serial)
                                Misc.Pause(600)  
                                for x in range(len(keep)):
                                    temp = Items.FindByID(keep[x],-1,Player.Backpack.Serial,False,False)
                                    while temp != None:
                                        MoveItem(Items,Misc,temp,beetle)
                                        temp = Items.FindByID(keep[x],-1,Player.Backpack.Serial,False,False) 
                                Misc.Pause(600)
                                Mobiles.UseMobile(beetle)
                                Misc.Pause(600)
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

while True:
    lootRopes()
    Misc.Pause(2000)