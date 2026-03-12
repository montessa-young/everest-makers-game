while True:
    print("Welcome to Mount Everst climbers")
    print("1. Start climbing but only if your choices are picked")
    print("2. Hear your misson again")
    print("3. Change your equiment")
    print("4. Exit your climb")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        print("You started your epic climb to the peak!!")
    elif choice == 2:
            print("You chose to climb the mountain")
            print("The mission is to climb and defeat a monster to save the village")
            print("You will also bring back any goods you find to the village")
    elif choice == 3:
            print("You chose to go to the village store")
    elif choice == 4:
            print("Exiting your climb.")
            break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")