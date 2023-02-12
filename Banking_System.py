## A PRIMITIVE BANKING SYSTEM WITH DIFFERENT WALLETS BY TARUN GARG ## 

# CLASS THAT HANDLES ACCOUNT CREATION

class Customer_account():

# DEFINING THE VARIABLES NEEDED FOR ACCOUNT CREATION  
    def __init__(self , f_name,l_name,cor,age,email,password,username):
        self.f_name = f_name
        self.l_name = l_name
        self.cor = cor
        self.age = age
        self.email = email
        self.password = password
        self.username = username

# FUNCTION THAT HANDLES CREATING A NEW ACCOUNT 
    def data(self,c_data):
        c_data[self.username] = {'f_name' : self.f_name ,
                                'l_name' : self.l_name,
                                'COR' : self.cor,
                                'age' : self.age,
                                'email' : self.email,
                                'password' : self.password}
        return (c_data)

# CLASS THAT HAS VARIOUS HELPER FUNCTIONS WHICH ARE USED MULTIPLE TIMES 
    
class Banking_system():

# DEFINING VARIABLES 
    def __init__(self , username ) :
        self.username = username
        
# FUNCTION THAT CHECKS RETURNS THE WALLET POSITION AS AN INTEGER FOR DIFFERENT FEATURES (ADD,WITHDRAW,ETC)
# AND CHECKS IF THAT POSTION IS THERE IN THE WALLET 
    def wallet_position(self,text):
        while True:
            while True:
                try:
                    wallet_pos = int(input(text))-1
                    break
                except:
                    print('\nERROR : INTERGER INPUT ONLY')
            
            if wallet_pos == -1:
                return(wallet_pos)
            if (wallet_pos not in range(len(wallet[self.username]))):
                print('\nPOSITION NOT IN WALLET')
                continue
            else:
                return(wallet_pos)

# FUNCTION THAT RETURNS THE AMOUNT AS INTEGER FOR DIFFERENT FEATURES (ADD,WITHDRAW,ETC)
# AND CHECKS THAT THE AMOUNT > 0  

    def amount(self,text):
        
        while True : 
            try :
                amt = (float(input(text)))
            except:
                print('\nERROR : INTERGER INPUT ONLY')
            
            if amt < 0 :
                print('ERROR : AMOUNT CAN NOT BE NEGATIVE OR ZERO ')
            else :
                return(amt)
       
# FUNCTION THAT CHECK IF USER HAS WALLET TO USE A FEATURE

    def check_wallets(self,wallet):

        if self.username in list(wallet.keys()):
            return(True)
        else:
            print('\nERROR : YOU DO NOT HAVE ANY WALLET, CREATE ONE TO USE THIS FEATURE')

# CLASS THAT HANDLES DIFFERENT WALLET FEATURES (CREATE,ADD,ETC.)
# INHERITANCE IS USED SO THAT Banking_system FUNCTIONS CAN BE USED 

class Wallet(Banking_system):
 
# DEFINING VARIABLES  
    
    def __init__(self,username):
        self.username = username

# FUNCTION TO PRINT WALLET OF THE USER 

    def print_wallet(self,wallet) : 
        print('---------------------------------------------------')
        print('Mr/Mrs '+ self.username.upper() + ' CURRENT WALLET : \n\n ',wallet.get(self.username))
        print('---------------------------------------------------')

# FUNCTION TO CREATE WALLET FOR THE USER 

    def create_wallet(self,wallet):
 
        while True:
            print('\nWALLET TYPE- \nD : DAILY USE  \nS : SAVINGS \nH : HOLIDAYS  \nM : MORTGAGE  \nB : BACK')
            wallet_type = input('WHAT WOULD YOU LIKE TO DO ? ') 
            
            if ((wallet_type == 'D') or (wallet_type == 'd')):
                wallet_type_ = 'DAILY USE'
                break
                
            elif ((wallet_type == 'S') or (wallet_type == 's')):
                wallet_type_ = 'SAVINGS'
                break
                
            elif ((wallet_type == 'H') or (wallet_type == 'h')):
                wallet_type_ = 'HOLIDAYS'
                break
                
            elif ((wallet_type == 'M') or (wallet_type == 'm')):
                wallet_type_ = 'MORTGAGE'
                break
            
            elif ((wallet_type == 'B') or (wallet_type == 'b')):
                return(False)
                
            else:
                print('ERROR : INVALID INPUT, TRY AGAIN')
                continue
        while True :        
            try:                        
                amount = int(input('ENTER AMOUNT : ' ))
                break
            except:
                print('INTERGER INPUT ONLY ALLOWED')

        
        if self.username not in list(wallet.keys()):
            wallet[self.username] = {'1) ' + wallet_type_ : amount}
        else:
            wallet[self.username][str(len(wallet[self.username])+1)+') ' + wallet_type_] = amount

