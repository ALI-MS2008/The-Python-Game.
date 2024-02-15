#import random number
import random
#Function for while loop for the whole game
while True:
    #Starting
    print("___________________________________")
    print()
    print("      THE GAME OF PYTHON")
    print("___________________________________")
    print("       By Ali Mustafa")
    print()
    
    #Variables for level 2
    slime = 0
    password = 4321
    
    #Output for level 1
    name = input("What is your name? ")
    print()
    print()
    print("------------------------------------------")
    print("   LEVEL 1: THE THREE TUNNELS")
    print("------------------------------------------")
    print()
    print("You are in a room, in front of you are three doors.In door 1 is a gigantic dragon.")
    print(" In door 2 is a lion who has not eaten in years.Door 3 is full of poisonous cobras")
    print()
    
    #Function for level 1: door choice
    door_choice = input("Type 1, 2, or 3 to choose your door: ")

    if door_choice == "1":
        print("The dragon ate you... GAME OVER")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break  
    elif door_choice == "2":
        print("The lion was dead as it had not eaten in years... YOU PASS TO THE NEXT ROUND")

        #Output for level 2
        print()
        print("-------------------------------------------------")
        print("        LEVEL 2: GUESS THE PASSWORD")
        print("-------------------------------------------------")
        print()
        print("Oh no! The room is filling up with slime balls. Quickly, there is a room in front of you")
        print("What the...the door needs a password first")
        print()
        print("It will take 50 slime balls to fill the room and to kill you")
        print()
        print("Every incorrect password means 10 more slime balls")
        print()
        print("Hope you know the password!")
        print()
        print("--------------------------------------------------")
        print("        WELCOME TO THE ESCAPE DOOR ")
        print("--------------------------------------------------")
        print()
        
        #Function for level 2: Password
        guess = int(input("Please enter the password: "))
        
        #Function If password is incorrect
        while guess != password:
            print()
            print("INCORRECT PASSWORD")
            print()
            slime += 10
            print("There are now", slime, "slimeballs")
            
            if slime > 40:
                print("Noooo! YOU DIED")
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() != 'yes':
                    break  
            
            print()
            print("Password hint: 1234 backwards")
            print()
            guess = int(input("Quick! Enter the password: "))
        
            if guess == password:
                break  
        
        #Function if password is correct
        if guess == password:
            print("WoohHoo! You pass to the last round")
            print()
            print("---------------------------------------------")
            print("      LEVEL 3: GUESS THE NUMBER")
            print("---------------------------------------------")
            print()
            print("Now you have entered a room, in the room is a wizard. To pass the room")
            print("you have to guess the number the wizard is thinking of...the number is")
            print("between 1 and 20")

            #Function for level 3: Guess the number
            number = random.randint(1, 20)
            guess_b = int(input("Take a guess! "))

            #Funtion if the guess is incorrect
            while guess_b != number:
                if guess_b < number:
                    print("Your number is too low...")
                else:
                    print("Your number is too high...")
                guess_b = int(input("Please try again..."))
            
            #Function if the guess is correct
            print("Congratulations you won the last round!")

    #Function for level 2: door choice 3
    elif door_choice == "3":
        print("You've been bitten by the cobras... GAME OVER")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break  

  
