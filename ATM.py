import time

print("Please Insert Your CARD")
time.sleep(5)
password=6592
pin=int(input("Enter Your ATM pin "))

balance=5000

if pin==password:
    while True:
        
        print("""
                1.Balance
                2.Withdraw Balance
                3.Deposit Balance
                4.Exit
                """)
        try:
            option=int(input("Please enter your choice"))
        except:
            print("Please enter valid option")
            
        if option==1:
            print(f"Your current balance is {balance}")
            
        if option==2:
            withdraw_amount=int(input("Please enter withdraw amount"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your updated balance is {balance}")
            
        if option==3:
            deposit_amount=int(input("Please enter deposit amount"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")

        if option==4:
            break  
            
else:
    print("Wrong Pin! Please try again!")