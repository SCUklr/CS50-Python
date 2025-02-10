# Personal Finance Management System

#### Video Demo: https://www.bilibili.com/video/BV19wNdemEbK/?spm_id_from=333.1387.upload.video_card.click&vd_source=40c958a131c45fc50601fe50c9b28095


#### Description:

The Personal Finance Management System is a command-line based tool designed to help users efficiently track and manage their daily financial transactions. This project was built using Python and aims to provide an intuitive interface for recording income and expenses, querying transactions, and generating detailed financial reports. The system leverages core Python programming concepts, including file I/O, regular expressions for data validation, and modular programming, to create a robust solution for personal financial management.

## Project Overview

Managing personal finances can often feel overwhelming, especially when done manually. With this system, users can easily add new transactions by providing essential details such as the transaction date, category (income or expense), amount, and additional notes. The application then stores these records in a JSON file for persistence, ensuring that all data is maintained between sessions. Additionally, the tool offers functionalities to query transactions based on specific criteria, such as date ranges or categories, and generate a summarized report that highlights total income, total expenses, and net income.

## Key Features

- **Transaction Entry**: Users can add new transactions with a specified date (validated against the YYYY-MM-DD format using regular expressions), category, amount, and a brief note. The system validates user input to prevent common errors, ensuring that all records are accurate and reliable.

- **Data Querying**: The system supports querying of stored transactions based on user-defined filters. Whether you need to see all income entries, expenses, or transactions within a particular date range, the query function provides a flexible and straightforward way to retrieve the desired information.

- **Financial Reporting**: A core component of the system is its ability to generate financial reports. The report summarizes key financial data by calculating the total income, total expenses, and the net income, offering users a quick snapshot of their financial status.

- **Data Persistence**: All transaction data is stored in a JSON file (`transactions.json`). This ensures that your financial records are maintained between sessions and can be easily imported or exported for further analysis.

## Project Structure

- **project.py**:
  This is the main module of the application. It contains the `main()` function, which serves as the entry point for the program, and other supporting functions such as:
  - `load_transactions()`: Loads existing transaction data from the JSON file.
  - `save_transactions()`: Saves the current list of transactions back to the JSON file.
  - `add_transaction()`: Handles adding new transactions with input validation.
  - `query_transactions()`: Filters transactions based on provided criteria.
  - `generate_report()`: Compiles and calculates financial statistics based on the transaction data.

- **test_project.py**:
  This file contains unit tests written using pytest. Each of the core functions (adding transactions, querying transactions, and generating reports) is tested to ensure that the application behaves as expected under various scenarios. Testing is an integral part of this project, ensuring the reliability and stability of the code.

- **requirements.txt**:
  While the project primarily relies on Python's standard libraries, any additional dependencies (if introduced later) can be listed in this file to facilitate easy installation.

## Design Decisions and Future Enhancements

During development, several design choices were made to enhance code readability and maintainability. For instance, regular expressions are used to enforce a strict date format, which helps in maintaining consistency in the transaction records. The system is structured in a modular way, which not only simplifies testing but also allows for future expansion. Potential enhancements for this project could include:

- Introducing a graphical user interface (GUI) for improved user interaction.
- Expanding the reporting capabilities to include data visualization, such as charts and graphs.
- Adding features for budgeting, recurring transactions, and alerts to further assist users in managing their finances.
- Refactoring parts of the code to incorporate object-oriented programming (OOP) principles, which can improve scalability as new features are added.

## How to Run

1. **Installation**:
   Ensure you have Python installed on your system. Clone or download this project repository to your local machine.

2. **Running the Application**:
   Open a terminal, navigate to the project directory, and execute the following command: python project.py

This will start the application and display a menu for interacting with the finance management system.

3. **Running Tests**:
To run the unit tests and verify that all functionalities are working as expected, execute: pytest

Make sure you have pytest installed. If not, you can install it using: pip install pytest


## Conclusion

The Personal Finance Management System is an ideal project for demonstrating proficiency in Python programming. It combines fundamental programming concepts with practical application, resulting in a tool that is both useful and extendable. Whether you are managing your own finances or looking to showcase your coding skills, this project offers a comprehensive solution that can be further developed and enhanced over time.



