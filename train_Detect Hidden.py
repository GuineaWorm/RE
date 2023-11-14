#DH
while Player.GetRealSkillValue('Detect Hidden') < Player.GetSkillCap('Detect Hidden'):
    Player.UseSkill("Detect Hidden")
    Target.WaitForTarget(10000, False)
    Target.Self()
    Misc.Pause(10000)