#FUNCTION TO DELETE WALLET 

    def del_wallet(self,wallet,wallet_type,wallet_transfer):

        keys = list(wallet[self.username].keys())
        wallet[self.username][keys[wallet_transfer]] += wallet[self.username][keys[wallet_type]]
        del wallet[self.username][keys[wallet_type]]

        dict_dummy = {}
        pos = 1
        for i in list(wallet[self.username].keys()):
            dict_dummy[str(pos)+') '+i[3:]] =  wallet[self.username][i]
            pos +=1
        wallet[self.username] = dict_dummy

# FUNCTION TO ADD FUNDS IN WALLET
 
    def add(self,wallet,wallet_type,deposit_amount):
        
        wallet[self.username][list(wallet[self.username].keys())[wallet_type]] += deposit_amount
       
# FUNCTION TO WITHDRAW FUNDS FROM WALLET
# ALSO CHECKS IF THE FUNDS ARE ENOUGH FOR THE FEATURE TO BE USED, IF NOT IT THROWS AN ERROR

    def withdraw(self,wallet,wallet_type,withdraw_amt):
        keys = list(wallet[self.username].keys())

        if keys[wallet_type][3:] != 'MORTGAGE' :
            
            if wallet[self.username][keys[wallet_type]] >= withdraw_amt:
                wallet[self.username][keys[wallet_type]] -= withdraw_amt
                return(True)
            else:
                print('\nERROR : FUNDS REQUESTED MORE THAN AVILABLE IN WALLET')
                return(False)
        else:
            print('\nERROR : CAN NOT WITHDRAW FROM MORTGAGE WALLET')
            return(False)

c_data = {}
wallet = {}
sys_funds = 0 

login = False 
loop = True
loop2 = True

while True :


    print('\nL : LOGIN  \nC : CREATE NEW USER  \nA : admin_login \nQ : QUIT')
    action = input('WHAT WOULD YOU LIKE TO DO ? ')

#ADMIN LOGIN 
  
    if ((action == 'A') or (action == 'a')):
       
        password = input('\nENTER ADMIN PASSWORD : ')
        if password == 'admin' : 
            while True:
                action = input('\nC : CHECK ALL USER DATA \nW : CHECK ALL USER WALLET DATA \nS : CHECK SYSTEM FUNDS \nB : GO BACK TO LOGIN PAGE \n\nWHAT WOULD YOU LIKE TO DO ? ')
                if ((action == 'C') or (action == 'c')):
                    print (c_data)
                elif ((action == 'W') or (action == 'w')):
                    print(wallet)
                elif ((action == 'S') or (action == 's')):
                    print(sys_funds)
                elif ((action == 'B') or (action == 'b')):
                    break
                else :
                    print('ERROR : INVALID INPUT ')

# CREATE NEW USER
# CHECKS IF AGE IS AN INTEGER > 0 
# CHECKS EMAIL ID HAS '@'

    elif ((action == 'C') or (action == 'c')):
        # cearte a back function 
        while True:
            username = input('ENTER USERNAME : ')
            if username not in list(c_data.keys())  :
                f_name = input('ENTER FIRST NAME : ')
                l_name = input('ENTER LAST NAME : ')
                cor = input('ENTER COUNTRY OF RESIDENCY : ')
                while True :
                    try :
                        age = int(input('ENTER AGE : '))
                        if age <= 0 :
                            print('AGE CAN NOT BE NEGATIVE OR ZERO')
                        else :
                            break
                    except:
                        print('ERROR : AGE SHOULD BE AN INTEGER')
                while True :
                    email = input('ENTER EMAIL ID : ')
                    if '@' in email:
                        break
                    else :
                        print ('ERROR : INVALID EMAIL ID , EMAIL ID SHOULD HAVE @')
                password = input('ENTER PASSWORD : ')
                c_1 = Customer_account(f_name,l_name,cor,age,email,password,username)
                c_1.data(c_data)
                print('\n ACCOUNT SUCCESSFULLY CREATED Mr/Mrs.' , username.upper())
                break
            else: 
                print('\nUSERNAME TAKEN, TRY ANOTHER USERNAME')
                               
