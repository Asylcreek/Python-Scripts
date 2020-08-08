print("Welcome to the Multiplication/Exponent Table App")
print("I will give multiply and raise the power of a given number by 1 all the way to 9\n")

while True:
    try:
        #Get number to work with
        number = float(input("What number would you like to work with? "))
        
        break
    except:
        print("\nPlease enter either an integer or a decimal number\n")

print(f"\nMultiplication Table for {number}\n")
for i in range(1, 10):
    #change i to float
    i = float(i)
    
    #multiply number by i
    multiplication = number * i

    #round multiplication to 2 d.p.
    multiplication = round(multiplication, 2)

    print(f"\t{i} * {number} = {multiplication}")

print(f"\nExponentiation Table for {number}\n")
for i in range(1, 10):    
    #multiply number by i
    exponentiation = number ** i

    #round multiplication to 2 d.p.
    exponentiation = round(exponentiation, 2)

    print(f"\t{number} ** {i} = {exponentiation}")