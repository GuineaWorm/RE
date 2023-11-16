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
                Misc.UseContextMenu(mobile.Serial,"Bulk Order Info",1000)
                Misc.Pause(650)
                if Journal.Search("An offer may be available in about"):
                    Journal.Clear()
                    #want to ignore the NPC
                else:
                    #Gumps.WaitForGump(2696865991, 1000)
                    asd = Gumps.CurrentGump()
                    if asd == 0:
                        break
                    while asd != 0:
                        Gumps.SendAction(Gumps.CurrentGump(), 1)
                        if Gumps.CurrentGump() == 0:
                            asd = 0
                    Misc.Pause(1000)  
                    for i in range(2): #needs to reiterate UseContext and GetBods 2 more times
                        Misc.UseContextMenu(mobile.Serial,"Bulk Order Info",1000)   
                        Misc.Pause(650)   
                        #Gumps.WaitForGump(2611865322, 1000)
                        asd = Gumps.CurrentGump()
                        if asd == 0:
                            break
                        while asd != 0:
                            Gumps.SendAction(Gumps.CurrentGump(), 1)
                            if Gumps.CurrentGump() == 0:
                                asd = 0
                        Misc.Pause(1000) 

                        
NPC = FindNPC(npcNames)