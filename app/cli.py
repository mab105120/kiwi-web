from termcolor import colored

from app.services.db.investment_dao import (get_investments_by_portfolio,
                                            purchase, sell)
from app.services.db.portfolio_dao import create_new, get_portfolios_by_user
from app.services.db.user_dao import create_user, delete_user, get_all


def print_main_menu():
    return ('''
Welcome to Kiwi!
----------------
MAIN MENU
----------------
1. Users Menu
2. Portfolio Menu
3. Market Menu
0. Exit

>>''')

def print_user_menu():
        return ('''
----------------
USER MENU
----------------
1. View all users
2. Add User
3. Delete User
0. Return to main menu

>>''')

def print_portfolio_menu():
        return ('''
----------------
PORTFOLIO MENU
----------------
1. View portfolio by user
2. Add Portfolio
0. Return to main menu

>>''')

def print_market_menu():
        return ('''
----------------
Market MENU
----------------
1. View investments by portfolio
2. Purchase
3. Sell
0. Return to main menu

>>''')

def user_prompt():
    while(True):
        user_input = input(print_user_menu())
        if user_input == '1':
            users = get_all()
            if len(users) == 0:
                 print(colored('No users exist', 'blue'))
            for user in users:
                print(colored(user, 'blue'))
        elif user_input == '2':
            username_input = input('Username: ')
            password_input = input('Password: ')
            balance_input = input('balance: ')
            try:
                create_user(username_input, password_input, float(balance_input))
                print(colored('User created successfully', 'green'))
            except Exception as e:
                print(colored(e, 'red'))
        elif user_input == '3':
            try:
                userid_input = input('id: ')
                delete_user(userid_input)
                print(colored('Deleted user successfully', 'green'))
            except Exception as e:
                print(colored(f'Failed to delete user with ID {user_input}: {e}', 'red'))
        elif user_input == '0':
             break
        else:
            print(colored('Invalid input', 'red'))

def porfolio_prompt():
    while(True):
        user_input = input(print_portfolio_menu())
        if user_input == '1':
            userid_input = input('user id: ')
            try:
               userid = int(userid_input)
               portfolios = get_portfolios_by_user(userid)
               if len(portfolios) == 0:
                    print(colored('This user has no portfolios', 'blue'))
               for portfolio in portfolios:
                    print(colored(portfolio, 'blue'))
            except Exception as e:
                print(colored(f'Failed to get portfolios: {e}', 'red'))
        elif user_input == '2':
            userid_input = input('User id: ')
            name_input = input('Portfolio name: ')
            strategy_input = input('Porfolio strategy: ')
            try:
                userid = int(userid_input)
                create_new(name_input, strategy_input, userid)
                print(colored('Portfolio created successfully', 'green'))
            except Exception as e:
                 print(colored(f'Failed to create portfolio: {e}', 'red'))
        elif user_input == '0':
             break
        else:
             print(colored('Invalid input', 'red'))

def market_prompt():
    while(True):
        user_input = input(print_market_menu())
        if user_input == '1':
            portfolioid_input = input('Portfolio id: ')
            try:
               portfolioid = int(portfolioid_input)
               investments = get_investments_by_portfolio(portfolioid)
               if len(investments) == 0:
                    print(colored('No investments exist in this portfolio', 'blue'))
               for investment in investments:
                    print(colored(investment, 'blue'))
            except Exception as e:
                print(colored(f'Failed to view investments: {e}', 'red'))
        if user_input == '2':
            portid_input = input('Portfolio id: ')
            ticker_input = input('Ticker: ')
            price_input = input('Price: ')
            qty_input = input('Quantity: ')
            try:
                portid = int(portid_input)
                price = float(price_input)
                qty = int(qty_input)
                purchase(portid, ticker_input, price, qty)
                print(colored('Purchase order completed successfully', 'green'))
            except Exception as e:
                print(colored(f'Could not complete purchase order: {e}', 'red'))
        if user_input == '3':
            investid_input = input('investment id: ')
            qty_input = input('Quantity: ')
            price_input = input('Price: ')
            try:
                investid = int(investid_input)
                qty = int(qty_input)
                price = float(price_input)
                sell(investid, qty, price)
                print(colored('Sale order completed successfully', 'green'))
            except Exception as e:
                print(colored(f'Failed to process the sale order: {e}', 'red'))
        if user_input == '0':
            break

def run():
    while(True):
        user_input = input(print_main_menu())
        if user_input == '1':
             user_prompt()
        if user_input == '2':
             porfolio_prompt()
        if user_input == '3':
             market_prompt()
        if user_input == '0':
                break
        
if __name__ == '__main__':
     run()