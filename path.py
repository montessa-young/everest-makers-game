import random
def path():
    while True:
        print("What do you want to do now??")
        print("1: Continue traveling.")
        print("2: Take a break and warm up.")
        print("3: Exit the climb.")

        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            print("You choose to keep moving")
            rin = random.randint(1,10)
            if rin >=8:
                print("A sudden blizzard over takes the mountain side and kills you!!")
                print("You can now restart the climb")
                break
            else:
                print("You contiune on the path unharmed.")

        elif choice == 2:
            print("You choose to start a small camp to ensure your safety.")

        elif choice == 3:
            print("You left the climb and abandoned the quest.")
            break

        else:
            print("Invalid choice please pick a number between (1-3)")
