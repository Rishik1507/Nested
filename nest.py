num=int(input("Enter Number: "))
if num>50:
    print(f'{num} is greater than 50')
    if num%2==0:
        print("It is even")
    else:
        print("It is odd")

else:
    print(f'{num} is less than 50')