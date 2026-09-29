# Currency Converter System

## VITyarthi – Build Your Own Project

### 1. Project Overview

This is a simple **Currency Converter System** made in Python. I selected this problem because currency conversion is something people may need when travelling, checking international prices, or learning about different currencies.

I wanted the project to be useful but also easy enough for me to understand and explain. So, instead of using a live API or a database, I used sample exchange rates and simple text files.

The project is divided into **3 main Python modules**, apart from `main.py`:

- `converter.py` – performs the conversion calculation.
- `currency_manager.py` – manages currencies and rates using CRUD operations.
- `history_manager.py` – stores conversion history and creates a simple report.

`main.py` works as the controller and connects these three modules.

## 2. Problem Statement

Doing currency calculations manually again and again can be inconvenient. A small program can make the calculation quicker and can also keep a record of previous conversions.

The proposed system allows a user to select two currencies, enter an amount, and get the converted value. It also allows currencies to be added, updated or deleted and keeps a local conversion history.

## 3. Main Features

1. Currency conversion between available currencies.
2. Six sample currencies included initially: INR, USD, EUR, GBP, JPY and AUD.
3. Add a new currency.
4. Update a currency rate.
5. Delete a currency, except INR because INR is the base currency.
6. View conversion history.
7. Search conversion history.
8. Clear conversion history.
9. View a simple conversion report.
10. Save the report in a text file.
11. Save currency data and history locally so data is available after restarting the program.
12. Basic input validation without making the code unnecessarily complicated.

## 4. Sample Rates

| Currency | Sample value of 1 unit in INR |
|---|---:|
| INR | 1.00 |
| USD | 83.00 |
| EUR | 90.00 |
| GBP | 105.00 |
| JPY | 0.56 |
| AUD | 55.00 |

**Note:** These are fixed sample rates for the academic project. They are not live exchange rates.

## 5. Three Main Modules

### Module 1 – `converter.py`

This module contains the main conversion formula. It changes the source amount into INR first and then changes INR into the target currency.

**Formula:**

`Amount in INR = Amount × Source Currency Rate`

`Converted Amount = Amount in INR ÷ Target Currency Rate`

This method means that I do not need to write a separate formula for every possible currency pair.

### Module 2 – `currency_manager.py`

This module manages the currency list and rates.

It handles:
- Loading currency data from a text file.
- Saving currency data.
- Viewing currencies.
- Adding a currency.
- Updating a rate.
- Deleting a currency.

This module demonstrates **CRUD** operations.

### Module 3 – `history_manager.py`

This module manages what happens after a conversion.

It handles:
- Loading history.
- Saving history.
- Adding a new conversion to history.
- Viewing history.
- Searching history.
- Clearing history.
- Showing and saving a simple report.

## 6. `main.py`

`main.py` is not counted as one of the three main modules. It acts as the controller of the project.

It displays the menu, takes input from the user, performs basic validation and calls the required function from the three modules.

## 7. Functional Requirements

- **FR1:** The user can convert an amount between available currencies.
- **FR2:** The user can view all available currencies.
- **FR3:** The user can add a new currency.
- **FR4:** The user can update a currency rate.
- **FR5:** The user can delete a currency except INR.
- **FR6:** The system stores conversion history.
- **FR7:** The user can search and clear history.
- **FR8:** The user can view and save a simple report.

## 8. Non-Functional Requirements

- **Usability:** The program uses a simple menu and clear messages.
- **Reliability:** Currency data and history are saved in local files.
- **Maintainability:** The three main modules have separate responsibilities.
- **Performance:** The program works quickly for the small local dataset.
- **Portability:** Only Python and its standard library are required.
- **Scalability:** More currencies and features can be added later.

## 9. Data Storage

The project uses text files instead of a database.

- `data/currencies.txt` – stores currency rates.
- `data/history.txt` – stores previous conversions.
- `data/conversion_report.txt` – stores the generated report.

This choice keeps the project simple and matches the level of a beginner Python course.

## 10. Project Structure

```text
Currency-Converter-System/
│
├── main.py
├── converter.py
├── currency_manager.py
├── history_manager.py
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── currencies.txt
│   ├── history.txt
│   └── conversion_report.txt
│
├── docs/
│   ├── architecture.md
│   ├── process_flow.png
│   ├── architecture.png
│   ├── use_case.png
│   ├── component_diagram.png
│   ├── sequence_diagram.png
│   └── testing.md
│
└── report/
    ├── Currency_Converter_Project_Documentation.docx
    └── Currency_Converter_Project_Report.pdf
```

## 11. How to Run

1. Install Python 3.
2. Open the project folder in VS Code or another Python editor.
3. Open the terminal in the project folder.
4. Run:

```text
python main.py
```

5. Select an option from the menu.

No external Python package is needed to run the project.

## 12. Testing

The project includes test cases for:

- Normal conversion.
- Reverse conversion.
- Invalid amount.
- Invalid menu choice.
- Adding a currency.
- Adding a duplicate currency.
- Updating a rate.
- Deleting INR.
- Viewing and searching history.
- Saving the report.

The expected results are documented in `docs/testing.md`.

## 13. Limitations

- Exchange rates are fixed sample values.
- There is no live currency API.
- The program is command-line based.
- Text files are used instead of a database.
- The program is intended for learning and academic demonstration, not financial decisions.

## 14. Future Improvements

If I continue this project, I would like to:

- Connect a live exchange-rate API.
- Add a graphical interface.
- Use a database for larger amounts of data.
- Add login and user accounts.
- Add charts and more detailed reports.

## 15. What I Learned

Through this project I practiced functions, conditions, loops, dictionaries, modules, file handling, CRUD operations, validation, testing, documentation and GitHub organization.

## 16. GitHub Upload

The repository can be uploaded directly to GitHub. The important files for evaluation are the Python source files, `README.md`, `statement.md`, the `data` folder, the `docs` folder and the project report.
