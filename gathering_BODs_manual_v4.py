## Get BODs v4 by Property Identifiers
##-----------------------
npcNames = ["blacksmith","tailor","tinker","carpenter","bowyer"]
#from System import Byte
#from System.Collections.Generic import List
Journal.Clear()
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
                for i in range(3):
                    Misc.UseContextMenu(mobile.Serial,"Bulk Order Info",1000)
                    Misc.Pause(500)
                    if Journal.SearchByType('An offer may be available in about', 'Regular'):
                        Journal.Clear()
                        break #want to ignore the NPC
                    else:
                    #Gumps.WaitForGump(2696865991, 1000)
                        asd = Gumps.CurrentGump()
                        if asd == 0:
                            break
                        while asd != 0:
                            Gumps.SendAction(Gumps.CurrentGump(), 1)
                            if Gumps.CurrentGump() == 0:
                                asd = 0
                                Misc.Pause(500)
                        
NPC = FindNPC(npcNames)