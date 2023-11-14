#tame 90-120
while Player.GetSkillValue('Animal Taming') < Player.GetSkillCap('Animal Taming'):
    Spells.CastMastery('Combat Training')
    Target.WaitForTarget(10000, False)
    Target.Last( )
    Misc.Pause(1500)
