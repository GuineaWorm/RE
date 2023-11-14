#Boat Navigation
#Utilized Dramoor's spell grid example to create

#setX = 0 #x location of gump on screen (if gump up have to click button to move)
#setY = 0 # y location of gump on screen (same)

def sendgump(): #Method to call to send gump.
    gd = Gumps.CreateGump()
    Gumps.AddPage(gd, 0);
    #row1
    Gumps.AddButton(gd, 20, 20, 4507, 4507, 1, 1, 0)
    Gumps.AddTooltip(gd, r"Forward-Left")
    Gumps.AddButton(gd, 50, 0, 4500, 4500, 2, 1, 0)
    Gumps.AddTooltip(gd, r"Forward")
    Gumps.AddButton(gd, 78, 20, 4501, 4501, 3, 1, 0)
    Gumps.AddTooltip(gd, r"Forward-Right")
    #row 2
    Gumps.AddButton(gd, 0, 50, 4506, 4506, 4, 1, 0)
    Gumps.AddTooltip(gd, r"Left")
    Gumps.AddButton(gd, 100, 50, 4502, 4502, 6, 1, 0)
    Gumps.AddTooltip(gd, r"Right")    
    #row 3
    Gumps.AddButton(gd, 20, 78, 4505, 4505, 7, 1, 0)
    Gumps.AddTooltip(gd, r"Back-Left")
    Gumps.AddButton(gd, 50, 100, 4504, 4504, 8, 1, 0)
    Gumps.AddTooltip(gd, r"Back")
    Gumps.AddButton(gd, 78, 78, 4503, 4503, 9, 1, 0)
    Gumps.AddTooltip(gd, r"Back-Right")  
    #center
    Gumps.AddImage(gd, 45, 45, 5609) #soraria globe 
    Gumps.AddItem(gd,125,25,0x3B09) #fishy 
    Gumps.AddButton(gd, 60, 40, 2152, 2151, 13, 1, 0)
    Gumps.AddTooltip(gd, r"Serpent Pillars")    
    Gumps.AddButton(gd, 35, 61, 2152, 2151, 10, 1, 0)
    Gumps.AddTooltip(gd, r"Turn-Left")
    Gumps.AddButton(gd, 60, 84, 2152, 2151, 11, 1, 0)
    Gumps.AddTooltip(gd, r"Turn-Around")
    Gumps.AddButton(gd, 85, 61, 2152, 2151, 12, 1, 0)
    Gumps.AddTooltip(gd, r"Turn-Right")
    Gumps.AddButton(gd, 60, 61, 2474, 2473, 5, 1, 0)    
    Gumps.AddTooltip(gd, r"Stop") 
    Gumps.SendGump(987654, Player.Serial, 0, 0, gd.gumpDefinition, gd.gumpStrings)
    buttoncheck()

def buttoncheck():
    Gumps.WaitForGump(987654, 60000)
    Gumps.CloseGump(987654)
    gd = Gumps.GetGumpData(987654)
    if gd.buttonid == 1:
        Player.ChatSay("Forward Left")
    elif gd.buttonid == 2:
        Player.ChatSay("Forward")
    elif gd.buttonid == 3:
        Player.ChatSay("Forward Right")
    elif gd.buttonid == 4:
        Player.ChatSay("Left")
    elif gd.buttonid == 5:
        Player.ChatSay("Stop")
    elif gd.buttonid == 6:
        Player.ChatSay("Right")
    elif gd.buttonid == 7:
        Player.ChatSay("Back Left")
    elif gd.buttonid == 8:
        Player.ChatSay("Back")
    elif gd.buttonid == 9:
        Player.ChatSay("Back Right")
    elif gd.buttonid == 10:
        Player.ChatSay("Turn Left")
    elif gd.buttonid == 11:
        Player.ChatSay("Turn Around")
    elif gd.buttonid == 12:
        Player.ChatSay("Turn Right")
    elif gd.buttonid == 13:
        if Player.Position.X < 5100:
            Player.ChatSay("Doracron")
        else:
            Player.ChatSay("Sueacron") 
    elif gd.buttonid == 20:
        Player.ChatSay("Turn Right")
    Misc.Pause(100)

while True:
    sendgump()