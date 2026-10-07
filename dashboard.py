balance = 5000
print('=====ATM=====')
print("1. Check balance")
print("2. Withdraw money")
print("3. Deposit money")
print("4. Exit")

choice = int(input('choose an option: '))  #user enters a number to kick off the program
if choice == 1:
    print(f'Your remaining balance is {balance}') 
#shows the balance of the user

elif choice == 2:
    withdrawal = int(input('Enter your withdrawal amount: ')) 
    if withdrawal <= 5000: 
        print('Withdrawal Succesful')
        balance = balance - withdrawal
        print(f'Your remaining balance is ${balance}')
    else:
        print('Enter a valid amount')
        print(f'Your remaining balance is ${balance}')
# it works the user on the withdrawal process here

elif choice == 3:
    deposit = int(input('Enter any amount: '))
    if deposit >= 0:
        print('Deposit Succesful')
        deposit = deposit + balance 
        print(f'Your new balance is ${deposit}')
    else:
        print('Enter a valid amount.')
        print(f'Your remaining balance is ${balance}')
# it works the user on the deposit process here

elif choice ==4:
    print('You have exited the program succesfully.')
    #the user succesfullty exits the code right here
