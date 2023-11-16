from Scripts.utilities.items import FindItem, MoveItem
WOOD_LOGS = 0x1BDD
AXE_SERIAL = 0x403BE10A
beetle = 0x0018DF40

# Determine your weight carrying capacity, and set thresholds relative to it.
max_weight = Player.MaxWeight
start_chopping_logs_weight = 400
stop_chopping_trees_weight = max_weight - 2

# Equip your axe if not already equipped.
axe_serial = Player.GetItemOnLayer('LeftHand')
if not axe_serial:
    Misc.SendMessage('No axe found!')
    axe_serial = AXE_SERIAL
    Player.EquipItem(axe_serial)
    Misc.Pause(600)

# Chop trees as you run up against them, until you're too heavy.
while True:
    
    Journal.Clear()
    Target.TargetResource(axe_serial,"wood")
    Misc.Pause(200)
    
    # If getting heavy, chop up the logs.
    if Player.Weight >= start_chopping_logs_weight:
        Misc.SendMessage("Heavy, chop logs....")

        log = Items.FindByID(WOOD_LOGS, -1, Player.Backpack.Serial) 
        while log != None:
            Items.UseItem(axe_serial)
            Target.WaitForTarget(5000, False)
            Target.TargetExecute(log)
            Misc.Pause(1000)
            log = Items.FindByID(WOOD_LOGS, -1, Player.Backpack.Serial)
    if Player.Weight > 400:
        crap = ([0x318F,0x3191,0x1BD7,0x3190,0x3199,0x2F5F])
        filter = Items.Filter()
        filter.Enabled = True
        filter.OnGround = False    
        itemfilter = Items.ApplyFilter(filter)
        for item in Player.Backpack.Contains:
            if item.ItemID in crap:
                MoveItem(Items,Misc,item,beetle)
            
    # Stop chopping trees when we can't carry more.
    if Player.Weight >= stop_chopping_trees_weight:
        Misc.SendMessage("Too heavy....  Stop")
        break