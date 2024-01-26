print("Welcome to BMI calculator")
height=float(input("Enter your height in meters:"))
weight=int(input("Enter your weight in Kilograms:"))
Bmi=weight/(height**2)
print("Your BMI",Bmi)
if(Bmi<18.5):
    print("So,You are Underweight")
elif(Bmi>=18.5 and Bmi<=24.9):
    print("So,You're in Normal weight")
elif(Bmi>=25 and Bmi<=29.9):
    print("So,You're Overweight")
else:
    print("So, You're Obsese")
