from Scripts.utilities.items import FindItem, MoveItem
rune = 0x406DC1F8

def start():
    Items.UseItem(0x400C5F98)
    Target.WaitForTarget(500)
    while Target.HasTarget():
        Misc.Pause(500)
    Journal.Clear()   
    
start()

def fish():
    Items.UseItem(0x400C5F98)
    Target.WaitForTarget(1000,False)
    Target.Last()

def jscan():
    i = 1
    while i == 1:
        if Journal.SearchByType( 'You pull out', 'System' ):
            Journal.Clear()
            i = 2
        if Journal.SearchByType( 'You fish a while,', 'System' ):
            Journal.Clear()
            i = 2
        if Journal.SearchByType( 'The fish', 'System' ):
            Journal.Clear()        
            Player.HeadMessage(1100,"Time to move on!")
            Misc.Pause(500)
            Items.UseItem(0x400C5F98)
            while Target.HasTarget():
                Misc.Pause(500)
        if Journal.SearchByType( 'Uh oh! That', 'System' ):  
            Journal.Clear()        
            Player.HeadMessage(1100,'Buckle up, there be sneks!')
            i = 2
        if Journal.SearchByType( 'Your fishing pole bends', 'System'):
            Journal.Clear()
            i = 2
        if Journal.Search('fdone'):
            Stop
        if Journal.SearchByType('You must wait', 'System'):
            i = 2
            
def weight():
    fish = ([0x4302, 0x097A, 0x573A, 0x09CC, 0x09CD, 0x09CE, 0x09CF, 0x4303, 0x4304, 0x4305, 0x4306, 0x4307, 0x44C3, 0x44C4, 0x44C5, 0x44C6])
    if Player.Weight > Player.MaxWeight - 30:
        Spells.CastMagery('Mark')
        Target.WaitForTarget(2000)
        Target.TargetExecute(rune)
        Misc.Pause(1000)
        Spells.CastMagery('Recall')
        Target.WaitForTarget(2000)
        Target.TargetExecute(0x40431F3F)        
        Misc.Pause(1500)
        filter = Items.Filter()
        filter.Enabled = True
        filter.OnGround = False    
        itemfilter = Items.ApplyFilter(filter)
        for item in itemfilter:
            if item.ItemID in fish:
                MoveItem(Items,Misc,item,0x4082C364)
                #Misc.Pause(500)
        Spells.CastMagery('Recall')
        Target.WaitForTarget(2000)
        Target.TargetExecute(rune)        
        Misc.Pause(2000)
        Journal.Clear() 
        start()
    
while True:
    jscan()
    weight()
    fish()