# HANDLES THE LOGIN FEATURE

    elif ((action == 'L') or (action == 'l')):
        username = input('\nENTER USERNAME : ')
        if username in list(c_data.keys()):
            while True: 
                password = input('\nENTER PASSWORD : ')
                if password == c_data[username]['password']:
                    print('\nWELCOME Mr/Mrs' , username.upper())
                    login = True 
                    break 
                else :
                    print('\nWRONG PASSWORD')
                    login = False
                    action = input('T : TRY AGAIN , G : GO BACK TO MAIN PAGE')
                    if ((action == 't') or (action == 'T')):
                        continue
                    elif ((action == 'g') or (action == 'G')):
                        break
        else:
            print('\nUSERNAME NOT FOUND') 
            continue
        
        if login :
            
            helper = Banking_system(username)
            username_wallet = Wallet(username)
            username_wallet.print_wallet(wallet) 
            
            while True : 
                # LOGOUT
                if not loop2:
                    loop2 = True
                    break
                
                print('\nA : ADD FUNDS IN EXISTING WALLET \nW : WITHDRAW FUNDS \nC : CREATE NEW WALLET  \nD : DELETE EXISTING WALLET  \nT : TRANSFER FUNDS TO DIFFERENT WALLET  \nO : TRANSFER TO OTHER USER \nS : SHOW WALLET \nDA : DELETE ACCOUNT   \nL : LOG OUT\n')
                action = input('WHAT WOULD YOU LIKE TO DO ? ')
                
                if ((action == 'L') or (action == 'l')):
                        break

                while True:

                    if not loop:
                        loop = True 
                        break

# SHOW WALLET 
                    if ((action == 'S') or (action == 's')):
                        username_wallet.print_wallet(wallet)  
                        break

# CREATE WALLET 
                    elif ((action == 'c') or (action == 'C')):    
                        if not username_wallet.create_wallet(wallet):
                            username_wallet.print_wallet(wallet)  
                            break

# ADD FUNDS               

                    elif((action == 'A') or (action == 'a')):

                        if username_wallet.check_wallets(wallet):
                            
                                username_wallet.print_wallet(wallet)
                                
                                wallet_type = username_wallet.wallet_position('\n0 : BACK TO MAIN PAGE \n\nPOSITION OF WALLET YOU WANT TO ADD FUNDS TO ?')
                                if wallet_type == -1:
                                    break
                                
                                add_amt = username_wallet.amount('\n0 : BACK TO MAIN PAGE \n\nAMOUNT TO ADD : ')
                                if add_amt == 0:
                                    break

                                username_wallet.add(wallet,wallet_type,add_amt)
                                username_wallet.print_wallet(wallet)
                                break
                            
                        else :
                            break   
# WITHDRAW FUNDS                
                    elif((action == 'W') or (action == 'w')):

                        if username_wallet.check_wallets(wallet):
                            username_wallet.print_wallet(wallet)

                            wallet_type = username_wallet.wallet_position('\n0 : BACK TO MAIN PAGE \n\nPOSITION OF WALLET YOU WANT TO WITHDRAW FUNDS FROM ?')
                            if wallet_type == -1:
                                break
                            if ((list(wallet[username].keys())[wallet_type][3:]) == 'MORTGAGE'):
                                print('\nERROR : CAN NOT WITHDRAW FUNDS FROM MORTAGE WALLETS ')
                            else :
                                withdraw_amt = username_wallet.amount('\n0 : BACK TO MAIN PAGE \n\nAMOUNT TO WITHDRAW : ')
                                if withdraw_amt == 0:
                                    break


                                username_wallet.withdraw(wallet,wallet_type,withdraw_amt)                                
                                username_wallet.print_wallet(wallet)
                                break
        
                        else :
                            break                 

