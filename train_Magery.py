## Bushido Skill Training
PingSpellDelay = 0
#------------------------------------------------------------------------------------------------
FC = Player.FasterCasting
FC = FC * 250
FCR = Player.FasterCastRecovery
FCR = int(((6 - FCR) / 4) * 1000 + PingSpellDelay)
#if Player.GetSkillValue('Magery') > 69.9 or Player.GetSkillValue('Mysticisim') > 69.9 and FC > 2:
#    FC = 2
while Player.GetRealSkillValue('Magery') < Player.GetSkillCap('Magery') and not Player.IsGhost:
    if Player.GetSkillValue('Magery') < 30.0:
        Misc.SendMessage('NPC train Magery to 30')
        break
    if Player.GetSkillValue('Magery') < 45.1:
        t_mana = int(9 - (10 * (Player.LowerManaCost / 100)))
        if Player.Mana > t_mana:
            Spells.CastMagery('Bless')## 9 mana
            Target.WaitForTarget(1500)
            Target.Self()
            Misc.Pause(FCR)
    if Player.GetSkillValue('Magery') > 45.0 and Player.GetSkillValue('Magery') < 55.1:
        t_mana = int(11 - (10 * (Player.LowerManaCost / 100)))
        if Player.Mana > t_mana:
            Spells.CastMagery('Greater Heal')## 11 mana
            Target.WaitForTarget(1750)
            Target.Self()
            Misc.Pause(FCR)
    if Player.GetSkillValue('Magery') > 55.0 and Player.GetSkillValue('Magery') < 65.1:
        t_mana = int(14 - (10 * (Player.LowerManaCost / 100)))
        if Player.Mana > t_mana:
            Spells.CastMagery('Magic Reflection')## 14 mana 
            tFC = 1500 - FC #1.5 second delay
            Misc.Pause(tFC)
            Misc.Pause(FCR)                     
    if Player.GetSkillValue('Magery') > 65.0 and Player.GetSkillValue('Magery') < 75.1:
        t_mana = int(20 - (10 * (Player.LowerManaCost / 100)))
        if Player.Mana > t_mana:
            Spells.CastMagery('Reveal')## 20 mana
            Target.WaitForTarget(2250)
            Target.Self() 
            Misc.Pause(FCR) 
    if Player.GetSkillValue('Magery') > 75.0 and Player.GetSkillValue('Magery') < 90.1:
        t_mana = int(40 - (10 * (Player.LowerManaCost / 100)))
        if Player.Mana > t_mana:
            Spells.CastMagery('Mass Dispel')## 40 mana
            Target.WaitForTarget(2500)
            Target.Self() 
            Misc.Pause(FCR)
    if Player.GetSkillValue('Magery') > 90.0:
        t_mana = int(50 - (10 * (Player.LowerManaCost / 100)))
        if Player.Mana > t_mana:
            Spells.CastMagery('Earthquake')## 50 mana
            tFC = 2250 - FC #2.25 second delay
            Misc.Pause(tFC)
            Misc.Pause(FCR)
    if Player.Mana < t_mana: 
        Player.UseSkill('Meditation')
        Misc.Pause(10000)
Misc.SendMessage('Magery training complete!')
sys.exit(0)