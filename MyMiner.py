fire_beetle = 0x00017C25
blue_beetle = 0x0000C5A2
tool_kits_to_keep = 2
shovels_to_keep = 20
#ores = {
#
#    'agapite ore': myItem( 'agapite ore', 0x19B9, 0x097E, 'ore', None ),
#    'bronze ore': myItem( 'bronze ore', 0x19B9, 0x06D8, 'ore', None ),
#    'copper ore': myItem( 'copper ore', 0x19B9, 0x045F, 'ore', None ),
#    'dull copper ore': myItem( 'dull copper ore', 0x19B9, 0x0415, 'ore', None ),
#    'golden ore': myItem( 'golden ore', 0x19B9, 0x06B7, 'ore', None ),
#    'iron ore': myItem( 'iron ore', 0x19B9, 0x0000, 'ore', None ),
#    'shadow iron ore': myItem( 'shadow iron ore', 0x19B9, 0x0455, 'ore', None ),
#    'verite ore': myItem( 'verite ore', 0x19B9, 0x07D2, 'ore', None ),
#    'valorite ore': myItem( 'valorite ore', 0x19B9, 0x0544, 'ore', None )
#}

#variables
ORE_TYPES = [0x19B7, 0x19B8, 0x19B9, 0x19BA]
CRAP = [0x0F16, 0x3193, 0x0F13, 0x3198, 0x3197, 0x0F10, 0x3192, 0x3194, 0x0F25, 0x0F28, 0x3195, 0x0F18, 0x0F26, 0x0F0F, 0x0F15, 0x0F11]          
TINKERING_GUMP = 0x38920ABD
TOOL_KIT = 0x1EB8
SHOVEL = 0x0F39
#RockStaticID = [6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012]
#miningTiles = [220,221,223,224,225,226,227,228,229,230,231,240,241,242,243,468,561,562,563,564,565,566,567,568,569,570,571,572,573,573,575,576,577,578,578,558,556,559,557,228,223,227,118]
#miningFloors = [0x022F,1339,1340,1342,1343,1344,1345,1346,1347,1348,1349,1350,1351,1352,1352,1354,1355,1356,1357,1358,1359]
ore_filter = Items.Filter()
ore_filter.Graphics.AddRange(ORE_TYPES)
crap_filter = Items.Filter()
crap_filter.Graphics.AddRange(CRAP)

sturdy = True
from AutoComplete import *

def move_ingots():
    ingots = Items.FindAllByID(0x1BF2, -1, Player.Backpack.Serial, True)
    beetle_backpack = Mobiles.FindBySerial(blue_beetle).Backpack.Serial
    for i in ingots:
        # keep at least 50 iron ingots in pack to make tools
        Items.Move(i, beetle_backpack,
                   max(0, i.Amount - 50) if i.Hue == 0 else -1)
        Misc.Pause(600)
        
def move_crap():  
    craps = Items.FindAllByID(CRAP, -1, Player.Backpack.Serial, True)
    beetle_backpack = Mobiles.FindBySerial(blue_beetle).Backpack.Serial    
    for i in craps:
        Items.Move(i, beetle_backpack, 0)
        Misc.Pause(600)
        
def smelt_ore():
    ores = Items.ApplyFilter(ore_filter)
    Player.HeadMessage(2128, 'Smelting...')
    for ore in ores:
        if ore.ItemID == 0x19B7 and ore.Amount == 1:
            continue
        Items.UseItem(ore)
        Target.WaitForTarget(1000)
        Target.TargetExecute(fire_beetle)
        Misc.Pause(200)

def get_shovels():
    return Items.FindAllByID(SHOVEL, -1 if sturdy else 0,Player.Backpack.Serial, True)
    
def get_tool_kits():
    return Items.FindAllByID(TOOL_KIT, 0, Player.Backpack.Serial, True)
    
def gump_check():
    if Gumps.CurrentGump() != TINKERING_GUMP:  # tinkering menu
        Items.UseItem(get_tool_kits()[0])
        Gumps.WaitForGump(TINKERING_GUMP, 2000)

    if not Gumps.LastGumpTextExistByLine(24, "scissors"):
        Gumps.SendAction(TINKERING_GUMP, 15)  # tools tab
        Gumps.WaitForGump(TINKERING_GUMP, 2000)
    
def make_tool_kit():
    gump_check()
    Gumps.SendAction(TINKERING_GUMP, 23)  # tool kit
    Gumps.WaitForGump(TINKERING_GUMP, 2000)
    return True    
        
def make_shovel():
    gump_check()
    Gumps.SendAction(TINKERING_GUMP, 72)  # shovel
    Gumps.WaitForGump(TINKERING_GUMP, 2000)
    return True
   
def make_tools():
    kits = len(get_tool_kits())
    shovels = len(get_shovels())

    while kits < tool_kits_to_keep:
        if make_tool_kit():
            kits += 1
        Misc.Pause(200)

    while shovels < shovels_to_keep:
        if make_shovel():
            shovels += 1
        Misc.Pause(200)

    Gumps.CloseGump(TINKERING_GUMP) 
        
while True:
    try:
        tool = get_shovels()[0]
    except IndexError:
        Player.HeadMessage(2125, 'Out of tools, making more!!')
        make_tools()
        tool = get_shovels()[0]
            

    #tool = get_shovels()[0]
    #Target.TargetResource(tool, 'ore')
    #Misc.Pause(10)
    
    shovels = get_shovels(); #Use your current function you made.
    for shovel in shovels: # loops through each shovel
        smelt_ore()
        if Player.Weight >= 250:
            ingots1 = Items.FindByID(0x1BF2, -1, Player.Backpack.Serial, True)
            beetle_backpack = Mobiles.FindBySerial(blue_beetle).Backpack.Serial
            if ( ingots1 is not None):
                Items.Move(ingots1, beetle_backpack,0)
            move_crap()
        #Misc.Pause(600)
        Items.UseItem(shovel) # Use the shovel
        Target.WaitForTarget(1000) #I add in delays like this because sometimes there is a bit of lag
        #Add code where you target whatever you're trying to mine here.
        tileinfo = Statics.GetStaticsTileInfo(Player.Position.X, Player.Position.Y, Player.Map)
        Target.TargetExecute(Player.Position.X, Player.Position.Y, Player.Position.Z, tileinfo[0].StaticID)
        if Journal.Search('There is no metal here to mine.'):
        #    x, y = Player.Position.X, Player.Position.Y
            Player.HeadMessage(33, "No ore here!")
            Journal.Clear('There is no metal here to mine.')
        #    while Player.Position.X == x and Player.Position.Y == y:
        #        Misc.Pause(50)
        #if Journal.Search('Someone has gotten to the metal before you.'):
        #    x, y = Player.Position.X, Player.Position.Y
        #    Player.HeadMessage(33, "Someone got the ore!!")
        #    Journal.Clear('Someone has gotten to the metal before you.')
        #    while Player.Position.X == x and Player.Position.Y == y:
        #        Misc.Pause(50)
        #if Journal.Search('Your backpack is full, so the ore you mined is lost.'):
        #    x, y = Player.Position.X, Player.Position.Y
        #    Player.HeadMessage(33, "FULL!")
        #    Journal.Clear('Your backpack is full, so the ore you mined is lost.')
        #    smelt_ore()
        if Player.Weight >= 500:
            Misc.Pause(1000)
            Player.HeadMessage(77, 'SMELTING ORE...')
            smelt_ore()
            if Player.Weight >= 250:
                Player.HeadMessage(33, 'Moving ingots to beetle...')
                move_ingots()