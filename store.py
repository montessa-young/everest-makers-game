def store():
    shopping_list=[]
    price_list=[]
    while True:
        print("Shopping List Menu:")
        print("1. Add item")
        print("2. View list")
        print("3. remove item")
        print("4. leave shop")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            print("fire sword 30, grenade,4,bow,25, arrow equals 10, pickaxe, 10,potion to revive health,20,shield with a forcefield power to it,50")
            print("ice trap,10, fire trap,10, water trap,10, lightning trap with poison effect,68, instant death trap when a monster steps on it,100")
            print("pants resistance to cold,10, jacket that can hold 20 guns, 45, shoes that give you more speed, 30, a hat that can shot out fire and lightning,47")
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)
            price_to_add = float(input("Enter the price to add: "))
            price_list.append(price_to_add)
            print(f"'{item_to_add}' added to the list.")
            print(f"'{price_to_add}' added to the list.")
        elif choice ==2:
            print(shopping_list)
        elif choice == 3:
            item_to_remove = input("Enter the item to remove: ")
            shopping_list.remove(item_to_remove)
            item_price_remove=float(input("Enter the price to remove"))
            price_list.remove(item_price_remove)
            print(f"'{item_price_remove}' removed from the list.")
        elif choice == 4:
            print("Exiting shopping list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
