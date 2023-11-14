#eb last
while True:
    Spells.CastMagery("Energy Bolt")
    Target.WaitForTarget(10000, False)
    Target.Last()
    Misc.Pause(1000)