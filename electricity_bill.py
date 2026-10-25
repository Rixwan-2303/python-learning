Units_consumed =int(input("How many units consumed?"))
Basic_bill = Units_consumed*20
if Units_consumed>300:
    Final_Bill = Basic_bill + 500
else:
    Final_Bill = Basic_bill

print(Final_Bill)