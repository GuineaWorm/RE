## SAMPIRE
## - Counter Attack
## - Secondary Attack

while True:
#    if not Player.BuffsExist('Enemy Of One'):
#        Spells.CastChivalry('Enemy Of One')
#        Misc.Pause(500)
    if not Player.BuffsExist('Hidden'):
        if not Player.BuffsExist('Webbing'):
            if not Player.BuffsExist('Counter Attack'):
                Spells.CastBushido('Counter Attack') 
                Misc.Pause(100)       
    if Player.Mana > 19:
        #Spells.CastMastery("Onslaught")
        if not Player.HasSpecial:
            Player.WeaponSecondarySA( )
            Misc.Pause(100)
