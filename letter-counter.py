print("Welcome to the Letter Counter App\n") #Welcome Message

name = input("What is your name? ").title().strip() #Get player name

#Greeting
print(f"\nHello {name}!! I will count the number of times that a specific letter (or number) occurs in a message.")

#Get message from user and convert to lower case
print('')
message = input("Please enter a message: ").lower()

#function to count the letters
def count_letters(message):
    #get letter to count from user and convert to lower case
    letter = input("\nWhich letter would you like to count the occurrences of? ").lower() #collect letter to count
    count = message.count(letter) #count letter

    #check if count is greater than 1 to print the proper response
    if count > 1:
        print(f"\n{name}, your message has {count} {letter}'s in it")
    else:
        print(f"\n{name}, your message has {count} {letter} in it")
    
count_letters(message) #call count_letters

response = input("\nWanna try again (Y/N)? ").lower() #ask if player wants to have another go

while response == 'y':
    new_message_response = input("\nWith a new message (Y/N)? ").lower() #ask if player wants to try with a new message

    if new_message_response == 'y':
        message = input("\nPlease enter a message: ").lower() #if player wants a new message

    count_letters(message)

    response = input("\nWanna try again (Y/N)? ").lower()

print("\nThank you for using!!")