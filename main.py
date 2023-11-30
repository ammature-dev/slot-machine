import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

COLS = 3
ROWS = 3
symbols_Count = {
    "A" : 2 ,
    "B" : 4 ,
    "C" : 6 ,
    "D" : 8
}
symbol_value = {
    "A" : 5 ,
    "B" : 4 ,
    "C" : 3 ,
    "D" : 2
}

def check_winnings(columns,lines,bets,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_check=column[line]
            if symbol != symbol_check:
                break
        else:
            winnings+=values[symbol]*bets
            winning_lines.append(line+1)

    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print (column[row] , end="|")
            else:
                print (column[row] , end="")

        print()        
    


def deposit():
    while True:
        amount=input("what would you like to deposit? $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print ("please enter an amount greater than 0.")

        else:
            print("please enter amount in digit.")

    return amount

def get_no_lines():
    while True:
        lines = input("how many lines would you like to select (1-"+str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print ("please enter valid lines.")
        else:
            print("please enter lines in digit.")
    return lines

def get_bet():
    while True:
        amount=input("what would you like to bet on each line ? $ ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print (f" amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a valid number")
    return amount

def spin(balance):
    lines=get_no_lines()

    while True:
        bet=get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print (f"you cannot bet that amount, your balance is :${balance}")
        else:
            break
            
    print (f"you are betting ${bet} on {lines} lines, so your total bet :${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbols_Count)
    print_slot_machine_spin(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on lines:", *winning_lines)

    return winnings-total_bet

def main():
    balance=deposit()
    while True:
        print(f"your current balance ${balance}.")
        answer=input("press enter to spin(q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print (f"your left with ${balance}. ")

    
main()
