def display_menu():
    print("\n--- Advanced Dictionary Operations ---")
    print("1. Create/Reset Dictionary")
    print("2. Add/Update Item")
    print("3. Delete Item")
    print("4. Get Item (with default)")
    print("5. Show All Items")
    print("6. Merge Dictionaries")
    print("7. Use setdefault()")
    print("8. Use fromkeys()")
    print("9. Exit")
    print("------------------------------------")

def main():
    my_dict = {}
    print("Current Dictionary:", my_dict)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            my_dict = {}
            print("Dictionary reset to empty.")
        elif choice == '2':
            key = input("Enter key to add/update: ")
            value = input("Enter value: ")
            my_dict[key] = value
            print(f"Item '{key}: {value}' added/updated.")
        elif choice == '3':
            key = input("Enter key to delete: ")
            if key in my_dict:
                deleted_value = my_dict.pop(key)
                print(f"Deleted '{key}: {deleted_value}'.")
            else:
                print("Key not found.")
        elif choice == '4':
            key = input("Enter key to get: ")
            default_val = input("Enter default value (if key not found): ")
            value = my_dict.get(key, default_val)
            print(f"Value for '{key}': {value}")
        elif choice == '5':
            if my_dict:
                print("Current Dictionary Items:")
                for k, v in my_dict.items():
                    print(f"  {k}: {v}")
            else:
                print("Dictionary is empty.")
        elif choice == '6':
            try:
                other_dict_str = input("Enter another dictionary as JSON (e.g., {\"a\": 1, \"b\": 2}): ")
                import json
                other_dict = json.loads(other_dict_str)
                if isinstance(other_dict, dict):
                    my_dict.update(other_dict)
                    print("Dictionaries merged.")
                else:
                    print("Invalid dictionary format.")
            except json.JSONDecodeError:
                print("Invalid JSON input.")
        elif choice == '7':
            key = input("Enter key for setdefault(): ")
            default_val = input("Enter default value for setdefault(): ")
            value = my_dict.setdefault(key, default_val)
            print(f"setdefault() returned: {value}. Dictionary updated if key was new.")
        elif choice == '8':
            keys_str = input("Enter comma-separated keys (e.g., 'k1,k2'): ")
            keys = [k.strip() for k in keys_str.split(',') if k.strip()]
            value = input("Enter default value for all keys (optional, press Enter for None): ")
            if value == '':
                new_dict = dict.fromkeys(keys)
            else:
                new_dict = dict.fromkeys(keys, value)
            print("New dictionary created using fromkeys():", new_dict)
            print("This new dictionary is not merged with the current one.")
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        print("Current Dictionary:", my_dict)

if __name__ == "__main__":
    main()