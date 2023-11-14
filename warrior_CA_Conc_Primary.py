## SAMPIRE
## - Counter Attack
## - Primary Attack

while True:
    if not Player.BuffsExist('Enemy Of One'):
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(500)
    if not Player.BuffsExist('Consecrate Weapon'):
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(500)    
    if Player.Mana > 19:
        #Spells.CastMastery("Onslaught")
        if not Player.HasSpecial:
            Player.WeaponPrimarySA( )
            Misc.Pause(100)
