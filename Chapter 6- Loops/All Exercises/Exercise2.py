#while command to start infinite loop
while True:
    age = input("Please enter your age (or 'leave' to exit): ")
#if user types 'leave' the loop will end
#the .lower let the user type 'leave' in upper case, basically not case-sensitive 
    if age.lower() == 'leave':
        print("Thank you for using the ticket service. See yaaa!")
        break
#converting age to integer
    age = int(age)
#if and elif statments for diffrent ages, will print diffrent messages for diffrent ages
    if age < 3:
        print("Your Ticket is free.")
    elif 3 <= age <= 12:
        print("Your Ticket will cost $10.")
    else:
        print("Your Ticket will cost $15.")
