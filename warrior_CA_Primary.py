## SAMPIRE
## - Counter Attack
## - Primary Attack
Player.HeadMessage(255,"Counter Attack - Primary - Webbing - Onslaught")
sandals = 0x40022F41
Timer.Create("Onslaught",1,"Onslaught timer initialized")

while True:
#    if not Player.BuffsExist('Enemy Of One'):
#        Spells.CastChivalry('Enemy Of One')
#        Misc.Pause(500)
    if not Player.BuffsExist("Hidden"):
        if not Player.BuffsExist('Counter Attack'):
            Spells.CastBushido('Counter Attack') 
            Misc.Pause(100)       
    if Player.Mana > 20:
        if Timer.Check("Onslaught") == False:
            Spells.CastMastery("Onslaught")
            Timer.Create("Onslaught",10000,"Onslaught timer deactivated")
            Misc.Pause(100)
        if not Player.HasSpecial:
            Player.WeaponPrimarySA( )
            Misc.Pause(100)
    if Journal.SearchByType( 'You are wrapped', 'System' ):
        while Player.CheckLayer("Shoes") == True:
            Player.UnEquipItemByLayer("Shoes",100)
            Misc.Pause(100)
        while Player.CheckLayer("Shoes") == False:
            Player.EquipItem(sandals)
            Misc.Pause(100)
        while Player.CheckLayer("Shoes") == True:
            Player.UnEquipItemByLayer("Shoes",100)
            Misc.Pause(100)
        Journal.Clear()   
   
         
while False:
    Player.HeadMessage(255,"Counteasdasd- Onslaught")        
    if Player.BuffsExist("Webbing"):
        Player.HeadMessage(255,"1")
        if Player.CheckLayer("Shoes") == False:
            Player.HeadMessage(255,"2")
            Player.EquipItem(sandals)
        else:
            Player.UnEquipItemByLayer("Shoes",100)
            Player.HeadMessage(255,"3")
    if Player.CheckLayer("Shoes") == True:
        Player.UnEquipItemByLayer("Shoes",100)
        Player.HeadMessage(255,"4")
