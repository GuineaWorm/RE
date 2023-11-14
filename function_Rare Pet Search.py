from System.Collections.Generic import List
from System import Byte
from System import Int32 as int
import winsound

sound = True #True or False
uncommon = False #True or False
rare = True #True or False
epic = True #True or False
legendary = True #True or False
times_to_ding = 5
check_status = 120000 #time in MS to send message that we are running still
spam_message_check = 5

for z in range(spam_message_check):
    Misc.SendMessage("*Looking for rare animals.*",255)
    Misc.Pause(100)
Timer.Create("rares", check_status, "")

while True:
    mobileFilter = Mobiles.Filter()
    mobileFilter.Enabled = True
    mobileFilter.Notorieties = List[Byte](bytes([1,2,3,4,6]))
    foundMobiles = Mobiles.ApplyFilter(mobileFilter)
    if Timer.Check("rares") == False:
        for z in range(spam_message_check):
            Misc.SendMessage("*Looking for rare animals.*",255)
            Misc.Pause(100)
        Timer.Create("rares", check_status, "")    
    for i in foundMobiles:
        if "Uncommon" in Mobiles.GetPropStringByIndex(i.Serial,1) and uncommon == True:
            for x in range(times_to_ding):
                Player.HeadMessage(40,"Uncommon Found!")
                Mobiles.Message(i.Serial,40,"uncommon",25)
                Misc.Pause(1000)
                if sound == True:
                    winsound.PlaySound("...\WARNING2.wav",1)
            stop
        if "Rare" in Mobiles.GetPropStringByIndex(i.Serial,1) and rare == True:
            for x in range(times_to_ding):
                Player.HeadMessage(30,"Rare Found!")
                Mobiles.Message(i.Serial,30,"rare",25)
                Misc.Pause(1000)
                if sound == True:
                    winsound.PlaySound("...\WARNING2.wav",1)
            stop
        if "Epic" in Mobiles.GetPropStringByIndex(i.Serial,1) and epic == True:
            for x in range(times_to_ding):
                Player.HeadMessage(10,"Epic Found!")
                Mobiles.Message(i.Serial,10,"epic",25)
                Misc.Pause(1000)
                if sound == True:
                    winsound.PlaySound("...\WARNING2.wav", 1)
            stop
        if "Legendary" in Mobiles.GetPropStringByIndex(i.Serial,1) and legendary == True:
            for x in range(times_to_ding):
                Player.HeadMessage(20,"Legendary Found!")
                Mobiles.Message(i.Serial,20,"legendary",25)
                Misc.Pause(1000)
                if sound == True:
                    winsound.PlaySound("...\WARNING2.wav",1)
            stop
    Misc.Pause(200)