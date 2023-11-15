# Taking user input for amount_one and amount_two
amount_one = float(input("Enter the value for amount_one: "))
amount_two = float(input("Enter the value for amount_two: "))

# Nested decision structure to check conditions and display the greater of amount_one and amount_two
if amount_one > 10:
    if amount_two < 100:
        if amount_one > amount_two:
            #above if statments check all conditions
            print(f"The greater of amount_one and amount_two is: {amount_one}")
            #below else statments prints diffrent outputs for diffrent scenarios
        else:
            print(f"The greater of amount_one and amount_two is: {amount_two}")
    else:
        print("amount_two is not less than 100.")
else:
    print("amount_one is not greater than 10.")

