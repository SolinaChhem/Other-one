# 2. question
shopping_list = []
while True:
    print("-" *20)
    print("'q' => Quit the program")
    print("'1' => Add")
    print("'2' => Delete")
    print("'3' => Display")
    print("-" * 20)
    user_input = input("Enter opton: ")

    if user_input == "q":
        print("Bye Bye")
        break

    #elif user_input == "1":
        #print("-" *20)
        #print("Type something you want to add: ")
        #print("-" *20)
    #elif user_input == "2":
        #print("-" *20)
        #print("Type something you want to delete: ")
        #print("-" *20)
    #elif user_input == "3":
        #print("-" *20)
        # print("Type something you want to display: ")
        # print("-" *20)

    elif user_input == "1":
        new_item = input("New ITEM: ")
        shopping_list.append(new_item)

    elif user_input == "2":
        remove_item = input("Item to remove: ")
        shopping_list.remove(remove_item)

    elif user_input == "3":
        for item in shopping_list:
            print(item)
    