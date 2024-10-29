height=float(input("Enter height: "))
weight=float(input("Enter weight: "))

bmi=weight/(height/100)**2
print(f'Your BMI is {bmi}')
if bmi<=18:
    print("You are under weight")
elif bmi<=30:
    print("You are fine.")
elif bmi<=40:
    print("You are over weight")
elif bmi<=45:
    print("Consult a doctor")
else:
    print('You are healthy and fine..')
