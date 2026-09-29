# converter.py
# This module does the main currency calculation.


def convert_amount(amount, from_currency, to_currency, rates):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # The rates dictionary stores the INR value of 1 unit of a currency.
    amount_in_inr = amount * rates[from_currency]
    result = amount_in_inr / rates[to_currency]
    return result


def show_conversion(amount, from_currency, result, to_currency):
    print("\nConversion Result")
    print("-----------------")
    print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
