# Testing – Currency Converter System

| ID | Test case | Expected result |
|---|---|---|
| T01 | Convert 100 USD to INR | 8300 INR using the sample rate |
| T02 | Convert 1000 INR to JPY | About 1785.71 JPY |
| T03 | Enter zero amount | Amount is rejected |
| T04 | Enter text instead of amount | Program asks for a valid number |
| T05 | Enter an invalid menu choice | Invalid-choice message is displayed |
| T06 | Add a new currency | Currency is added and saved |
| T07 | Add an existing currency | Duplicate currency is rejected |
| T08 | Update a currency rate | New rate is saved |
| T09 | Try to delete INR | Deletion is rejected because INR is the base currency |
| T10 | View history | Previous conversions are displayed |
| T11 | Search history | Matching conversions are displayed |
| T12 | Save report | Report is written to the report text file |

## Testing approach

I used both normal cases and invalid-input cases. The main calculation can also be checked directly through the function in `converter.py`. The purpose is to make sure common user mistakes do not immediately stop the program and that saved data can be loaded again after restarting it.
