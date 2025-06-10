print("Welcome to the Pattern Generator and Number Analyzer!")
print()

print("Select an option: ")
print("1. Generate a Pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

choice1=int(input("Enter your choice: "))

match choice1:
            case 1:
                a=int(input("Enter the number of rows for the pattern: "))
                print()
                print("Pattern: ")
                for i in range(1,a+1):
                    for j in range(1,i+1):
                        print("*",end=" ")
                    print()

            case 2:
                start=int(input("Enter the start of the range: "))
                last=int(input("Enter the end of the range: "))

                i=start
                while i>=start and i<=last:
                    if i%2==0:
                        print("Number",i,"is","Even")
                    else:
                        print("Number",i,"is","Odd")
                    i+=1

                b=last-start+1
                num=int(b/2*(start+last))
                print("Sum of all numbes from",start,"to",last,"is:",num)

            case 3:
                while choice1==3:
                    print("Exiting the program. Goodbye!")
                    break
                    

            
                
                                
                 
            


