from System.Collections.Generic import List
from System import Byte

Player.HeadMessage(255,"BOTTLE SCRIPT STARTED")
mobile = Mobiles.Filter()
mobile.Enabled = True
mobile.Notorieties = List[Byte](bytes([6]))
mobile.RangeMax = 10

filter = Items.Filter()
filter.Enabled = True
filter.Name = 'A Bottle of Liquor'
filter.RangeMax = 2

while True:
    list = Items.ApplyFilter(filter)
    for item in list:
        Items.UseItem(item)
        Target.WaitForTarget(500)
        mobiles = Mobiles.ApplyFilter(mobile)
        if len(mobiles) > 0:
            Target.TargetExecute(mobiles[0])