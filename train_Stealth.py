# Bushido Skill Training
while Player.GetRealSkillValue('Bushido') < Player.GetSkillCap('Bushido') and not Player.IsGhost:
    if Player.GetSkillValue('Bushido') < 30.0:
        Misc.SendMessage('NPC train Bushido to 30')
        break
    if Player.GetSkillValue('Bushido') < 60.0:
        ## 10 mana
        t_mana = 10 * (Player.LowerManaCost / 100)
        if Player.Mana > t_mana:
            Spells.CastBushido('Confidence')   
    if Player.GetSkillValue ('Bushido') > 59.9 and Player.GetSkillValue('Bushido') < 75.0:
        ## 5 mana
        t_mana = 5 * (Player.LowerManaCost / 100)
        if Player.Mana > t_mana:
            Spells.CastBushido('Counter Attack')
    if Player.GetSkillValue('Bushido') > 74.9 and Player.GetSkillValue('Bushido') < 105.0:
        ## 10 mana
        t_mana = 10 * (Player.LowerManaCost / 100)
        if Player.Mana > t_mana:
            Spells.CastBushido('Evasion')
            Misc.Pause(1000)
            if Player.BuffsExist('Evasion'):
                Misc.Pause(20000)
    if Player.GetSkillValue('Bushido') > 104.9 and Player.GetSkillValue('Bushido') < 120.0:
        ## 10 mana
        t_mana = 10 * (Player.LowerManaCost / 100)
        if Player.Mana > t_mana:
            Spells.CastBushido('Momentum Strike')
    Misc.Pause(500)
Misc.SendMessage('Bushido training complete!')