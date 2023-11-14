fishIDs = [ 0x09CF, 0x09CE, 0x09CC, 0x09CD, 0x0DD6, 0x44C6, 0x4307, 0x4303, 0x44C3, 0x44C4, 0x4306 ]
chopFish = True
sharedFishChopperId = 'fishChopper'

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

def ChopFish():
    if not chopFish or not Misc.CheckSharedValue(sharedFishChopperId):
        return
    if Player.Weight > (Player.MaxWeight * .9):
        chopper = Items.FindBySerial(Misc.ReadSharedValue(sharedFishChopperId))
        if chopper is None:
            return
        for item in Player.Backpack.Contains:
            if item.ItemID in fishIDs:
                Items.UseItem(chopper)
                Target.WaitForTarget(1000,False)
                Target.TargetExecute(item)
                Misc.Pause(700)
    

def dismount():
    if Player.Mount is None:
        return
    Mobiles.UseMobile(Player.Serial)
    
def CheckForPoleAndEquip():
    pole = None
    for layer in ['RightHand','LeftHand']:
        if Player.CheckLayer(layer):
            Player.UnEquipItemByLayer(layer,1250)
            Misc.Pause(700)
    pole = Items.FindByID(0x0DC0, -1, Player.Backpack.Serial, 2)
    if pole is not None:
        Player.EquipItem(pole)
        Misc.Pause(700)
    return pole
   
Journal.Clear() # Clear journal in scan as to not detect a previous end.

def DoFishing(): # create method.
    skilGain = 0
    pole = CheckForPoleAndEquip()#Unequip, check for pole, and equip if found.Amount
    if pole is None: #check for pole existence
        Misc.SendMessage('no fishing pole') # Send system message to player.
        return
    waterSpots = GetGatherGridCoordinates() #optional sizeX, sizeY for survey size, default is 6x6
    if len(waterSpots) == 0:
        Misc.SendMessage('no locations to fish') # Send system message to player.
        return
    Misc.SendMessage('LETS FISH', 44)
    dismount()
    for spot in waterSpots:
        Journal.Clear()
        Player.TrackingArrow(spot["x"],spot["y"],True)
        earlyEnd = False
        while not Journal.Search("seem to be biting here."):# Do everything inside here until this message comes up in journal.
            if Target.HasTarget():
                Target.Cancel()
            ChopFish()
            Items.UseItem(pole) # Use Fishing Pole. 
            Target.WaitForTarget(1500) # Wait 1.5 seconds for a target.
            Misc.SendMessage('Targeting: [' + str(spot["id"]) + '] ' +  ' x '.join([str(spot["x"]),str(spot["y"]),str(spot["z"])]))
            Target.TargetExecute(spot["x"], spot["y"], spot["z"], spot["id"]) #target location to fish
            Misc.Pause(300)
            if Journal.Search("cannot be seen.") or Journal.Search("need to be closer"):
                Misc.Pause(700)
                break
            if not Journal.Search("seem to be biting here."):
                Misc.Pause(7550)
    Player.TrackingArrow(0,0,False)
    Misc.SendMessage('FISHING COMPLETE', 44)

    
if chopFish and not Misc.CheckSharedValue(sharedFishChopperId):
    Misc.SetSharedValue(sharedFishChopperId, Target.PromptTarget('Where is your chopper?'))
DoFishing() # run method above.