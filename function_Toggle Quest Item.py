#Toggle Quest Items
Misc.WaitForContext(0x00051472, 10000)
Misc.ContextReply(0x00051472, 7)
Target.WaitForTarget(10000, False)
amount = 0

crap = ([0x0B5E])
filter = Items.Filter()
filter.Enabled = True
filter.OnGround = False    
#filter.Hue = 0
itemfilter = Items.ApplyFilter(filter)
for item in Player.Backpack.Contains:
    if item.ItemID in crap:
        if item.Hue == 0:
            if amount < 10:
                amount += 1
                Player.ChatSay(str(amount))
                Target.TargetExecute(item)
                Misc.Pause(300)
                
Target.Cancel()              
Mobiles.UseMobile(0x0005FBA2)
Gumps.WaitForGump(1280077232, 10000)
Gumps.SendAction(1280077232, 8)
Gumps.WaitForGump(1280077232, 10000)
Gumps.SendAction(1280077232, 5)