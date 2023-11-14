from Scripts.utilities.items import FindItem, MoveItem
fireBeetle = 0x001681BB
bluebeetle = 0x0018DF40
Journal.Clear()
prospecting = False

def smelt():
    oreFilter = Items.Filter()
    oreFilter.Graphics.AddRange([0x19B9,0x19BA,0x19B8,0x19B7])
    ores = Items.ApplyFilter(oreFilter)
    for ore in ores:
        Player.HeadMessage(2128, 'Smelting...')
        if ore.ItemID == 0x19B7 and ore.Amount == 1:
            continue
        Items.UseItem(ore)
        Target.WaitForTarget(1000)
        Target.TargetExecute(fireBeetle)
        Misc.Pause(500)

def dig(): 
    Journal.Clear()
    while not Journal.Search("There is no metal here to mine."):
        while not Journal.Search("mine there"):
            while not Journal.Search("Someone has gotten to the metal before you."):
            #pickaxe 0x0E86 
                shovels = Items.FindAllByID(0x0F39,-1,Player.Backpack.Serial, True)
                for shovel in shovels: 
                    Player.HeadMessage(2128, 'Digging...')
                    Target.TargetResource(shovel,"ore") 
                    Misc.Pause(100)
                    if Player.Weight > 400:
                        smelt()
                        unload()
                    if Journal.Search("There is no metal here to mine.") or Journal.Search("mine there") or Journal.Search("Someone has gotten to the metal before you."):
                        Journal.Clear()
                        prospect()
    Journal.Clear()                    
    prospect()
            
        
def unload():
    unloadingots = [0x1BF2]
    unloadgems = [0x3197,0x0F13,0x0F16,0x0F18,0x0F25,0x0F10,0x0F15,0x0F11,0x0F0F,0x3195,0x3194,0x0F26,0x3198,0x3192,0x3193,0x0F28]
    for unloadable in Player.Backpack.Contains:
        if unloadable.ItemID in unloadingots and unloadable.Amount > 49:
            MoveItem(Items,Misc,unloadable,bluebeetle)
        if unloadable.ItemID in unloadgems and unloadable.Amount > 74:
            MoveItem(Items,Misc,unloadable,bluebeetle)

def prospect():
    Target.Cancel()
    Journal.Clear()
    prospector = Items.FindByID(0x0FB4,-1,Player.Backpack.Serial,False,False)
    Items.UseItem(prospector)
    Target.PromptTarget("Prospect Ground",255)
    if Player.Weight > 500:    
        smelt()
        unload()
    dig()

        

while True: 
    prospect()