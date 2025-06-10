print("Press1 for sandwich")
print("Press2 for pizza")
print("Press3 for burger")

choice=int(input("Enter your choice: "))

match choice:
    case 1:
        print("You ordered a sandwich")       
        
    case 2:
        print()
        print("||||||||||||||||||||")
        print("Press 1 for a fresh dough pizza")
        print("Press 2 for a thin crust pizza")
        print("Press 3 for a cheese burst pizza")
        print("||||||||||||||||||||")
        print()
        
        pizza_type=int(input("Enter your pizza type: "))

        match pizza_type:
            case 1:
                print("You ordered a fresh dough pizza")
            case 2:
                print("You ordered a thin crust pizza")
            case 3:
                print("You ordered a cheese burst pizza")
            case 4:
                print("Not available......")
    case 3:
        print("You ordered a burger")
    case _:
        print("Invalid Choice....")
        
