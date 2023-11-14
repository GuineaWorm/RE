from Scripts import config
from Scripts.glossary.items.instruments import FindInstrument
Journal.Clear()
target = Target.PromptTarget("Target 1", 33);
targ1  = Mobiles.FindBySerial(target);
target = Target.PromptTarget("Target 2", 33);
targ2  = Mobiles.FindBySerial(target);
while True:
    Player.UseSkill('Provocation')
    Target.WaitForTarget(500)
    if Journal.Search( 'What instrument shall you play?' ):
        #Instrument either broke or hasn't been selected
        instrument = FindInstrument( Player.Backpack )
        if instrument == None:
            #No more instruments, stop the provo attempt
            Target.Cancel()
            Misc.SendMessage( 'Ran out of instruments to train with', colors[ 'red' ] )
            stop
        else:
            Target.WaitForTarget(2000, True)
            Target.TargetExecute(instrument.Serial)
            Journal.Clear()
    Target.TargetExecute(targ1.Serial)
    Target.WaitForTarget(500)
    Target.TargetExecute(targ2.Serial)
    Misc.Pause(10500)