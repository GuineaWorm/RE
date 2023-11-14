from Scripts.utilities.items import FindItem, MoveItem
rune = 0x406DC1F8
#Items.UseItem(0x400C5F98)
#Target.WaitForTarget(500)
Journal.Clear()   

def fish():
    waterSpots = GetGatherGridCoordinates() #optional sizeX, sizeY for survey size, default is 6x6
    if len(waterSpots) == 0:
        Misc.SendMessage('no locations to fish') # Send system message to player.
        return
    Misc.SendMessage('LETS FISH', 44)
    for spot in waterSpots:
        #Player.ChatSay(str(spot))
        Journal.Clear()
        Player.TrackingArrow(spot["x"],spot["y"],False)
        earlyEnd = False
        while not Journal.Search("seem to be biting here."):# Do everything inside here until this message comes up in journal.
            if Target.HasTarget():
                Target.Cancel()
            weight()
            Items.UseItem(0x400C5F98) # Use Fishing Pole. 
            Target.WaitForTarget(1500) # Wait 1.5 seconds for a target.
            Misc.SendMessage('Targeting: [' + str(spot["id"]) + '] ' +  ' x '.join([str(spot["x"]),str(spot["y"]),str(spot["z"])]))
            Target.TargetExecute(spot["x"], spot["y"], spot["z"], spot["id"]) #target location to fish
            Timer.Create("timer",10000)
            Misc.Pause(500)
            if Journal.Search("cannot be seen.") or Journal.Search("need to be closer"):
                Misc.Pause(500)
                break
            i = 1
            while i == 1:
                if not Timer.Check("timer"):
                    Journal.Clear()
                    i = 2
                if Journal.SearchByType( 'You pull out', 'System' ):
                    Journal.Clear()
                    i = 2
                if Journal.SearchByType( 'You fish a while,', 'System' ):
                    Journal.Clear()
                    i = 2
                if Journal.SearchByType( 'The fish', 'System' ):
                    #Journal.Clear()        
                    #Player.HeadMessage(1100,"Time to move on!")
                    #Misc.Pause(500)
                    #Items.UseItem(0x400C5F98)
                    #while Target.HasTarget():
                    #    Misc.Pause(500)
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
    fish = ([0x09CC, 0x09CD, 0x09CE, 0x09CF, 0x4303, 0x4304, 0x4305, 0x4306, 0x4307, 0x44C3, 0x44C4, 0x44C5, 0x44C6, 0x573A])
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
        Misc.Pause(1500)
        
def GetGatherGridCoordinates(sizeX = 6, sizeY = 6):
    coords = []
    for x in range(-1 * sizeX,sizeX + 1):
        for y in range(-1 * sizeY,sizeY + 1):
             tileX = Player.Position.X+x
             tileY = Player.Position.Y+y
             landinfo = Statics.GetStaticsLandInfo(tileX, tileY, Player.Map)
             if landinfo is not None:
                 staticId = landinfo.StaticID
                 staticZ = landinfo.StaticZ
                 isWet =  Statics.GetLandFlag(staticId,'Wet')
                 tileinfo = Statics.GetStaticsTileInfo(tileX, tileY, Player.Map)
                 if tileinfo.Count == 0:
                     staticId = 0x0000
                 if not isWet and tileinfo.Count == 1:
                     isWet = Statics.GetTileFlag(tileinfo[0].StaticID,'Wet')
                     if isWet:
                          staticId = tileinfo[0].StaticID
                          staticZ = tileinfo[0].StaticZ
                 if isWet:
                    coords.append({"x": tileX, "y": tileY, "z": staticZ, "id": staticId})
                    continue
             else:
                tileinfo = Statics.GetStaticsTileInfo(tileX, tileY, Player.Map)
                if tileInfo.Count == 1:
                    tile = tileinfo[0]
                    tileWet = Statics.GetTileFlag(tile.StaticID,'Wet')
                    isWet = Statics.GetTileFlag(tile.StaticID,'Wet')
                    if isWet:
                        coords.append({"x": tileX, "y": tileY, "z": tile.StaticZ, "id": tile.StaticID})
    return coords
    
while True:
    fish()
