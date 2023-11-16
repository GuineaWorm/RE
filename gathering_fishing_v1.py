from Scripts.utilities.items import FindItem, MoveItem
dropbag = 0x4084B4A6
fishingpole = 0x403BC812

Journal.Clear()   
def fish():
    Items.UseItem(fishingpole)
    Target.WaitForTarget(1000,False)
    Target.TargetExecute(Player.Position.X,Player.Position.Y,Player.Position.Z-4)

def jscan():
    i = 1
    Journal.Clear() 
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
            X1 = Player.Position.X
            Y1 = Player.Position.Y
            while Misc.Distance(X1, Y1, Player.Position.X, Player.Position.Y) < 8:
                Player.ChatSay("Forward")
                Misc.Pause(500)  
            Player.ChatSay("Stop")              
            i = 2
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
    fish = ([0x44D1,0x44D2,0x44D3,0x44D4,0x44C6,0x44C4,0x4305,0x4307,0x4306,0x4302,0x097A,0x573A,0x09CC,0x09CD,0x09CE,0x09CF,0x4303,0x4304,0x4305,0x4306,0x4307,0x44C3,0x44C4,0x44C5,0x44C6])
    filter = Items.Filter()
    filter.Enabled = True
    filter.OnGround = False    
    itemfilter = Items.ApplyFilter(filter)
    for item in Player.Backpack.Contains:
        if item.ItemID in fish:
            MoveItem(Items,Misc,item,dropbag)
                #Misc.Pause(500)
   # for x in range(len(crabs)):
   #     temp = Items.FindByID(crabs[x],-1,Player.Backpack.Serial,False,False)
   #     while temp != None:
   #         MoveItem(Items,Misc,temp,dropbag)
   #         temp = Items.FindByID(crabs[x],-1,Player.Backpack.Serial,False,False)    
while True:
    fish()
    jscan()
    weight()