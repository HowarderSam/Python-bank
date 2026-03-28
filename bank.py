from colorama import Fore,Style, init 

currency = {'UAH': 1, 'USD': 41.48, 'EUR': 45.2, 'BTC': 2884251.82, 'ETH': 100494.46, 'PLN': 10.3848, 'GBP': 53.6675, 'CHF': 48.02, 'CZK': 1.78}
user_wallets = {}
admins = {}
users = {}

def add_admin():
    username = (input('Please create a username for Admin: '))
    if username in admins:
        print(Fore.RED + 'This admin username already exists. Please choose another.')
        return
    while True:
        password = input('Create a password by using only numbers: ')
        if password.isdigit():
            password_int = int(password)
            admins[username] = password_int
            print(Fore.GREEN + f'Your password will be {password}, please remember it ')
            break
        else:
            print(Fore.RED + 'Password must be numeric. Please try again.')

def add_user():
    username = input('Please create a username for User: ')
    if username in users:
        print(Fore.RED + 'This user username already exists. Please choose another.')
        return
    while True:
        password = input('Create a password by using only numbers: ')
        if password.isdigit():
            password_int = int(password)
            users[username] = password_int
            print(Fore.GREEN + f'User account created for {username}')
            break
        else:
            print(Fore.RED + 'Password must be numeric. Please try again.')

def login(role):
    username = input(f'Please enter your {role} username: ') 
    if role == 'Admin':
        if username in admins:
            password = input('Enter your Admin password: ')
            if password.isdigit() and int(password) == admins[username]:
                print(Fore.GREEN + f'Welcome, Admin {username}')
                return 'Admin'
            else:
                print(Fore.RED + 'Incorrect password for Admin.')
        else:
            print(Fore.RED + 'Admin username not found')
    elif role == 'User':
        if username in users:
            password = input('Enter your User password: ')
            if password.isdigit() and int(password) == users[username]:
                print(Fore.GREEN + f'Welcome, User {username}')
                return 'User'
            else:
                print(Fore.RED + 'Incorrect password for User.')
        else:
            print(Fore.RED + 'User username not found.')
    return None

def add_categories():
    categ = input('Введіть назву нової категорії: ')
    if categ:
        user_wallets[categ] = dict()
        print(Fore.BLUE + '✅Готово!')
    else:
        print(Fore.RED + '❌Error: you need to type at least 1 symbol to create a new category!')

def add_money():
    categ = input('Введіть назву категорії куди хочете додати кошти: ')
    print()
    if categ in user_wallets:
        money = int(input('Введіть кількість коштів: '))
        print()
        cur = input('Введіть назву валюти: ')
        if cur in currency:
            user_wallets[categ][cur] = money
            print(Fore.GREEN + '✅Готово!')
        else:
            print(Fore.RED + 'Error: there is no such currency in our bank!')
    else:
        print(Fore.RED + 'Error: there is no such category!')

def del_categ():
    categ = input('Введіть назву категорії яку хочете видалити: ')
    if categ in user_wallets:
        print('If you delete a category you will lose all your money! ')
        print('You should better transfer your money from the picked category to another, so you wont lose all your money in this category! ')
        ask = input('Are you sure you want to delete this category?:')
        if ask.lower() in ['yes', 'y']:
            final_ask = input('Are you absolutely sure? This action can\'t be undone! ')
            if final_ask.lower() in ['yes', 'y']:  
                user_wallets.pop(categ)
                print(Fore.GREEN + '✅Готово!')
            elif ask.lower() in ['no', 'n']:
                print(Fore.RED + 'Deletion process canceled! ')
        elif ask.lower() in ['no', 'n']:
            print(Fore.RED + 'Deletion process canceled! ')
    else:
        print(Fore.RED + 'Error: there is no such category')

def send_money():
    what_categ = input('Введіть звідки хочете відправити кошти: ')  
    currenc = input('Введіть валюту в якої хочете відправити кошти: ')
    amount = int(input('Введіть скільки коштів хочете відправити: '))
    if what_categ in user_wallets:
        print(Fore.GREEN + '✅Categorie found!')
    else:
        print(Fore.RED + 'There is no such category!')
    if amount > user_wallets[what_categ][currenc]:
        print(Fore.RED + 'You can\'t send more money than you have!')
    else:
        cur_conv = input('В якій валюті будете зберігати кошти?: ')
        if cur_conv in currency:
            hrn_convert  = amount * currency[currenc]
            final_convert = hrn_convert / currency[cur_conv]
            user_wallets[what_categ][currenc] -= amount
            in_categ  = input('В яку категорію хочете відправити кошти: ')
            if in_categ in user_wallets:
                if cur_conv is user_wallets[in_categ]:
                    user_wallets[in_categ][cur_conv] += final_convert
                    print(Fore.GREEN + '✅Готово!')
                else:
                    user_wallets[in_categ][cur_conv] = final_convert
                    print(Fore.GREEN + '✅Готово!')
        else:
            print(Fore.RED + 'ERROR!')

def all_wallets():
    print(Fore.BLUE + str(user_wallets))

def all_cur():
    print(Fore.BLUE + str(currency.keys()))


def user_terminal():
    print("Welcome to the User Terminal!")
    while True:
        print("1. See all currencies\n2. See Admin wallets by username\n3. Exit the User Terminal")
        comm = int(input("Enter command number: "))
        if comm == 1:
            all_cur() 
        elif comm == 2:
            admin_name = input("Enter the Admin username to view their wallets: ")
            if admin_name in admins:
                print(Fore.BLUE + f"Wallets for Admin {admin_name}: {user_wallets}")
            else:
                print(Fore.RED + "Error: Admin not found!")
        elif comm == 3:
            print(Fore.GREEN + "Exiting User Terminal. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid command!")


def bank():
   while True:
    print("Welcome!")
    print("1. Create Admin account")
    print("2. Create User account")
    print("3. Login")
    print("4.Exit the app")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        add_admin()
    elif choice == 2:
        add_user()
    elif choice == 3:
        role = input("Are you logging in as Admin or User? (Admin/User): ").capitalize()
        if role == "Admin":
            if login('Admin'):
                admin_terminal()
        elif role == "User":
            if login("User"):
                user_terminal()
        else:
            print(Fore.RED+'Error')
    elif choice == 4:
        print(Fore.GREEN + "Exiting the app.Goodbye!")
        return 
    else:
        print(Fore.RED + 'Invalid choice! Please select a valid option.')
        return

def admin_terminal():
    while True:    
        print("1. Create a wallet\n2. Delete a wallet\n3. Add cash\n4. See all wallets\n5. Send cash\n6. See all currencies\n7. Exit to the choice menu")
        comm = int(input("Enter command number: \n"))
        print("\n")

        if comm == 1:
            add_categories()
        elif comm == 2:
            del_categ()
        elif comm == 3:
            add_money()
        elif comm == 4:
            all_wallets()
        elif comm == 5:
            send_money()
        elif comm == 6:
            all_cur()
        elif comm == 7:
            return 1
        else:
            print(Fore.RED + 'There is no such command!')







bank()