# DELETE WALLET             
                    elif ((action == 'd') or (action == 'D')):
                        
                        if username_wallet.check_wallets(wallet):

                            wallet_type = username_wallet.wallet_position('\n0 : GO BACK TO MAIN PAGE \n\nPOSITION OF WALLET YOU WANT TO DELETE ? ')
                            if wallet_type == -1 :
                                break
                            print((list(wallet[username].keys()))[wallet_type])
                            del wallet[username][(list(wallet[username].keys()))[wallet_type]]
                            username_wallet.print_wallet(wallet)
                            break
                    
                        else :
                            break   

#TRANSFER FUNDS WITHIN USER 

                    elif ((action == 'T') or (action == 't')):
                        if username_wallet.check_wallets(wallet):
                            print('\nNOTE : TO USE THIS FEATURE, A SYSTEM CHARGE OF 0.5% OF THE TRANSFER AMOUNT WILL BE DEDUCTED FROM THE WALLET  \n CONTINUE ? \n Y : YES \n N : NO')
                            action_ = input('WHAT WOULD YOU LIKE TO DO ? ')
                            
                            if ((action_ == 'y') or (action_ == 'Y')):
                                while True:
                                    username_wallet.print_wallet(wallet)
                                    wallet_type = username_wallet.wallet_position('\n0 : GO BACK TO MAIN PAGE \n\nPOSITION OF WALLET YOU WANT TO TRANSFER FUNDS FROM ? ')
                                    
                                    if wallet_type == -1:
                                        loop = False
                                        break

                                    
                                    if ((list(wallet[username].keys())[wallet_type][3:]) == 'SAVINGS' or (list(wallet[username].keys())[wallet_type][3:]) == 'MORTGAGE'):
                                        print('\nERROR : CAN NOT TRANFER FUNDS FROM SAVINGS/MORTGAGE WALLETS ')
                                    else :
                                        wallet_transfer = username_wallet.wallet_position('\n0 : GO BACK TO MAIN PAGE \n\nPOSITION OF WALLET YOU WANT TO TRANSFER THE FUNDS TO ?')
                                        
                                        if wallet_transfer == -1:
                                            loop = False
                                            break

                                        if wallet_type == wallet_transfer:
                                            print('\nERROR : POSITION OF THE WALLETS CAN NOT BE SAME')
                                        else:
                                            transfer_amt = username_wallet.amount('\n0 : GO BACK TO MAIN PAGE \n\nTRANSFER AMOUNT ? ')
                                            if transfer_amt == 0:
                                                break
                                            funds = 0.005*transfer_amt
                                            if username_wallet.withdraw(wallet,wallet_type,transfer_amt+funds):
                                                
                                                sys_funds += funds
                                                username_wallet.add(wallet,wallet_transfer,transfer_amt)
                                                username_wallet.print_wallet(wallet)
                                                print('\nNOTE : ' + str(funds) + ' WAS CHARGED AS SYSTEM CHARGE ')
                                                print(sys_funds)
                                                loop = False
                                                break
                                    
                                
                            elif((action_ == 'N') or (action_ == 'n')):
                                break
                           
                            else:
                                print('\nERROR : INVALID INPUT, TRY AGAIN')
                        else:
                            break

