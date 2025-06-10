num1=int(input("Enter value of num1: "))
num2=int(input("Enter value of num2: "))
num3=int(input("Enter value of num3: "))
num4=int(input("Enter value of num4: "))

if num1==num2 and num2==num3 and num3==num4:
    print("All are same")
elif num1>num2:
    if num1>num3:
        print("num1 is max")
    else:
        print("num3 is max")
elif num2>num3:
    if num2>num4:
        print("num2 is max")
    else:
        print("num4 is max")
elif num3>num4:
    if num4>num1:
        print("num4 is max")
    else:
        print("num1 is max")
elif num1==num2 and num2==num4:
    if num1>num3 and num2>num3:
        print("num1 and num2 are max")
    else:
        print("num3 is max")
elif num2==num3:
    if num2>num4:
        print("num2 and num3 are max")
    else:
        print("num4 is max")
elif num3==num4:
    if num3>num1:
        print("num3 and num4 are max")
    else:
        print("num1 is max")
elif num4==num1:
    if num4>num2:
        print("num4 and num1 are max")
    else:
        print("num2 is max")
        

