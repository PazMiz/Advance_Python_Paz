# Bank Customer Management App

![Bank App Screenshot](/path/to/screenshot.png)  # Replace with an actual screenshot of your app

## Description

The Bank Customer Management App is a simple Python application built using the Kivy framework. It allows you to manage and interact with different categories of bank customers, including VIP customers, premium customers, and regular customers.

## Features

- View a list of bank customers categorized by VIP, premium, and regular customers.
- Deposit money for VIP customers.
- Withdraw money for VIP customers (premium and regular customers are not allowed to withdraw).
- Filter customers based on their categories (VIP, premium, regular).

## Installation

1. Clone the repository to your local machine.

git clone https://github.com/PazMiz/Advance_Python

css
Copy code

2. Navigate to the project directory.

cd bank-app

markdown
Copy code

3. Install the required dependencies.

pip install kivy
requests

bash
Copy code

## Usage

Run the following command to start the Bank Customer Management App.

python main.py

python
Copy code

## How It Works

- The app creates instances of bank customers, including VIP, premium, and regular customers.
- The main screen displays a list of customers with their names, account balances, and action buttons.
- Clicking on a VIP customer's name allows you to deposit money to their account.
- Clicking on a premium customer's name allows you to select an action (deposit or withdraw) and perform the action accordingly.

## Credits

- Kivy: https://kivy.org
- Picsum Photos: https://picsum.photos

## License

This project is licensed under the [MIT License](LICENSE).
