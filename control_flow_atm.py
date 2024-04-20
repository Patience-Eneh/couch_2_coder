balance= int(55000)
pin= 1234 

pin_prompt = int(input("Please, enter your pin"))

#if pin matches
if pin_prompt == pin:
    print(f"your account balance is £{balance}")
 
 #transactions:
 
    transaction = input("would you like to withdraw or deposit?")
    if transaction == "withdraw":
        amount = float(input("enter an amount: "))
        if amount <= balance:
            new_balance = balance - amount
            print(f"transaction successful. new balance: £{new_balance}")
        else:
            print("insufficient funds.")

    elif transaction == "deposit":
        amount = float(input("Enter deposit amount"))
        new_balance = balance + amount
        print(f"Deposit has been successful. Your New balance is £{new_balance}")
    else:
        print("invalid transaction")

else:
    print("wrong pin. please try again.") 