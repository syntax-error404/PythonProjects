from random import randint
import tkinter

###### Madlibs story dogs sentences
dogS1 = "It has often been said that 'a dog is a man's best %s.' Dogs are very %s.and can be taught many %s"
dogS2 = "tricks. A dog can be trained to carry a %s in his mouth. And if you throw his %s, he will run and fetch it. Dogs"
dogS3 = "will also bark %s if someone tries to break into your %s during the night. One of the most popular canine pets"
dogS4 = "today is the %s Spaniel. Spaniels have curly %s coats and %s ears. They also have very %s"
dogS5 = "dispositions and live to be %s years old. Other popular dogs are %s Terriers, German %s, and the"
dogS6 = "%s Poodle. Every home should have a loyal dog for a %s."

adjective = "I need an adjective: "
noun = "I need a noun: "
color = " I need a color: "
number = "I need a number: "
adverb = "I need a adverb: "
pluralnoun = "I need a plural noun: "
celeb = "I need a celebrity"
verb = "I need a verb: "

###### hamlet ##### 


liquid = "I need a type of liquid: "

H_S1 = "This is the soliloquy from the play 'Hamlet,' written by %s. In the third act of this %s play, Hamlet, who is sometimes"

H_S2 = "called 'the melancholy %s,' is suspicious of his stepfatherand hires some actors to act out a scene in which a king is killed"

H_S3 = " when someone pours %s into his %s. First, however, he declaims: To be or not to be: that is the %s: "

H_S4 = "Whether 'tis nobler in the mind to suffer the %s and %s of outrageous fortune, or to take arms against a sea of"

H_S5 = "%s, and by opposing end them. To die: to sleep; no more; and by a sleep to say we end the heartache and the thousand natural"

H_S6 = "%s that flesh is heir to, 'tis a consumation devoutly to be wish'd. To die, to %s; to %s: perchance to"

H_S7 = "%s: ay, there's the %s."

########### Madlib Video Game

part1 = "I need a body part: "
verb_ing = "i need a verb with  ing"

V_S1 = "I love to %s video games. I can play them day and %s! My mom and %s are not too happy with my %s"

V_S2 = "so much time in front of the television %s. Although Dad believes that these %s games help children"

V_S3 = "develop hand-%s coordination and improve their learning %s, he also seems to think they have %s"

V_S4 = "side effects on one's %s. Both of my %s think this is due to a %s use of violence in the majority"

V_S5 = "of the %s. Finally, we all arrived at a %s compromise: After dinner I can play %s hours of video games"

V_S6 = "provided I help clear the %s, and wash the %s"


#####RPS#######
choice = (" Enter a weapon: ")

###### Madlibs Stories ####
story = "What story would you like? 1.Hamlet, 2.Dogs or 3.Video Game:"

#####Keep Play####
another_game = "Would you like to play a different game?"


def battleship():
    board = []

    for x in range(5):
        board.append(["O"] * 5)

    def print_board(board):
        for row in board:
            print " ".join(row)

    print "Let's play Battleship! "
    print_board(board)

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)


    for turn in range(2):
        print "Turn", turn ++ 1

        guess_row = int(raw_input( "Guess Row:" ))
        guess_col = int(raw_input( "Guess Col:"))
        
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean"
            elif board[guess_row][guess_col] == "X" :
                print "You guessed that one already." 
            else:
                print "You missed my battleship!" 
                board[guess_row][guess_col] = "X"
            print_board(board)

        
    print "Game Over, would you like to play again? Yes or No: " 
    playBS = raw_input("" )
    if playBS =="yes":
        battleship()

    else:
        print another_game
        aga = raw_input("")
        aga.lower()
        if aga == "yes":
            main()
        else:
                print "Thanks for playing!"







def RPS():
    print 'Welcome to Rock, Paper, Scissors!'
    choice = raw_input(" Enter a weapon: ")
    choice = choice.lower()
    comp_choice = randint(0, 2)
    choice_num = 10
    if choice == 'rock':
        choice_num = 0
    elif choice == 'scissors':
        choice_num = 1
    elif choice == 'paper':
        choice_num = 2
    else:
        print 'You did not enter Rock, Paper, or Scissors'
    if comp_choice == 0:
        comp_str = "Rock"
    elif comp_choice == 1:
        comp_str = "Scissors"
    elif comp_choice == 2:
        comp_str = "Paper"
    print 'The computer chose %s '%(comp_str)
    if choice_num == 0:
        if comp_choice == 0:
            print 'You have tied!'
        elif comp_choice == 1:
            print 'You have won!'
        elif comp_choice == 2:
            print 'The computer has won!'
    if choice_num == 1:
        if comp_choice == 1:
            print 'You have tied!'
        elif comp_choice == 2:
            print 'You have won!'
        elif comp_choice == 0:
            print 'The computer has won!'
    if choice_num == 2:
        if comp_choice == 2:
            print 'You have tied!'
        elif comp_choice == 0:
            print 'You have won!'
        elif comp_choice == 1:
            print 'The computer has won!'

        print "Game Over, would you like to play again? Yes or No: "
        playRPS = raw_input("")
        if playRPS == "yes":
            RPS()

    else:
        print  another_game
        aga = raw_input("")
        aga.lower()
        if aga == "yes":
            main()
        else:
            print "Thanks for playing!"




