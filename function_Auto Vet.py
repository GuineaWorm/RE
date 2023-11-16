# This script will run UNTIL you stop it. If you hotkey it, think of it as an on/off switch.
# Add the serials of pets you want to heal to the petList
from System.Collections.Generic import List
from System import Int32, Byte
import sys

def lazyLoad():
    Misc.Pause(1000)
    if Journal.SearchByName('Welcome,', 'System'):
        Misc.SendMessage('Fresh login, Autovet starting in 2secs...',33)
        Journal.Clear()
        Misc.Pause(2000)
        Misc.SendMessage('Autovet started',0x0044)
lazyLoad()

petList = [
 0x0004F4C1,0x000456DC,0x00064BA3 # Add your pet serials here separated by a comma
]

bands = Items.FindByID(0x0E21, 0, Player.Backpack.Serial)

def pauseLoot():
    Misc.SetSharedValue("Lootmaster:Pause", True)

def startLoot():
    Misc.RemoveSharedValue("Lootmaster:Pause")

def petTarget():
    Target.WaitForTarget(2000,True)
    if Target.HasTarget():
        Target.TargetExecute(g)

def castCheck():
    while Player.Paralized or Target.HasTarget():
        Misc.Pause(1)
        if not Player.Paralized and not Target.HasTarget():
            break
        Misc.Pause(20)
    Misc.Pause(20)

def blockCheck():
    while not Player.Visible or 'Mortal Strike' in str(g.Properties):
        Misc.Pause(1)
        if Player.Visible or not 'Mortal Strike' in str(g.Properties):
            break
        Misc.Pause(20)

def healWait():
    Misc.Pause(320)
    while Player.BuffsExist('Veterinary'):
        Misc.Pause(1)
        if not Player.BuffsExist('Veterinary'):
            break
        Misc.Pause(20)
    startLoot()

def bandage():
    pauseLoot()
    Items.UseItem(bands)
    Misc.Pause(100)
    petTarget()
    healWait()

def bandCheck():
    bands = Items.FindByID(0x0E21, 0, Player.Backpack.Serial)
    while not bands:
        Misc.Pause(1)
        bands = Items.FindByID(0x0E21, 0, Player.Backpack.Serial)
        if bands:
            break
        Misc.Pause(20)
    total = Items.ContainerCount(Player.Backpack.Serial, 0x0E21, -1, -1)
    if total < 75:
        Player.HeadMessage(33,'Bandages running low, restock soon')


petfilter = Mobiles.Filter()
petfilter.Enabled = True
petfilter.RangeMax = 15
petfilter.IsHuman = False
petfilter.IsGhost = False
petfilter.Serials = List[Int32] (petList)

while Player.IsGhost == False:
    Misc.Pause(1)    
    petList = Mobiles.ApplyFilter(petfilter)   
    for g in petList:
        g = Mobiles.Select(petList, 'Weakest')
            
        #check health level if in range one of guilded meta pet heals with bandages.          
        if g.Hits <= g.HitsMax * 0.96 and Player.DistanceTo(g) < 2:
            bandCheck()
            castCheck()
            blockCheck()
            Player.HeadMessage(0x0502, 'Healing: ' + (g.Name))
            bandage()
            Journal.Clear()
            break        
        if Journal.Search("too far away"):
            Journal.Clear()
        elif Journal.Search("stay close enough"):
            Player.HeadMessage(95, "You moved")
            Journal.Clear()
    Misc.Pause(50)
Misc.Pause(50)