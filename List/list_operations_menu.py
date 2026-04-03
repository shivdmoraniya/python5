my_list = []

while True:
    print("\n--- List Operations Menu ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View list")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item to add: ")
        my_list.append(item)
        print(f"'{item}' added to the list.")
    elif choice == '2':
        if my_list:
            item = input("Enter item to remove: ")
            try:
                my_list.remove(item)
                print(f"'{item}' removed from the list.")
            except ValueError:
                print(f"'{item}' not found in the list.")
        else:
            print("List is empty. Nothing to remove.")
    elif choice == '3':
        if my_list:
            print("Current List:", my_list)
        else:
            print("List is empty.")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")