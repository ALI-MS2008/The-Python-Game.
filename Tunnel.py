import random

while True:
    print("___________________________________")
    print()
    print("      THE GAME OF PYTHON")
    print("___________________________________")
    print("       By Ali Mustafa")
    print()

    slime = 0
    password = 4321

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

    door_choice = input("Type 1, 2, or 3 to choose your door: ")

    if door_choice == "1":
        print("The dragon ate you... GAME OVER")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break  
    elif door_choice == "2":
        print("The lion was dead as it had not eaten in years... YOU PASS TO THE NEXT ROUND")
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
        guess = int(input("Please enter the password: "))
        
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

            number = random.randint(1, 20)
            guess_b = int(input("Take a guess! "))

            while guess_b != number:
                if guess_b < number:
                    print("Your number is too low...")
                else:
                    print("Your number is too high...")
                guess_b = int(input("Please try again..."))

            print("Congratulations you won the last round!")

    elif door_choice == "3":
        print("You've been bitten by the cobras... GAME OVER")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break  

  
    
    
               
   
