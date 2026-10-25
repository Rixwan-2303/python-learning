Age =int(input("What is your age?"))
Account =input("Do you have an account?").lower()

if Age >= 18 and Account == "yes":
    Access = "Granted"
else:
    Access ="Denied"

print("Access" , Access)