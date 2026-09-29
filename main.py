# main.py
# Main program file. It connects the three main modules.

import os
from converter import convert_amount, show_conversion
from currency_manager import load_currencies, save_currencies
from currency_manager import show_currencies, add_currency, update_currency, delete_currency
from history_manager import load_history, save_history, add_history
from history_manager import show_history, search_history, clear_history
from history_manager import show_report, save_report

CURRENCY_FILE = "data/currencies.txt"
HISTORY_FILE = "data/history.txt"
REPORT_FILE = "data/conversion_report.txt"


def prepare_files():
    if not os.path.exists("data"):
        os.makedirs("data")


def valid_number(text):
    # This avoids try/except and keeps input checking simple.
    text = text.strip()
    if text.count(".") > 1:
        return False
    text = text.replace(".", "", 1)
    return text.isdigit()


def get_amount():
    while True:
        value = input("Enter amount: ").strip()
        if valid_number(value):
            amount = float(value)
            if amount > 0:
                return amount
        print("Please enter a valid amount greater than 0.")


def get_currency(rates, message):
    while True:
        code = input(message).strip().upper()
        if code in rates:
            return code
        print("Currency not found. Please enter a code from the list.")


def get_new_code(rates):
    while True:
        code = input("Enter new 3-letter currency code: ").strip().upper()
        if len(code) == 3 and code.isalpha() and code not in rates:
            return code
        print("Enter a new 3-letter code that is not already present.")


def get_rate(code):
    while True:
        value = input("Enter value of 1 " + code + " in INR: ").strip()
        if valid_number(value):
            rate = float(value)
            if rate > 0:
                return rate
        print("Please enter a valid rate greater than 0.")


def show_menu():
    print("\n====================================")
    print("        CURRENCY CONVERTER")
    print("====================================")
    print("1. Convert currency")
    print("2. View currencies")
    print("3. Add currency")
    print("4. Update currency rate")
    print("5. Delete currency")
    print("6. View conversion history")
    print("7. Search history")
    print("8. Clear history")
    print("9. View report")
    print("10. Save report")
    print("11. Exit")
    print("------------------------------------")


def convert_currency(rates, history):
    show_currencies(rates)
    from_currency = get_currency(rates, "Convert from: ")
    to_currency = get_currency(rates, "Convert to: ")
    amount = get_amount()

    result = convert_amount(amount, from_currency, to_currency, rates)
    show_conversion(amount, from_currency, result, to_currency)
    add_history(history, amount, from_currency, result, to_currency)
    save_history(HISTORY_FILE, history)


def add_new_currency(rates):
    code = get_new_code(rates)
    rate = get_rate(code)
    success, message = add_currency(rates, code, rate)
    print(message)
    if success:
        save_currencies(CURRENCY_FILE, rates)


def update_rate(rates):
    show_currencies(rates)
    code = get_currency(rates, "Enter currency code to update: ")
    rate = get_rate(code)
    success, message = update_currency(rates, code, rate)
    print(message)
    if success:
        save_currencies(CURRENCY_FILE, rates)


def delete_existing_currency(rates):
    show_currencies(rates)
    code = get_currency(rates, "Enter currency code to delete: ")
    success, message = delete_currency(rates, code)
    print(message)
    if success:
        save_currencies(CURRENCY_FILE, rates)


def main():
    prepare_files()
    rates = load_currencies(CURRENCY_FILE)
    history = load_history(HISTORY_FILE)

    print("\nWelcome to my Currency Converter Project!")
    print("This project uses sample exchange rates for academic use.")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            convert_currency(rates, history)
        elif choice == "2":
            show_currencies(rates)
        elif choice == "3":
            add_new_currency(rates)
        elif choice == "4":
            update_rate(rates)
        elif choice == "5":
            delete_existing_currency(rates)
        elif choice == "6":
            show_history(history)
        elif choice == "7":
            word = input("Enter currency code or text to search: ").strip()
            search_history(history, word)
        elif choice == "8":
            clear_history(history)
            save_history(HISTORY_FILE, history)
            print("Conversion history cleared.")
        elif choice == "9":
            show_report(history)
        elif choice == "10":
            save_report(REPORT_FILE, history)
        elif choice == "11":
            print("Thank you for using my Currency Converter Project!")
            break
        else:
            print("Invalid choice. Please select from 1 to 11.")


if __name__ == "__main__":
    main()
