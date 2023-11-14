## Chivalry Skill Training
PingSpellDelay = 250
#------------------------------------------------------------------------------------------------
FC = Player.FasterCasting
FC = FC * 250
FCR = Player.FasterCastRecovery
FCR = int(((6 - FCR) / 4) * 1000 + PingSpellDelay)

while Player.GetRealSkillValue('Chivalry') < Player.GetSkillCap('Chivalry') and not Player.IsGhost:
    if Player.GetSkillValue('Chivalry') < 40.0:
        Misc.SendMessage('NPC train Necromancy to 40')
        break
    if Player.GetSkillValue('Chivalry') < 50.1:
        t_mana = 10 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            if Player.Hits > 25:
                Spells.CastChivalry('Consecrate Weapon',1)## 10 mana
                tFC = 1500 - FC
                Misc.Pause(tFC)
                Misc.Pause(FCR) 
    if Player.GetSkillValue('Chivalry') > 44.9 and Player.GetSkillValue('Chivalry') < 60.1:
        t_mana = 15 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastChivalry('Divine Fury')## 15 mana
            tFC = 2000 - FC #2 second delay
            Misc.Pause(tFC)
            Misc.Pause(FCR)              
    if Player.GetSkillValue('Chivalry') > 60.0 and Player.GetSkillValue('Chivalry') < 70.1:
        t_mana = 20 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            if Player.Hits > 25:
                Spells.CastChivalry('Enemy of One')## 20 mana
                tFC = 1500 - FC #??? second delay
                Misc.Pause(tFC)
                Misc.Pause(FCR)                     
    if Player.GetSkillValue('Chivalry') > 70.0 and Player.GetSkillValue('Chivalry') < 90.1:
        t_mana = 10 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastChivalry('Holy Light')## 10 mana
            tFC = 2000 - FC #2 second delay
            Misc.Pause(tFC)
            Misc.Pause(FCR)   
    if Player.GetSkillValue('Chivalry') > 90:
        t_mana = 20 - (10 * (Player.LowerManaCost / 100))
        if Player.Mana > t_mana:
            Spells.CastChivalry('Noble Sacrifice')## 20 mana
            tFC = 2250 - FC #2.25 second delay
            Misc.Pause(tFC)
            Misc.Pause(FCR)  
    if Player.Mana < t_mana and Player.GetSkillValue('Meditation') > 50.0: 
        Player.UseSkill('Meditation')
        Misc.Pause(10000)
Misc.SendMessage('Chivalry training complete!')
sys.exit(0)