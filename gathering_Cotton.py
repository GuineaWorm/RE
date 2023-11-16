from System.Collections.Generic import List
from System import Int32 as int
ignore = []
harvestables = [0x1A9B, 0x1A9A, 0x0C4F, 0x0C50, 0x0C51, 0x0C52, 0x0C53, 0x0C54, 0x0CC6, 0x1A99]
resources = [0x0DF9, 0x1A9C, 0x1A9D]
pause = 350
blade = 0x40285F93

while True:
    itemFilter = Items.Filter()
    itemFilter.Enabled = True
    itemFilter.IsCorpse = False # optional
    itemFilter.OnGround = True # Questionably optional
    itemFilter.Movable = False # Questionably optional
    itemFilter.RangeMin = 0 # optional
    itemFilter.RangeMax = 2 # optoinal
    itemFilter.Graphics = List[int](harvestables) # optional, use item IDs
    itemFilter.CheckIgnoreObject = False # optioinal, if you use Misc.IgnoreObject(item) the fitler will ignore if true.
    itemFilter.Hues = List[int]([0x0000])
    itemsFilterList = Items.ApplyFilter(itemFilter) # returns list of items, manipulate list after this as you wish

    for item in itemsFilterList:
        Items.UseItem(item)
        Misc.Pause(pause)
        
    Misc.Pause(50)# Run the check 2x per second.
    
    ## Next we sheer sheep if they are nearbye using our dagger.
    mobileFilter = Mobiles.Filter()
    mobileFilter.Enabled = True
    mobileFilter.RangeMin = 0
    mobileFilter.RangeMax = 2
    mobileFilter.CheckLineOfSite = False
    #mobileFilter.Graphics  = List[int]([0x00CF,0x00DF])
    #mobileFilter.Name = 'A Sheep'
    mobileFilter.IsGhost = False  

    foundMobiles = Mobiles.ApplyFilter(mobileFilter)
    
    for mobile in foundMobiles:
        if mobile.Name == "a sheep" and mobile.Serial not in ignore:
            Player.HeadMessage(33,"123")
            Items.UseItem(blade) #Dagger
            Misc.Pause(200)
            Target.TargetExecute(mobile)  
            ignore.append(mobile.Serial)
        
        
        
    ## PICKUP BALES ##
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
        
    Misc.Pause(0) # Run the check 2x per second.
        