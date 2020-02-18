def transaction(x): #creates function transaction
    if x==1:
        print('Your available balance is $'+str('{:.2f}'.format(float(username[2]))))  #prints user's balance
        menu=eval(input('''
Menu:
Press 1 to view your balance
Press 2 to withdraw
Press 3 to deposit
Press 4 to quit

''')) #presents transaction options to user
        transaction(menu) #restarts transaction function
    elif x==2:
        withdraw() #executes withdraw function
        menu=eval(input('''
Menu:
Press 1 to view your balance
Press 2 to withdraw
Press 3 to deposit
Press 4 to quit

''')) #presents transaction options to user
        transaction(menu) #restarts transaction function
    elif x==3:
        deposit() #executes deposit function
        menu=eval(input('''
Menu:
Press 1 to view your balance
Press 2 to withdraw
Press 3 to deposit
Press 4 to quit

''')) #presents transaction options to user
        transaction(menu) #restarts transaction function
    elif x==4:
        infile=open('accounts.txt', 'w') #opens accounts.txt in writing mode
        text='' #creates string text
        for k in users:
            text=users.get(k) #assigns text to the list of values for each key in dictionary users
            text=str(text[0])+' '+str(text[1])+' '+str(text[2]) #formats the text in the desired manner for writing to file
            infile.write(str(k)+' '+str(text)+'\n') #writes the key and value in string format to the file
        infile.close() #closes accounts.txt
        print('Your session has ended.') #notifies user that they have successfully quit the application
        quit #quits application
    else:
        x=eval(input(menu)) #reprompts menu options

def deposit(): #creates function deposit
    while True:
        try:
            amount=eval(input('Please enter the amount to deposit: ')) #asks user for their deposit amount
            total=float(username[2])+float(amount) #adds deposit amount to previous balance
            username[2]=total #replaces old balance with new balance
            total=str('{:.2f}'.format(total)) #formats the balance to the form of a float with 2 decimal points
            print('Your deposit has been completed successfully.') #notifies user that their deposit was successfully processed
            return(total) #returns the new balance
        except:
            print('Your entry was not valid.') #lets the user know that their entry was invalid
    
    
def withdraw(): #creates function withdraw
    while True:
        try:
            takeout=eval(input('Please enter the amount to withdraw: ')) #asks user for the amount to withdraw
            if float(takeout) <= float(username[2]): #checks to ensure withdraw amount is not greater than the amount in the account
                total=float(username[2])-float(takeout) #subtracts withdraw amount from previous balance
                username[2]=total #replaces old balance with new balance
                total=str('{:.2f}'.format(total)) #formats the balance
                print('Your withdrawal has been completed successfully.') #notifies user that their transaction was completed successfully
                return(total) #returns the new balance
            else:
                print('Your account has insufficient funds for requested withdrawal amount. Please enter a lower amount.') #alerts the user that their requested withdraw amount was too large   
        except:
            print('Your entry was not valid.') #lets the user know that their entry was invalid
    

try:
    infile=open('accounts.txt', 'r') #opens accounts.txt in reading mode
except IOError:
    print('This application is experiencing technical difficulties.  Your session has been terminated.') #notifies user that an error occurred
    quit #quits the application
content=infile.readlines() #reads each line of the file
users={} #creates empty dictionary users
try:
    for line in content:
        items=line.split() #splits each line of the file into a list of words
        key=eval(items[0]) #assigns key to the first word of the line
        users[key]=list(items[1:4]) #assigns the remaining words of the line as the value in the form of a list
except:
    pass
infile.close() #closes the file
pin=eval(input('Please enter your 4 digit code: ')) #asks user for their code
try:
    if pin in users.keys(): #determines if the code corresponds to an account
        global username #assigns username as a global variable
        username=users.get(pin) #assigns username to the values that correspond to the entered code
        print('\nHello ' + str(username[0]) + ' ' + str(username[1])) #greets the user by name
        global menu #assigns menu as a global variable
        menu=eval(input('''
Menu:
Press 1 to view your balance
Press 2 to withdraw
Press 3 to deposit
Press 4 to quit

''')) #presents user with a menu of transaction options
        global total #assigns total as a global variable
        transaction(menu) #executes function transaction with the input of menu
    else:
        print('The code that you entered cannot be found.  Your session has been terminated.') #alerts the user that the code entered was not found
        quit #quits the application
except:
    print('The code that you entered cannot be found.  Your session has been terminated.') #alerts the user that the code entered was not found
    quit #quits the application

