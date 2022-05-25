from os import system, name


actorPosition = 0
actorShape = '#'

while(True):
    #IF, else branching to clear the screen and update the actor location in the screen
    #System command to clear the terminal based on nt (windows) or unix (mac, ubuntu, debian, redhat etc)
    if( name == 'nt'):
        system('cls')
    else:
        system('clear')

    #Print * to denote a row of tree tops for 50 times
    print('*'*50)
    
    #Print * to denote a row of tree tops for 50 times
    print('*'*50)

    #Print * to denote a row of tree tops for 50 times
    print('*'*50)

    #Print * to denote a row of tree tops for 50 times
    print('*'*50)
    #Print \n to denote rows of empty space for 1 times
    print('\n')

    #actorPosition is along the horizontal direction
    #Print space characters based on how much the actor has moved and then print the actorShape
    print(' '*actorPosition, actorShape)

    #Print \n to denote rows of empty space for 2 times
    print('\n'*2)

    #Print * to denote a row of tree tops for 50 times
    print('*'*50)
    #Print * to denote a row of tree tops for 50 times
    print('*'*50)
    #Print * to denote a row of tree tops for 50 times
    print('*'*50)
    #Print * to denote a row of tree tops for 50 times
    print('*'*50)
    direction = int(input('Which direction you want to go? (1) Right, (-1) Left : '))
    actorPosition += direction

    if(actorPosition > 48):
        print('\n'*4)
        print('='*50)
        print('Hurray you left the forest')
        print('='*50)
        print('\n'*4)
        break
