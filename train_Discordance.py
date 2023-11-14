from AutoComplete import *
from System import Byte
from System.Collections.Generic import List

instruments = [0x2805, 0x0E9C, 0x0EB3, 0x0EB2, 0x0EB1, 0x0E9E, 0x0E9D]


def get_enemies(max_range=12):
    enemy_filter = Mobiles.Filter()
    enemy_filter.RangeMax = max_range
    enemy_filter.Notorieties = List[Byte](bytes([3, 4, 5, 6]))
    enemy_filter.CheckIgnoreObject = True
    enemy_filter.Friend = False
    enemies = Mobiles.ApplyFilter(enemy_filter)
    return enemies


def main():
    while not Player.IsGhost:
        Misc.SendMessage('Searching for new mobiles around you', 1195)
        found_mobiles_around_you = get_enemies(8)
        Misc.Pause(1000)

        for mob in found_mobiles_around_you:
            Journal.Clear()
            Target.Cancel()

            while not Journal.Search('suppressing your target') and not Journal.Search('That creature is already in discord.') and not Journal.Search('That is too far away.'):
                Journal.Clear()
                Misc.SendMessage(f'Trying to discord creature: {hex(mob.Serial)}', 52)
                Player.UseSkill('Discordance')
                Misc.Pause(200)
                if Journal.Search('What instrument shall you play?'):
                    instrument = next(
                        filter(lambda x: x.ItemID in instruments, Player.Backpack.Contains), None)
                    if not instrument:
                        Target.Cancel()
                        Misc.SendMessage('Ran out of instruments to train with', 33)
                        return

                    Target.WaitForTarget(2000)
                    Target.TargetExecute(instrument)

                Target.WaitForTarget(2000)
                Target.TargetExecute(mob)
                Misc.Pause(1000)

                if Journal.Search('no effect on that.'):
                    break

            if Journal.Search('suppressing your target'):
                Misc.Pause(8000)
            elif Journal.Search('That is too far away.'):
                continue

        while not Player.IsGhost:
            Player.UseSkill('Hiding')
            Misc.Pause(500)
            if Journal.Search('You fail to hide.'):
                Journal.Clear('You fail to hide.')
                Misc.Pause(10000)
            elif Journal.Search('hidden yourself well.'):
                Misc.SendMessage('Waiting for 20sec. hidden to reset discorded animals.', 52)
                Misc.Pause(20000)
                break


if __name__ == '__main__':
    main()