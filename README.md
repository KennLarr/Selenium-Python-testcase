This repository contains an automated testing framework built using Selenium WebDriver, Python, and PyTest.
The test suite includes functional UI test cases such as Login, Sign Up, and Contact Us, with test data sourced dynamically from an Excel (.xlsx) file.

The project is structured for scalability and follows the Page Object Model (POM) design pattern.

| Feature                | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| 🔐 `test_login`        | Validates login functionality using credentials from Excel    |
| 📝 `test_sign_up`      | Automates user registration flow with parameterized test data |
| 📩 `contact_us`        | Tests contact form by filling fields and uploading a file     |
| 📊 Excel Data Driven   | Reads test data using `openpyxl` for dynamic inputs           |
| 🧱 POM Architecture    | Clean maintainable structure using page objects               |
| 🧪 PyTest Support      | Supports fixtures, assertions, and reporting                  |
| 🌐 Cross-Browser Ready | Can easily extend to Firefox, Edge, etc.                      |


Download Project and Open in VS Code
