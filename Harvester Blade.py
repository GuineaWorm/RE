from Scripts.utilities.items import FindItem, MoveItem
blade = 0x41023F20
corpse = 0x2006
ignore = []
trash = [0x1609,0x09B9,0x1BD1,0x0DF8,0x09F1]

def scan():
    skin = Items.Filter()
    skin.Enabled = True
#    skin.CheckLineOfSight = True
    skin.RangeMin = 0
    skin.RangeMax = 2
    skin.IsCorpse = True

    skins = Items.ApplyFilter(skin)
    for toskin in skins:
        #if toskin:
        if not toskin.Serial in ignore:
            Misc.SendMessage( 'Corpse found', 20 )
            Items.UseItem(blade)
            Target.WaitForTarget(1000)
            Journal.Clear()
            Target.TargetExecute(toskin)
            if Journal.Search(toskin.Name + ":You see nothing useful to carve from the corpse."):# or Journal.Search("You carve some meat and put it in your backpack"):
                Player.ChatSay(toskin.Name + ":You see nothing useful to carve from the corpse.")
                ignore.append(toskin.Serial)
                Misc.Pause(2000)
            while Player.Weight > Player.MaxWeight:
                filter = Items.Filter()
                filter.Enabled = True
                filter.OnGround = False    
                itemfilter = Items.ApplyFilter(filter)
                for item in itemfilter:
                    Misc.SendMessage( 'Fat', 20 )
                    if item.ItemID in trash:
                        MoveItem(Items,Misc,item,toskin.Serial)
                
                Misc.Pause(1000)
        
    else:
        pass
        #Misc.SendMessage( 'No corpse', 20 )

while True:
    scan()
    Misc.Pause(500)