def hamlet():
    adj = raw_input(adjective)
    famous = raw_input(celeb)
    
    noun1 = raw_input(noun)
    
    noun2 = raw_input(noun)
    
    noun3 = raw_input(noun)
    
    noun4 = raw_input(noun)
    
    pnoun1 = raw_input(pluralnoun)
    
    pnoun2  = raw_input(pluralnoun)
    
    pnoun3 = raw_input(pluralnoun)
   
    tol = raw_input(liquid)
    verb1 = raw_input(verb)
    verb2  = raw_input(verb)
    verb3 = raw_input(verb)


    print  H_S1%(famous, adj)
    print  H_S2%(noun1)
    print  H_S3%(tol,noun2,noun3)
    print  H_S4%(pnoun1,pnoun2)
    print  H_S5%(pnoun3)
    print  H_S6%(noun4,verb1,verb2)
    print  H_S7%(verb3,noun4)


    playHM_ML = raw_input("Game Over, would you like to play again? Yes or No: ")
    if playHM_ML == "yes":
        ml()

    else:
        print  another_game
        aga = raw_input()
        aga.lower()
        if aga == "yes":
            main()
        else:
            print "Thanks for playing!"


def videogame():
    
    adj1 = raw_input(adjective)
    
    adj2 = raw_input(adjective)
    
    adj3 = raw_input(adjective) 
    
    adj4 = raw_input(adjective)
    
    noun1 = raw_input(noun)
    
    noun2 = raw_input(noun)
    
    noun3 = raw_input(noun)
    
    noun4 = raw_input(noun)
    number1 = raw_input(number)
    pob2 = raw_input(part1)
    pob3 = raw_input(part1)
    
    pnoun1 = raw_input(pluralnoun)
    
    pnoun2 = raw_input(pluralnoun)
    
    pnoun3 = raw_input(pluralnoun)

    pnoun4 = raw_input(pluralnoun)
    verb1 = raw_input(verb)
    verbing = raw_input(verb_ing)

    print  V_S1%(verb1, noun1, noun2, verbing)
    print  V_S2%(noun3, adj1)
    print  V_S3%(pob3, pnoun1, adj2)
    print  V_S4%(pob2, pnoun2, adj3)
    print  V_S5%(pnoun3, adj4, number1)
    print  V_S6%(noun4, pnoun4)

    print  "Game Over, would you like to play again? Yes or No: "
    playVG_ML = raw_input("")
    if playVG_ML == "yes":
        ml()

    else:
        print  another_game
        aga = raw_input("")
        aga.lower()
        if aga == "yes":
            main()
        else:
            print  "Thanks for playing!"
    pass
def dog():
    
    adj1 = raw_input(adjective)
    
    adj2 = raw_input(adjective)
    
    adj3 = raw_input(adjective)
    
    adj4 = raw_input(adjective)
    
    adj5 = raw_input(adjective)
    
    adj6 = raw_input(adjective)
    adv = raw_input(adverb)
    color1 = raw_input(color)
    noun1 = raw_input(noun)
    noun2 = raw_input(noun)
    noun3 = raw_input(noun)
    noun4 = raw_input(noun)
    noun5 = raw_input(noun)
    noun6 = raw_input(noun)
    num = raw_input(number)
    pnoun1 = raw_input(pluralnoun)
    print dogS1%(noun1, adj1, adj2)
    print dogS2%(noun2, noun3)
    print dogS3%(adv, noun4)
    print dogS4%(noun5,color1,adj3,adj4)
    print dogS5%(num, adj5, pnoun1)
    print dogS6%(adj6,noun6)

    print "Game Over, would you like to play again? Yes or No: "
    playD_ML = raw_input("")
    if playD_ML == "yes":
        ml()

    else:
        print another_game
        aga = raw_input("")
        aga.lower()
        if aga == "yes":
            main()
        else:
            print "Thanks for playing!"

    pass


def ml():
    print story
    storyc = raw_input(" ")
    if storyc == "1":
        hamlet()
    if storyc == "2":
        dog()
    if storyc == "3":
        videogame()





def main():
    game = raw_input("Choose a game 1.Battleship 2.Rock Paper Scissors 3.Madlibs: ")
    if game == "1":
        battleship()
    if game == "2":
        RPS()
    if game == "3":
        ml()
        


main()
