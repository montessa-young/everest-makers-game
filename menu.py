while True:
    print("Welcome to Mount Everst climbers")
    print("1. Start climbing but only if your choices are picked")
    print("2. Hear your misson again")
    print("3. Go to the village store")
    print("4. Pick your animal friend")
    print("5. Exit your climb")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        print("You started your epic climb to the peak!!")
    elif choice == 2:
            print("You choose to hear your misson again.")
            print("The mission is to climb and defeat a monster to save the village.")
            print("You will also bring back any goods you find to the village.")
    elif choice == 3:
            print("You chose to go to the village store.")
            print("You have a total of 200 coins to spend right now.")
    elif choice == 4:
            print("You will choose your animal friend to help you during your climb.")
    elif choice == 5:
            print("You abandoned everyone who trusted you.")
            break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")