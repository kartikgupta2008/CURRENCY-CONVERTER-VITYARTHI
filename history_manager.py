# history_manager.py
# This is the second main module. It handles history and simple reports.

from datetime import datetime


def load_history(filename):
    history = []

    try:
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line != "":
                history.append(line)
        file.close()
    except FileNotFoundError:
        file = open(filename, "w")
        file.close()

    return history


def save_history(filename, history):
    file = open(filename, "w")
    for item in history:
        file.write(item + "\n")
    file.close()


def add_history(history, amount, from_currency, result, to_currency):
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M")
    text = (date_time + " | " + str(round(amount, 2)) + " " +
            from_currency + " = " + str(round(result, 2)) + " " + to_currency)
    history.append(text)


def show_history(history):
    print("\nConversion History")
    print("------------------")

    if len(history) == 0:
        print("No conversions have been made yet.")
        return

    number = 1
    for item in history:
        print(str(number) + ".", item)
        number += 1


def search_history(history, word):
    print("\nSearch Results")
    print("--------------")
    found = False

    for item in history:
        if word.upper() in item.upper():
            print(item)
            found = True

    if not found:
        print("No matching conversion was found.")


def clear_history(history):
    history.clear()


def show_report(history):
    print("\nConversion Report")
    print("-----------------")
    print("Total conversions:", len(history))

    if len(history) > 0:
        print("First conversion:", history[0])
        print("Latest conversion:", history[-1])
    else:
        print("No conversion data is available yet.")


def save_report(filename, history):
    file = open(filename, "w")
    file.write("Currency Converter Report\n")
    file.write("=========================\n")
    file.write("Total conversions: " + str(len(history)) + "\n")

    if len(history) > 0:
        file.write("First conversion: " + history[0] + "\n")
        file.write("Latest conversion: " + history[-1] + "\n")

    file.close()
    print("Report saved to", filename)
