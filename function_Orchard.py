from System.Collections.Generic import List
from System import Byte, Int32

##############################################
#               ---Orchard---                #
#                     By                     #
#              ---Guinea Worm---             #
#             v4 11/15/2023 @ 2345           #
##############################################

def colorize():
    items = []
    ignore = []
    theFilter = Items.Filter()
    theFilter.RangeMax = 25
    theFilter.OnGround = True
    theFilter.Enabled = True
    theFilter.Movable = False
    trees = List[Int32]([0xD01])
    theFilter.Graphics = trees
    itemsInRange = Items.ApplyFilter(theFilter)
    Misc.Pause(100)
        
    for x in itemsInRange:
        if x.Serial not in items and "cypress tree" in x.Name and x.Serial not in ignore:
            items.Add(x.Serial)
            ignore.Add(x.Serial)

    items = sorted(items, key=lambda itm: itm)
    bool = False
    hue = 0
    num = 0
    while bool == False:
        for x in range(len(items)):
            Items.SetColor(items[x],hue)
            num = num + 1
            if num == 2:
                num = 0
                hue = (x+6) * 6
        bool = True
    return

def autothrow():
    ignore = []
    picked = False
    complete = False
    Journal.Clear()
    while complete == False:
        theFilter = Items.Filter()
        theFilter.RangeMax = 10
        theFilter.OnGround = True
        theFilter.Enabled = True
        theFilter.Movable = False
        trees = List[Int32]([0xD01])
        theFilter.Graphics = trees
        treeInRange = Items.ApplyFilter(theFilter)
        Misc.Pause(100)

        for tree in range(len(treeInRange)):
            if picked == False and Player.DistanceTo(treeInRange[tree]) < 4 and treeInRange[tree].Serial not in ignore:
                treeColor = treeInRange[tree].Hue
                Items.UseItem(treeInRange[tree])
                Misc.Pause(100)
                if Items.BackpackCount(0x09D0,-1) > 0:
                    ignore.Add(treeInRange[tree].Serial)
                    Player.HeadMessage(55,"Pick")
                    Items.SetColor(Items.FindByID(0x09D0,-1,Player.Backpack.Serial,False,False).Serial,treeColor)
                    picked = True
            if picked == True and Player.DistanceTo(treeInRange[tree]) < 10 and treeInRange[tree].Hue == treeColor and treeInRange[tree].Serial not in ignore:
                Player.HeadMessage(55,"Throw")
                Items.UseItem(Items.FindByID(0x09D0,-1,Player.Backpack.Serial,False,False))
                Misc.Pause(100)
                Target.TargetExecute(treeInRange[tree].Serial)
                Misc.Pause(100)
                if Items.BackpackCount(0x09D0,-1) > 0:
                    ignore.Add(treeInRange[tree])
                    Misc.Pause(1100)
                    picked = False
        if Journal.SearchByType("You have bested this tower",'System'):
            Player.HeadMessage(55,"Huzzah!")
            complete = True

def Main():
    colorize()
    autothrow()
Main()

#lambda test.....
#items = [3, 4, 1, 7]
#Player.HeadMessage(52, str(items))
#lambda test.....