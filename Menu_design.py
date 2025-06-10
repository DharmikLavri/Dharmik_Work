print("Press1 for English")
print("Press2 for Gujarati")
print("Press3 for Hindi")

language=int(input("Enter your choice: "))

match language:
    case 1:
        print("Press 1 for recharge of 1gb")
        print("Press 2 for recharge of 5gb")
        print("Press 3 for recharge of 10gb")

        recharge_data1=int(input("Enter Your Recharge Pack: "))

        match recharge_data1:
            case 1:
                print("Thank u for choosing 1gb data")
            case 2:
                print("Thank u for choosing 5gb data")
            case 3:
                print("Thank u for choosing 1gb data")

    case 2:
        print("1gb nu recharge karava mate 1 dabavo")
        print("5gb nu recharge karava mate 2 dabavo")
        print("10gb nu recharge karava mate 3 dabavo")

        recharge_data2=int(input("Enter Your Recharge Pack: "))

        match recharge_data2:
            case 1:
                print("Thank u for choosing 1gb data")
            case 2:
                print("Thank u for choosing 5gb data")
            case 3:
                print("Thank u for choosing 1gb data")
            
    
    case 3:
        print("1gb ka recharge karne ke liye 1 daboo")
        print("5gb ka recharge karne ke liye 1 daboo")
        print("10gb ka recharge karne ke liye 1 daboo")

        recharge_type3=int(input("Enter Your Recharge Pack: "))

        match recharge_data3:
            case 1:
                print("Thank u for choosing 1gb data")
            case 2:
                print("Thank u for choosing 5gb data")
            case 3: 
                print("Thank u for choosing 1gb data")

    case _:
        print("Invalid Choice")
       
                
        

    
