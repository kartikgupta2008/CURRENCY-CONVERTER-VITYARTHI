# Architecture – Currency Converter System

The project uses a simple modular design with **three main Python modules** and one controller file.

```text
                         USER
                           |
                           v
                        main.py
                    (menu + input)
                  /        |        \
                 v         v         v
          converter.py  currency_    history_
                       manager.py    manager.py
                          |             |
                          v             v
                  currencies.txt   history.txt
                                         |
                                         v
                               conversion_report.txt
```

## Why these three modules?

I selected the three modules based on the three main jobs of the application:

1. **converter.py** – calculation of the converted amount.
2. **currency_manager.py** – managing currency rates and CRUD operations.
3. **history_manager.py** – storing previous conversions and creating the report.

`main.py` is the controller that connects them. This is enough modular separation for the project without making it unnecessarily complicated.
