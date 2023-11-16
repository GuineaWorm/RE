from System.Collections.Generic import List
from Scripts.utilities.items import FindItem, MoveItem
beetle = 0x0003DA97

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
                    Items.UseItem(corpse)
                    Misc.Pause(500)

#                    Misc.SendMessage( 'in corpse list', colors[ 'red' ] )
                    knife = Items.FindByID(0x0F52,-1,Player.Backpack.Serial) #skinning knife
                    Misc.Pause(100)
                    if knife is not None:
#                        Misc.SendMessage( 'Found knife, attempting to cut corpse', colors[ 'red' ] )
                        Items.UseItem(knife)
                        Target.WaitForTarget(5000)
                        Target.TargetExecute(corpse)
                        Misc.Pause(1000)
                        temp = Items.FindByID(0x1079,-1,corpse.Serial)
                        if temp is not None:
                            if Player.Weight < 450:
                                MoveItem(Items,Misc,temp,Player.Backpack.Serial)
                                Misc.Pause(500)
                                scissors = Items.FindByID(0x0F9F,-1,Player.Backpack.Serial)
                                leather = Items.FindByID(0x1079,-1,Player.Backpack.Serial)
                                if leather is not None:
                                    Items.UseItem(scissors)
                                    Target.WaitForTarget(5000)
                                    Target.TargetExecute(leather)
                                    Misc.Pause(500)
                            elif Player.Weight > 449:
                                if Player.Mount:
                                    cutleather = Items.FindByID(0x1081,-1,Player.Backpack.Serial)
                                    if cutleather is not None:
                                        Mobiles.UseMobile(Player.Serial)
                                        Misc.Pause(600)
                                        MoveItem(Items,Misc,cutleather,beetle)
                                        Misc.Pause(600)
                                        Mobiles.UseMobile(beetle)
                                        Misc.Pause(600)
                                        temp = Items.FindByID(0x1079,-1,corpse.Serial)
                                        if temp is not None:
                                            MoveItem(Items,Misc,temp,Player.Backpack.Serial)
                    ignore.append(corpse.Serial) 

while True:
    lootRopes()
    Misc.Pause(2000)