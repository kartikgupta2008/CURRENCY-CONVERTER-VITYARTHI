# currency_manager.py
# This is the first main module. It manages currencies and their rates.

DEFAULT_RATES = {
    "INR": 1.0,
    "USD": 83.0,
    "EUR": 90.0,
    "GBP": 105.0,
    "JPY": 0.56,
    "AUD": 55.0
}


def load_currencies(filename):
    rates = {}

    try:
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            if line != "" and "=" in line:
                code, rate = line.split("=", 1)
                rates[code.strip().upper()] = float(rate.strip())
        file.close()
    except FileNotFoundError:
        rates = DEFAULT_RATES.copy()
        save_currencies(filename, rates)

    if len(rates) == 0:
        rates = DEFAULT_RATES.copy()
        save_currencies(filename, rates)

    return rates


def save_currencies(filename, rates):
    file = open(filename, "w")
    for code in sorted(rates):
        file.write(code + "=" + str(rates[code]) + "\n")
    file.close()


def show_currencies(rates):
    print("\nAvailable Currencies")
    print("--------------------")
    for code in sorted(rates):
        print(code, "=", rates[code], "INR")


def add_currency(rates, code, rate):
    code = code.upper()
    if code in rates:
        return False, "This currency already exists."
    rates[code] = rate
    return True, "Currency added successfully."


def update_currency(rates, code, rate):
    code = code.upper()
    if code not in rates:
        return False, "Currency not found."
    rates[code] = rate
    return True, "Currency rate updated successfully."


def delete_currency(rates, code):
    code = code.upper()
    if code == "INR":
        return False, "INR is the base currency and cannot be deleted."
    if code not in rates:
        return False, "Currency not found."
    del rates[code]
    return True, "Currency deleted successfully."
