import re

def coords(ydeg, ymin, ydir, xdeg, xmin, xdir):
    ydeg, ymin, xdeg, xmin = map(int, [ydeg, ymin, xdeg, xmin])
    if xdir == 'W': xdeg = -xdeg
    if ydir == 'N': ydeg = -ydeg
    x = (((xdeg * 5120) + (xmin * 60)) / 360) + 1323
    y = (((ydeg * 4096) + (ymin * 60)) / 360) + 1624
    if x < 0: x += 5120
    elif x > 5120: x -= 5120
    if y < 0: y -= 4096
    elif y > 4096: y -= 4096
    return round(x), round(y)

if Gumps.CurrentGump() == 1426736667:
    raw = Gumps.LastGumpRawData()
    pattern = re.compile(r"@(\d+)o (\d+)'(N|S), (\d+)o (\d+)'(E|W)@")
    matches = re.search(pattern, raw)
    if len(matches.groups()) == 6:
        x, y = coords(*matches.groups())
        Player.HeadMessage(1150, f'SOS @ {x}, {y}')