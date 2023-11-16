## Get BODs
##-----------------------
npcSerials = [0x000001CC,0x0000027C,0x00000280,0x00000282,0x0000016E,0x000657BD]
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
        if mobile.Serial in target:          
            Misc.UseContextMenu(mobile.Serial,"Bulk Order Info",1000)
            Misc.Pause(650)
            if Journal.Search("An offer may be available in about"):
                Journal.Clear()
                #want to ignore the NPC
            else:
                Gumps.WaitForGump(2611865322, 10000)
                Gumps.SendAction(2611865322, 1)   
                for i in range(2):
                    Misc.UseContextMenu(mobile.Serial,"Bulk Order Info",1000)   
                    Misc.Pause(650)   
                    Gumps.WaitForGump(2611865322, 10000)
                    Gumps.SendAction(2611865322, 1)                
                    #needs to reiterate UseContext and GetBods 2 more times
        else:
            print((mobile.Name))

            
NPC = FindNPC(npcSerials)