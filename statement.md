# Project Statement

## Project Title

**Currency Converter System**

## Problem Statement

Currency conversion is a common requirement when people compare international prices, travel, or simply want to understand the value of money in another currency. Doing repeated calculations manually can be inconvenient.

I identified this as a small real-world problem that can be solved using basic Python. My project provides a menu-based Currency Converter System that performs the conversion and keeps a record of previous conversions.

## Proposed Solution

The proposed system uses Python and three main modules:

1. `converter.py` – handles conversion calculations.
2. `currency_manager.py` – handles currency data and CRUD operations.
3. `history_manager.py` – handles history and reports.

`main.py` connects these modules and controls the menu.

The project uses simple text files for storage instead of a database. This makes the system easy to understand and suitable for a beginner-level Python course.

## Scope

The system covers:

- Currency conversion.
- Viewing available currencies.
- Adding currencies.
- Updating currency rates.
- Deleting currencies except the INR base currency.
- Saving conversion history.
- Searching and clearing history.
- Viewing and saving a simple report.

The system does not currently cover live exchange rates, online payments, financial advice or a graphical interface.

## Target Users

- Students learning Python.
- Beginners practising modules and file handling.
- Travellers checking approximate currency values.
- Users who need a simple local currency calculator.

## Objectives

1. Identify a simple real-world problem.
2. Build a working Python solution for the problem.
3. Divide the solution into three meaningful modules.
4. Apply functions, loops, conditions, dictionaries and file handling.
5. Demonstrate CRUD operations.
6. Keep the program understandable enough for a student to explain.
7. Prepare proper documentation and testing.

## Functional Requirements

- **FR1:** Convert an amount from one available currency to another.
- **FR2:** Display available currencies and their sample rates.
- **FR3:** Add a new currency.
- **FR4:** Update an existing currency rate.
- **FR5:** Delete a currency except INR.
- **FR6:** Save and display conversion history.
- **FR7:** Search and clear conversion history.
- **FR8:** Generate and save a simple report.

## Non-Functional Requirements

- **Usability:** The interface should be simple and understandable.
- **Reliability:** Saved currency and history data should remain available after restarting the program.
- **Maintainability:** Each main module should have a clear responsibility.
- **Performance:** Normal operations should be quick for the small local dataset.
- **Portability:** The project should run using Python's standard library.
- **Scalability:** The structure should allow more currencies and features later.

## Assumptions

- The exchange rates are sample academic values.
- INR is used as the base currency for storing rates.
- The user has Python 3 installed.
- The program has permission to read and write its local data files.

## Success Criteria

The project is successful if a user can run the program, convert currencies, manage currency rates, save and search conversion history, and generate a report through the menu without requiring an online service or database.
