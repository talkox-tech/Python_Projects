def showmenu():
    print("\n---Shopping List Main Menu")
    print("1. View the Shopping list")
    print("2. Add the item in the Shopping list")
    print("3. Remove the Shopping list")
    print("4. clear the Shopping list")
    print("5. Exit")
showmenu()
shopping_list=[]
while True:
    choice = input("Enter the value from 1-5 for your desired Operation: ")
    if choice == "1":
        if not shopping_list:
            print("Your Shopping List is empty.")
            showmenu()
        else:
            print("\n")
            for index, item in enumerate(shopping_list):
                print(f"{index+1}. {item}")
            showmenu()
    elif choice == "2":
        numofItem = int(input("Number of Item: "))
        for i in range(1,numofItem+1):
            item = input(f"Enter the {i} item name: ")
            shopping_list.append(item)
        print(f"{numofItem} item added successfully in your shoping list")    
        showmenu()
    elif choice == "3":
        removeChoice = int(input("\nRemove the item by: \n\t 1.By item name \n\t 2.By index number \n Enter the option: "))
        if removeChoice == 1:
            removeItem = input("Enter the item name to remove from the list: ")
            shopping_list.remove(removeItem)
            showmenu()
        else:
            removeIndex = int(input("Enter the index number of the item to remove from the list: "))
            shopping_list.pop(removeIndex-1)
            showmenu()
    elif choice == "4":
        shopping_list.clear()
        showmenu()
    elif choice == "5":
        print("See you !! Happy Shopping  ")
        break
    else:
        print("Invalid Choice. Please try again with right choice")
        showmenu()


