print("Welcome to the Temperature Conversion Program")
print("I will convert degree Fahrenheit to degree Celsius and Kelvin and also round to 4 decimal places")

while True:
    try:
        #Get temperature from user
        temp_in_fahrenheit = float(input("\nWhat is the given temperature in degrees Fahrenheit? "))

        break
    except:
        print('\nPlease enter only integers or decimal numbers\n')


#convert temperature to celsius and kelvin
temp_in_celsius = (temp_in_fahrenheit - 32) * 5/9
temp_in_kelvin = temp_in_celsius + 273.15

#round all the temperatures to 4 d.p
temp_in_fahrenheit = round(temp_in_fahrenheit, 4)
temp_in_celsius = round(temp_in_celsius, 4)
temp_in_kelvin = round(temp_in_kelvin, 4)

#print the results
print(f"\nDegrees Fahrenheit:\t {temp_in_fahrenheit}")
print(f"Degrees Celsius: \t {temp_in_celsius}")
print(f"Degrees Kelvin: \t {temp_in_kelvin}")