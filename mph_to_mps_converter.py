print("Welcome to the MPH to MPS Conversion App\n")
print("I would convert miles per hour to meters per second and correct to 2 decimal places\n")

# continue looping until the code does not error out
while True:
    # if no error
    try:
        speed_in_mph = float(
            input("What is your speed in miles per hour? "))  # Get user input

        speed_in_mps = speed_in_mph * 0.447  # convert that input to mps
        speed_in_mps = round(speed_in_mps, 2)  # round the number to 2 d.p.

        print(f"\nYour speed in meters per second is {speed_in_mps}")

        break
    # if there is an error
    except:
        print("\nPlease only enter integers or decimals\n")
