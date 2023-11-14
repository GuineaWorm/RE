## Bushido Skill Training
PingSpellDelay = 400
#------------------------------------------------------------------------------------------------
FC = Player.FasterCasting
FCR = Player.FasterCastRecovery
FCR = int(((6 - FCR) / 4) * 1000 + PingSpellDelay)
if Player.GetSkillValue('Magery') > 69.9 or Player.GetSkillValue('Mysticisim') > 69.9 and FC > 2:
    FC = 2
while Player.GetRealSkillValue('Bushido') < Player.GetSkillCap('Bushido') and not Player.IsGhost:
    if Player.GetSkillValue('Bushido') < 30.0:
        Misc.SendMessage('NPC train Bushido to 30')
        break
    if Player.GetSkillValue('Bushido') < 60.0:
        t_mana = 10 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastBushido('Confidence')## 10 mana
            if FC > -1:
                Misc.Pause(250)
                Misc.Pause(FCR)
            if FC < 0:
                fc_var = int(-1000 * ((FC / 4) - 0.25))
                Misc.Pause(fc_var)
                Misc.Pause(FCR)
    if Player.GetSkillValue ('Bushido') > 59.9 and Player.GetSkillValue('Bushido') < 75.0:
        t_mana = 5 - (5 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastBushido('Counter Attack')## 5 mana
            if FC > -1:
                Misc.Pause(250)
                Misc.Pause(FCR)
            if FC < 0:
                fc_var = int(-1000 * ((FC / 4) - 0.25))
                Misc.Pause(fc_var)
                Misc.Pause(FCR)
    if Player.GetSkillValue('Bushido') > 74.9 and Player.GetSkillValue('Bushido') < 97.5:
        t_mana = 10 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastBushido('Evasion')## 10 mana
            if FC > -1:
                Misc.Pause(250)
                Misc.Pause(FCR)
                if Player.BuffsExist('Evasion'):
                    Misc.Pause(20000)
            if FC < 0:
                fc_var = int(-1000 * ((FC / 4) - 0.25))
                Misc.Pause(fc_var)
                Misc.Pause(FCR)
                if Player.BuffsExist('Evasion'):
                    Misc.Pause(20000)                       
    if Player.GetSkillValue('Bushido') > 97.4 and Player.GetSkillValue('Bushido') < 120.0:
        t_mana = 10 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana >= t_mana: 
            if not Player.BuffsExist('Momentum Strike'):
                Spells.CastBushido('Momentum Strike')## 10 mana
        Misc.Pause(250)
Misc.SendMessage('Bushido training complete!')
sys.exit(0)