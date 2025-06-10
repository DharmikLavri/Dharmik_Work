num1=int(input("Enter value ofnum1: "))
num2=int(input("Enter value ofnum2: "))
num3=int(input("Enter value ofnum3: "))

if num1==num2 and num2==num3:
    print("All Are Same")
elif num1==num2:
    if num1>num3:
        print("num1 and num2 are max")
    else:
        print("num3 is max")
elif num2==num3:
    if num2>num1:
        print("num2 and num3 are max")
    else:
        print("num1 is max")
elif num3==num1:
    if num3>num2:
        print("num3 and num1 are max")
    else:
        print("num2 is max")
elif num1>num2:
    if num1>num3:
        print("num1 is max")
    else:
        print("num3 is max")
elif num2>num3:
    if num2>num3:
        print("num2 is max")
    else:
        print("num3 is max")

