from System.Collections.Generic import List
from System import Int32 as int

resources = [0x0DF9]
pause = 350
while True:
    #pickup cotton bale
    itemFilter = Items.Filter()
    itemFilter.Enabled = True
    itemFilter.IsCorpse = False # optional
    itemFilter.OnGround = True # Questionably optional
    itemFilter.Movable = True # Questionably optional
    itemFilter.RangeMin = 0 # optional
    itemFilter.RangeMax = 2 # optoinal
    itemFilter.Graphics = List[int](resources) # optional, use item IDs
    itemFilter.CheckIgnoreObject = False # optioinal, if you use Misc.IgnoreObject(item) the fitler will ignore if true.
    itemFilter.Hues = List[int]([0x0000])
    itemsFilterList = Items.ApplyFilter(itemFilter) # returns list of items, manipulate list after this as you wish

    for item in itemsFilterList:
        Items.Move(item, Player.Backpack.Serial, 9)
        Misc.Pause(pause)
        
    Misc.Pause(500) # Run the check 2x per second.    