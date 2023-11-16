#Boat Navigation
#Utilized Dramoor's spell grid example to create

setX = 0 #x location of gump on screen (if gump up have to click button to move)
setY = 0 # y location of gump on screen (same)

def sendgump(movable=True): #Method to call to send gump. 
    gd = Gumps.CreateGump() #making the gump movable=False (gump not movable) closeable=False(right click does not close gump with button zero)
    Gumps.AddPage(gd, 0); #add page to the gump.
    
    Gumps.AddImage(gd, 35, 35, 1417)
    #Gumps.AddImageTiled(gd, 0, 0, 240, 150, 200) #Add Background (gump, x, y, length, height, gumpid)
    #Gumps.AddAlphaRegion(gd,-0,-0,240,150) #Add See Thru Region (gump, x, y, length, height)

    #row1
    Gumps.AddButton(gd, 15, 15, 4507, 4507, 1, 1, 0)#Add Button (gump, x, y, unpressedid, pressedid, buttonnumber, buttoncalltype, param)
    Gumps.AddTooltip(gd, r"Forward-Left") #Add Tool Tip for hovering over the button above. Gumps.AddButton(gd, 15, 15, 4507, 4507, 1, 1, 0)

    Gumps.AddButton(gd, 50, 0, 4500, 4500, 2, 1, 0)
    Gumps.AddTooltip(gd, r"Forward")
    
    Gumps.AddButton(gd, 83, 15, 4501, 4501, 3, 1, 0)
    Gumps.AddTooltip(gd, r"Forward-Right")

    #row 2
    Gumps.AddButton(gd, 0, 50, 4506, 4506, 4, 1, 0)
    Gumps.AddTooltip(gd, r"Left")
    
    
    Gumps.AddButton(gd, 100, 50, 4502, 4502, 6, 1, 0)
    Gumps.AddTooltip(gd, r"Right")
    
    #row 3
    Gumps.AddButton(gd, 15, 83, 4505, 4505, 7, 1, 0)
    Gumps.AddTooltip(gd, r"Back-Left")
    
    Gumps.AddButton(gd, 50, 100, 4504, 4504, 8, 1, 0)
    Gumps.AddTooltip(gd, r"Back")
    
    Gumps.AddButton(gd, 83, 83, 4503, 4503, 9, 1, 0)
    Gumps.AddTooltip(gd, r"Back-Right")
    

    

    
    Gumps.AddItem(gd,135,40,0x14F3) #boat
    
    Gumps.AddButton(gd, 60, 40, 2152, 2151, 13, 1, 0)
    Gumps.AddTooltip(gd, r"Serpent Pillars")
    
    #center

    
    Gumps.AddButton(gd, 35, 61, 2152, 2151, 10, 1, 0)
    Gumps.AddTooltip(gd, r"Turn-Left")
    
    Gumps.AddButton(gd, 60, 84, 2152, 2151, 11, 1, 0)
    Gumps.AddTooltip(gd, r"Turn-Around")
    
    Gumps.AddButton(gd, 85, 61, 2152, 2151, 12, 1, 0)
    Gumps.AddTooltip(gd, r"Turn-Right")
    
    Gumps.AddButton(gd, 60, 61, 2474, 2473, 5, 1, 0)    
    Gumps.AddTooltip(gd, r"Stop") 

    if Gumps.HasGump(987654):
        Misc.Pause(100)
    else:
        Gumps.SendGump(987654, Player.Serial, setX, setY, gd.gumpDefinition, gd.gumpStrings) #sends gump (gumpid use high to not interfere with in gamegumps and make sure every gump has different id, player serial to get gump, x y location of gump, definition gump information, gumpStrings ) )
    buttoncheck() #once send gump go to check for button presses.
    
def buttoncheck(): #method called to check for a button push.
    Gumps.WaitForGump(987654, 60000) # waiting for gump (gumpid, ms to wait)
    Gumps.CloseGump(987654) #close gump (gumpid)
    gd = Gumps.GetGumpData(987654) #get data from gump (gumpid)
    if gd.buttonid == 1: #if button pressed is buttonid 1.
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
        if Player.Position.X < 5100 and Player.Position.Y < 2300:
            Player.ChatSay("Doracron")
        else:
            Player.ChatSay("Sueacron") 
    elif gd.buttonid == 20:
        Player.ChatSay("Turn Right")
    Misc.Pause(100)

while True: # if program running. Replaces having to loop it and keeps from returning to top if variables that change are set.
    #sendgump()#go to start sendgump method.
    sendgump()
    #Misc.Pause(100) #pause for 750ms