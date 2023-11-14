from Scripts.utilities.items import FindItem, MoveItem
while True:
    trash = 0x404B4F7A
    crap = ([0x13B2,0x0F50,0x26C2,0x13FD,0x26C3])
    filter = Items.Filter()
    filter.Enabled = True
    filter.OnGround = False    
    itemfilter = Items.ApplyFilter(filter)
    for item in Player.Backpack.Contains:
        if item.ItemID in crap:
            MoveItem(Items,Misc,item,trash)