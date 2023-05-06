import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

rows = 3
cols = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def winnings_check(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def slot_machine_spin_get(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    column = []
    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        for i in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
        column = []

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()


def deposit():
    while True:
        amount = input("Enter your deposit value: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit value must be greater than 0.")
        else:
            print("Deposit value must be a valid number.")

    return amount


def lines_number():
    while True:
        lines = input("Enter the number o lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if (lines >= 1) and (lines <= 3):
                break
            else:
                print("Enter a number of lines between 1 - 3.")
        else:
            print("Enter a valid number of lines.")

    return lines


def bet_get():
    while True:
        bet = input("Enter your bet value for each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet value must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Bet value must be a valid number.")

    return bet


def spin(balance):
    lines = lines_number()
    while True:
        bet = bet_get()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough cash. Your current balance is ${balance}")
        else:
            break

    print(f"Your betting ${bet} in {lines} lines. Total bet = ${total_bet}")

    slots = slot_machine_spin_get(rows, cols, symbols)
    print_slot_machine(slots)
    winnings, winning_lines = winnings_check(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Currente balance is ${balance}")
        start = input("Press enter to spin or q to quit.")
        if start == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()