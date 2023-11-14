#Smithing by Worm
from Scripts.utilities.items import FindItem, MoveItem
filter = Items.Filter()
filter.Enabled = True
filter.OnGround = False    
itemfilter = Items.ApplyFilter(filter)
for item in Player.Backpack.Contains:
    if item.Name == "Salvage Bag":
        dropbag = item.Serial

def smith():
    if Gumps.LastGumpTextExist('BLACKSMITHING MENU') == False:
        Items.UseItem(Items.FindByID(0x0FBB,-1,Player.Backpack.Serial,False,False))
        Gumps.WaitForGump(949095101, 10000)
    smithy = Player.GetRealSkillValue('Blacksmithy')
    if smithy == Player.GetSkillCap('Blacksmithy'):
        Stop
    elif smithy >= 40 and smithy <= 45.0: #mace
        if Gumps.LastGumpTextExist('hammer pick') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 43)  
        Gumps.GetGumpData(Gumps.CurrentGump())
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 9)
    elif smithy >= 45 and smithy <= 50.0: #maul
        if Gumps.LastGumpTextExist('hammer pick') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 43)  
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 16)
    elif smithy >= 50 and smithy <= 55.0: #cutlass
        if Gumps.LastGumpTextExist('bone harvester') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 22)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 23)
    elif smithy >= 55 and smithy <= 59.5: #katana
        if Gumps.LastGumpTextExist('bone harvester') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 22)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 21)
    elif smithy >= 59.5 and smithy <= 70.5: #scimitar
        if Gumps.LastGumpTextExist('bone harvester') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 22)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 58)
    elif smithy >= 70.5 and smithy <= 106.4: #gorget
        if Gumps.LastGumpTextExist('ringmail') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 1)    
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 65)
    elif smithy >= 106.4 and smithy <= 108.9: #gloves
        if Gumps.LastGumpTextExist('ringmail') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 1)  
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 58)
    elif smithy >= 108.9 and smithy <= 116.3: #arms
        if Gumps.LastGumpTextExist('ringmail') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 1)  
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 51)
    elif smithy >= 116.3 and smithy <= 118.8: #legs
        if Gumps.LastGumpTextExist('ringmail') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 1)  
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 72)
    elif smithy >= 118.8 and smithy <= 119.9: #tunic
        if Gumps.LastGumpTextExist('ringmail') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 1)  
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 79)  
    Misc.Pause(100)
    
def weight():
    trash = ([0x0F5C,0x143B,0x1441,0x13B6,0x13FF,0x1410,0x1411,0x1413,0x1414,0x1415])
    filter = Items.Filter()
    filter.Enabled = True
    filter.OnGround = False    
    itemfilter = Items.ApplyFilter(filter)
    for item in Player.Backpack.Contains:
        if item.ItemID in trash:
            MoveItem(Items,Misc,item,dropbag)
    if Items.GetPropValue(dropbag,"Contents") > 0 and Items.BackpackCount(0x0FBB,-1) > 0:
        Misc.WaitForContext(dropbag, 10000)
        Misc.ContextReply(0x4033E25D, 0)            

def tools():
    tinkCount = Items.BackpackCount(0x1EB8,-1)
    if tinkCount == 1:
        Player.HeadMessage(255,"Craft tinker tool because we have " + str(tinkCount))
        Items.UseItem(Items.FindByID(0x1EB8,-1,Player.Backpack.Serial,False,False))
        Gumps.WaitForGump(949095101, 10000)
        if Gumps.LastGumpTextExist('scissors') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 15)
        Gumps.WaitForGump(949095101, 10000)  
        Gumps.SendAction(949095101, 23)
    tongCount = Items.BackpackCount(0x0FBB,-1)
    if tongCount == 0:
        Player.HeadMessage(255,"Craft smith tool because we have " + str(tongCount))
        Items.UseItem(Items.FindByID(0x1EB8,-1,Player.Backpack.Serial,False,False))
        Gumps.WaitForGump(949095101, 10000)
        if Gumps.LastGumpTextExist('scissors') == False:
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 15)
        Gumps.WaitForGump(949095101, 10000)  
        Gumps.SendAction(949095101, 86)
        
while True:
    tools()
    smith()
    weight()