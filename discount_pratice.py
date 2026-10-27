Amount_Shopped = int(input("Total amount of Shopping?"))
if Amount_Shopped>= 5000:
    Payable_Amount = Amount_Shopped - 500
else:
    Payable_Amount = Amount_Shopped

print("Amount to Pay =" , Payable_Amount)