#EVAL INT

animalLoreTimerMilliseconds = 1200

# Select what to run Animal Lore on
animalLoreTarget = Target.PromptTarget( 'Select animal to train on' )
Mobiles.Message( animalLoreTarget, 52, 'Selected for animal lore training' )

def TrainAnimalLore():
    '''
    Trains Animal Lore with the selected target
    '''
    global animalLoreTarget

    Timer.Create( 'animalLoreTimer', 1 )
    targetStillExists = Mobiles.FindBySerial( animalLoreTarget )

    while targetStillExists != None and not Player.IsGhost and Player.GetRealSkillValue( 'Evaluating Intelligence' ) < Player.GetSkillCap( 'Evaluating Intelligence' ):
        if Gumps.HasGump(3644314075) == True:
            Gumps.SendAction(3644314075, 0)
            Misc.Pause(100)
            
        if not Timer.Check( 'animalLoreTimer' ):
            Player.UseSkill( 'Evaluating Intelligence' )
            Target.WaitForTarget( 2000 )
            Target.TargetExecute( animalLoreTarget )
            Timer.Create( 'animalLoreTimer', animalLoreTimerMilliseconds )

    if targetStillExists == None:
        Player.HeadMessage( colors[ 'red' ], 'Selected target for animal lore is gone' )
    elif Player.GetRealSkillValue( 'Evaluating Intelligence' ) >= Player.GetSkillCap( 'Evaluating Intelligence' ):
        Player.HeadMessage( colors[ 'green' ], 'Evaluating Intelligence training complete!' )

# Start Training
TrainAnimalLore()