#TRASFER FUNDS TO OTHER USER

                    elif ((action == 'O') or (action == 'o')):

                        if len(list(wallet.keys()))<2:
                            print('THERE ARE NO OTHER CUSTOMERS, ADD NEW TO USE THIS FEATURE')
                            break
                        
                        print('\nNOTE :  A SYSTEM CHARGE OF 1.5% OF THE TRANSFER AMOUNT WILL BE DEDUCTED FROM THE WALLET TO USE THIS FEATURE \n CONTINUE \n Y : YES \n N : NO?')
                        action_ = input('WHAT WOULD YOU LIKE TO DO ? ')

                        if ((action_ == 'Y')or (action_ == 'y')):
                            
                            list_other_user = list(c_data.keys())
                            list_other_user.remove(username)
                            print('LIST OF OTHER CUSTOMERS :' , list_other_user)

                            cust_username = input('USERNAME OF THE USER YOU WANT TO TRANSFER FUNDS TO ? ')
                            other_user_class = Wallet(cust_username)
                            print(cust_username , list_other_user)
                            if cust_username in list_other_user :
                                
                                if cust_username in list(wallet.keys()):
                                
                                    username_wallet.print_wallet(wallet)
                                    other_user_class.print_wallet(wallet)
                                    user_wallet_pos = helper.wallet_position('\n 0 : BACK TO MAIN PAGE\nPOSITION OF YOUR WALLET : ')
                                    if user_wallet_pos == -1:
                                        break
                                    
                                    if ((list(wallet[username].keys())[user_wallet_pos][3:]) == 'DAILY USE' ):
                                        
                                        cust_wallet_pos = helper.wallet_position('\n 0 : BACK TO MAIN PAGE\nPOSITION OF CUSTOMER WALLET :')
                                        if cust_wallet_pos == -1 :
                                            break
                                        transfer_amt = helper.amount('\n 0 : BACK TO MAIN PAGE\nFUNDS TO TRANSFER : ')
                                        if transfer_amt == 0 :
                                            break
                                        funds = transfer_amt*0.015
                                        if username_wallet.withdraw(wallet,user_wallet_pos,transfer_amt+funds):
                                            sys_funds += funds
                                            username_wallet.print_wallet(wallet)
                                            other_user_class.add(wallet,cust_wallet_pos,transfer_amt)
                                            other_user_class.print_wallet(wallet)
                                            print('\nNOTE : ' + str(funds) + ' WAS CHARGED AS SYSTEM CHARGE ')
                                        break
                                    else:
                                        print('ERROR : CAN NOT TRANSFER FUNDS TO OTHER USER FROM SAVING/MORTGAGE/HOLIDAY WALLET')
                                        break
                                    
                                else:
                                    print('THE USER DOES NOT HAVE AN ACTIVE WALLET')
                                    print('IF YOU WISH TO TRANSFER THE FUND, A NEW SAVINGS ACCOUNT WILL OPEN FOR MR/MRS ' + cust_username.upper() )
                                    action_ = input('DO YOU WISH TO CONTINUE ? Y : YES , N : NO ')
                                    if ((action_ == 'Y') or (action_ == 'y')):
                                        username_wallet.print_wallet(wallet)
                                        user_wallet_pos = helper.wallet_position('\n 0 : BACK TO MAIN PAGE\nPOSITION OF YOUR WALLET : ')
                                        if user_wallet_pos == -1:
                                            break
                                        transfer_amt = helper.amount('\n 0 : BACK TO MAIN PAGE\nFUNDS TO TRANSFER : ')
                                        if transfer_amt == 0 :
                                            break
                                        funds = transfer_amt*0.015
                                        if username_wallet.withdraw(wallet,user_wallet_pos,transfer_amt+funds):
                                            sys_funds += funds
                                            wallet[cust_username] = {'1) SAVINGS :' : transfer_amt}
                                        break
                            else:
                                print('\nERROR : USER NOT FOUND')
                        
                        elif((action_ == 'N')or (action_ == 'n')):
                            break
                        
                        else:
                            print('\nERROR : INVALID INPUT')
                            break                

#DELETE ACCOUNT               

                    elif((action == 'DA') or (action == 'da')):
                        
                        action_ = input('\nARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT ? \nY : YES \nN : NO \n\nWHAT WOULD YOU LIKE TO DO ?')
                        if ((action_ == 'Y') or (action_ == 'y')):
                            username_wallet
                            del c_data[username]
                            del wallet[username] 
                            loop2 = False
                            break
                        elif ((action_ == 'N') or (action_ == 'n')): 
                            break       
                        else:
                            print('\nERROR : INVALID INPUT') 
                                 
                    else:
                        print('\nERROR : INVALID INPUT')
                        break

# TERMINATES THE PROGRAMME                      

    elif((action == 'Q') or (action == 'q')):
        break

    else:
        print('\nINVALID INPUT , TRY AGAIN')
    

