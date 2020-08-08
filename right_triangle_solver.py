#Import math for the squareroot method
import math

print("Welcome to the Right Triangle Solver App")
print("I will provide the hypotenuse and area of any given opposite and adjacent sides\n")

while True:
    try:
        #Collect input from user
        first_leg = float(input("Enter the value for the first leg of the triangle: "))
        second_leg = float(input("Enter the value for the second leg of the triangle: "))
        
        break
    except:
        print("\nPlease enter an integer or a decimal number")

#Calculate the hypotenuse
hypotenuse = math.sqrt((first_leg ** 2) + (second_leg ** 2))
hypotenuse = round(hypotenuse, 3)

#Calculate the area
triangle_area = (first_leg * second_leg) / 2
triangle_area = round(triangle_area, 3)

#Print the results
print(f"\nFor a triangle with legs {first_leg} and {second_leg}, the hypotenuse is {hypotenuse}")
print(f"For a triangle with legs {first_leg} and {second_leg}, the area is {triangle_area}")