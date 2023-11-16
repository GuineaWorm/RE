## Get BODs v2 by Property Identifiers
##-----------------------
npcNames = ["blacksmith","tailor","tinker","carpenter","bowyer"]
#from System import Byte
#from System.Collections.Generic import List

def FindNPC(target):
    filter = Mobiles.Filter()
    filter.Enabled = True
    filter.RangeMax = 8
    filter.CheckLineOfSite = True
    filter.IsGhost = False
    mobiles = Mobiles.ApplyFilter(filter)
    

    for mobile in mobiles: 
        for tempvar in target:
            if tempvar in Mobiles.GetPropStringByIndex(mobile,0):  
               for x in range(3): 
                    Misc.UseContextMenu(mobile.Serial,"Bulk Order Info",1000)
                    Misc.Pause(650)
                    if Journal.Search("An offer may be available in about"):
                        Journal.Clear()
                        break
                        #want to ignore the NPC
                    else:
                        Gumps.WaitForGump(2611865322, 1000)
                        asd = Gumps.CurrentGump()
                        if asd == 0:
                            break
                        while asd != 0:
                            Gumps.SendAction(2611865322, 1)                       
NPC = FindNPC(npcNames)