def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        match (choice):
            case "1":
                item = str(input("Enter the item to add: "))
                shopping_list.append(item)
            
            case "2":
                item = str(input("please pick an item to remove: "))
                try:
                    shopping_list.remove(item)
                except:
                    print("the item in not in the list.")
            case "3":
                for item in shopping_list:
                    print(item)
            case "4":
                break
            case _:
                print("Invalid choice. Please try again.")

main()

