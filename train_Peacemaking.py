from Scripts import config
from Scripts.glossary.items.instruments import FindInstrument
Journal.Clear()

while True:
    Player.UseSkill('Peacemaking')
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
    Target.Self()
    Misc.Pause(10500)