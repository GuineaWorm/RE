##Kotl Chests
############
from System.Collections.Generic import List 
from System import Byte, Int32 as int
from Scripts.utilities.items import FindItem, MoveItem

picks = Items.FindByID(0x14FC,-1,Player.Backpack.Serial,False,False)

Player.UseSkill("Detecting Hidden")
Target.WaitForTarget(1000)
Target.Self()
Misc.Pause(100)
Timer.Create("DH", 10000, "Detect hidden timer over.")


boxfil = Items.Filter()
boxfil.RangeMax = 6
boxfil.OnGround = True
boxfil.Movable = False
boxfil.Graphics = List[int]((0x4D0C,0x4D0D)) #chest ID
box = Items.ApplyFilter(boxfil)

for temp in box:
    if temp != None:
        Journal.Clear()
        bool = 1
        Player.HeadMessage(316,"Found box!")
        while Player.DistanceTo(temp) != 1:
            Misc.Pause(100)
        while bool == 1:
            Player.HeadMessage(1310,"Lock picking...")
            Items.UseItem(picks)
            Target.WaitForTarget(1000)
            Target.TargetExecute(temp)
            if Journal.SearchByType('The lock quickly yields','Regular') or Journal.SearchByType('This does not appear to be locked','System'):
                Player.HeadMessage(671,"Lock picked!")
                bool = 0    
        while Timer.Check("DH") != False:
            Misc.Pause(100)
        bool = 1
        while bool == 1:
            Player.HeadMessage(1310,"Removing trap...")
            Player.UseSkill("Remove Trap")
            Target.WaitForTarget(1000)
            Target.TargetExecute(temp)
            bool2 = 2
            while bool2 == 2:
                if Journal.SearchByType('You successfully render the trap','System'):
                    Player.HeadMessage(671,"Trap removed!")
                    bool = 0
                    break
                if Journal.SearchByType('appear to be trapped','System'):
                    Player.HeadMessage(671,"Trap removed!")
                    bool = 0
                    break
                if Journal.SearchByType('You fail to disarm','System'):
                    Player.HeadMessage(1646,"Trap still active!")
                    Misc.Pause(10000)
                    Journal.Clear()
                    bool2 = 1
                else:
                    Misc.Pause(1000)
            
        Items.UseItem(temp.Serial)