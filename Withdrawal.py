Available_Balance = int(input("What is your balance? "))
Required_Amount = int(input("What amount you need? "))

Remaining_Balance = Available_Balance - Required_Amount

if Available_Balance >= Required_Amount:
    print("Remaining Balance =", Remaining_Balance)
else:
    print("Insufficient Fund")