from System.Collections.Generic import List
from System import Int32 

def auto():
    #attack all of a type
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 15
    fil.Bodies = List[Int32]([0x0023,0x0024,0x00F2])
    #fil.Graphics(0x0023)
    enemies = Mobiles.ApplyFilter(fil)
    for enemy in enemies:
        #if enemy.MobileID = 0x0023
        #print(str(enemy.Name))
        Player.Attack(enemy.Serial)
        if not Player.HasSpecial:
            Player.WeaponPrimarySA()
        Misc.Pause(500)   
        #Mobiles.Filter.Graphics
        Misc.Pause(100)
    Misc.Pause(100)
    
while True:    
    auto()