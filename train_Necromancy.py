## Necromancy Skill Training
PingSpellDelay = 250
#------------------------------------------------------------------------------------------------
FC = Player.FasterCasting
FC = FC * 250
FCR = Player.FasterCastRecovery
FCR = int(((6 - FCR) / 4) * 1000 + PingSpellDelay)

while Player.GetRealSkillValue('Necromancy') < Player.GetSkillCap('Necromancy') and not Player.IsGhost:
    if Player.GetSkillValue('Necromancy') < 40.0:
        Misc.SendMessage('NPC train Necromancy to 40')
        break
    if Player.GetSkillValue('Necromancy') < 50.1:
        t_mana = 5 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            if Player.Hits > 25:
                Spells.CastNecro('Pain Spike',Player.Serial,1)## 5 mana
                tFC = 1500 - FC
                Misc.Pause(tFC)
                Misc.Pause(FCR) 
    if Player.GetSkillValue('Necromancy') > 50.0 and Player.GetSkillValue('Necromancy') < 70.1:
        t_mana = 11 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastNecro('Horrific Beast')## 11 mana
            tFC = 2000 - FC #2 second delay
            Misc.Pause(tFC)
            Misc.Pause(FCR)              
    if Player.GetSkillValue('Necromancy') > 70.0 and Player.GetSkillValue('Necromancy') < 90.1:
        t_mana = 23 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            if Player.Hits > 25:
                Spells.CastNecro('Wither',Player.Serial,1)## 23 mana
                tFC = 1500 - FC #??? second delay
                Misc.Pause(tFC)
                Misc.Pause(FCR)                     
    if Player.GetSkillValue('Necromancy') > 90.0 and Player.GetSkillValue('Necromancy') < 100.1:
        t_mana = 23 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastNecro('Lich Form')## 23 mana
            tFC = 2000 - FC #2 second delay
            Misc.Pause(tFC)
            Misc.Pause(FCR)   
    if Player.GetSkillValue('Necromancy') > 100:
        t_mana = 23 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastNecro('Vampiric Embrace')## 23 mana
            tFC = 2250 - FC #2.25 second delay
            Misc.Pause(tFC)
            Misc.Pause(FCR)  
    if Player.Mana < t_mana and Player.GetSkillValue('Meditation') > 50.0: 
        Player.UseSkill('Meditation')
        Misc.Pause(10000)
Misc.SendMessage('Necromancy training complete!')
sys.exit(0)