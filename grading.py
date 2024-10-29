#ifelse
#Create a program that checks a student performance
from colorsys import yiq_to_rgb

marks=int(input("Enter the number of marks: "))

if marks <= 100 and marks >= 80:
    print("You have grade A")
elif marks <= 79 and marks >= 60:
    print(" You have grade B")
elif marks <= 59 and marks >= 40:
    print(" You have grade C")
elif marks <= 39 and marks >= 0:
    print("You failed")
else:
    print("Invalid Input")


#Create a program to calculate the Body Mass Index BMI
# BMI Calculator

# Taking user input for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

# Calculating BMI
bmi = weight / (height ** 2)

# Displaying the BMI result
print(f"Your BMI is: {bmi:.2f}")

# BMI Categorization using if-else statements
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")



