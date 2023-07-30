from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.uix.gridlayout import GridLayout

# Base class for bank customers
class Customer:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

# Subclass for VIP customers
class VIPCustomer(Customer):
    def __init__(self, name, account_balance):
        super().__init__(name, account_balance)

# Subclass for premium customers
class PremiumCustomer(Customer):
    def __init__(self, name, account_balance):
        super().__init__(name, account_balance)

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

# Subclass for regular customers
class RegularCustomer(Customer):
    def __init__(self, name, account_balance):
        super().__init__(name, account_balance)

    def withdraw(self, amount):
        return False

# Create instances of the Customer subclasses
vip_customer1 = VIPCustomer("Paz (VIP)", 10000)
premium_customer1 = PremiumCustomer("Eyal (Premium)", 5000)
premium_customer2 = PremiumCustomer("Sol (Premium)", 3000)
regular_customer1 = RegularCustomer("Michel (Regular)", 1000)
regular_customer2 = RegularCustomer("David (Regular)", 2000)

class BankApp(App):
    def build(self):
        self.vip_customers = [vip_customer1]
        self.premium_customers = [premium_customer1, premium_customer2]
        self.regular_customers = [regular_customer1, regular_customer2]

        self.show_vip_customers = False  # Initialize the attribute to False
        self.show_premium_customers = False  # Initialize the attribute to False
        self.show_regular_customers = False  # Initialize the attribute to False

        layout = BoxLayout(orientation='vertical')
        self.list_label = Label(text="List of Bank Customers:", color=(1, 0, 0, 1))
        self.customer_list = BoxLayout(orientation='vertical')
        self.vip_count_label = Label(text="VIP Customers: 0", color=(1, 0, 0, 1))
        self.premium_count_label = Label(text="Premium Customers: 0", color=(1, 2, 0, 1))
        self.regular_count_label = Label(text="Regular Customers: 0", color=(0, 0, 1, 1))

        self.update_customer_list()

        vip_button = Button(text="Show VIP Customers", on_press=self.filter_vip_customers)
        premium_button = Button(text="Show Premium Customers", on_press=self.filter_premium_customers)
        regular_button = Button(text="Show Regular Customers", on_press=self.filter_regular_customers)

        layout.add_widget(self.list_label)
        layout.add_widget(self.customer_list)
        layout.add_widget(vip_button)
        layout.add_widget(premium_button)
        layout.add_widget(regular_button)
        layout.add_widget(self.vip_count_label)
        layout.add_widget(self.premium_count_label)
        layout.add_widget(self.regular_count_label)

        return layout
    
    def update_customer_list(self):
        self.customer_list.clear_widgets()

        customers = []
        if self.show_vip_customers:
            customers.extend(self.vip_customers)
        if self.show_premium_customers:
            customers.extend(self.premium_customers)
        if self.show_regular_customers:
            customers.extend(self.regular_customers)

        for customer in customers:
            customer_button = Button(text=f"{customer.name} - Balance: {customer.account_balance} $",
                                     on_press=lambda instance, customer=customer: self.on_customer_click(customer))

            # Set color based on customer type
            if isinstance(customer, VIPCustomer):
                customer_button.color = get_color_from_hex('#FF0000')  # Red for VIP customers
            elif isinstance(customer, RegularCustomer):
                customer_button.color = get_color_from_hex('#0000FF')  # Blue for regular customers
            else:
                customer_button.color = get_color_from_hex('#00FF00')  # Green for premium customers

            self.customer_list.add_widget(customer_button)

        self.vip_count_label.text = f"VIP Customers: {len(self.vip_customers)}"
        self.premium_count_label.text = f"Premium Customers: {len(self.premium_customers)}"
        self.regular_count_label.text = f"Regular Customers: {len(self.regular_customers)}"

    def filter_vip_customers(self, instance):
        self.show_vip_customers = True
        self.show_premium_customers = False
        self.show_regular_customers = False
        self.update_customer_list()

    def filter_premium_customers(self, instance):
        self.show_vip_customers = False
        self.show_premium_customers = True
        self.show_regular_customers = False
        self.update_customer_list()

    def filter_regular_customers(self, instance):
        self.show_vip_customers = False
        self.show_premium_customers = False
        self.show_regular_customers = True
        self.update_customer_list()

    def on_customer_click(self, customer):
        # If the customer is a premium customer, show action popup (deposit or withdraw)
        if isinstance(customer, PremiumCustomer):
            self.create_action_popup(customer)

    def create_action_popup(self, customer):
        # Create a popup for premium customers to select action (deposit or withdraw)
        popup_layout = BoxLayout(orientation='vertical')
        deposit_button = Button(text="Deposit", on_press=lambda instance: self.perform_action(customer, "deposit"))
        withdraw_button = Button(text="Withdraw", on_press=lambda instance: self.perform_action(customer, "withdraw"))
        popup_layout.add_widget(deposit_button)
        popup_layout.add_widget(withdraw_button)

        self.popup = Popup(title=f"{customer.name} - Select Action", content=popup_layout, size_hint=(0.5, 0.5))
        self.popup.open()

    def perform_action(self, customer, action):
        # Perform the selected action for the premium customer
        self.popup.dismiss()  # Dismiss the popup after the action is selected
        if action == "deposit":
            # For premium customers, show a deposit dialog to enter the deposit amount
            self.show_deposit_popup(customer)
        elif action == "withdraw":
            # For premium customers, show a withdraw dialog to enter the withdraw amount
            self.show_withdraw_popup(customer)

    def show_deposit_popup(self, customer):
        # Create a popup to enter the deposit amount for premium customers
        popup_layout = FloatLayout()
        amount_label = Label(text="Enter Deposit Amount:")
        amount_input = TextInput(size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "top": 0.6})
        deposit_button = Button(text="Deposit", size_hint=(0.3, 0.1), pos_hint={"x": 0.35, "y": 0.2},
                                on_press=lambda instance: self.deposit_money(customer, amount_input.text))
        popup_layout.add_widget(amount_label)
        popup_layout.add_widget(amount_input)
        popup_layout.add_widget(deposit_button)

        popup = Popup(title=f"{customer.name} - Deposit Money", content=popup_layout, size_hint=(0.5, 0.5))
        popup.open()

    def deposit_money(self, customer, amount):
        # Perform the deposit for the premium customer
        try:
            amount = float(amount)
            customer.deposit(amount)
            self.update_customer_list()
        except ValueError:
            # Invalid input
            pass

    def show_withdraw_popup(self, customer):
        # Create a popup to enter the withdraw amount for premium customers
        popup_layout = FloatLayout()
        amount_label = Label(text="Enter Withdraw Amount:")
        amount_input = TextInput(size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "top": 0.6})
        withdraw_button = Button(text="Withdraw", size_hint=(0.3, 0.1), pos_hint={"x": 0.35, "y": 0.2},
                                 on_press=lambda instance: self.withdraw_money(customer, amount_input.text))
        popup_layout.add_widget(amount_label)
        popup_layout.add_widget(amount_input)
        popup_layout.add_widget(withdraw_button)

        popup = Popup(title=f"{customer.name} - Withdraw Money", content=popup_layout, size_hint=(0.5, 0.5))
        popup.open()

    def withdraw_money(self, customer, amount):
        # Perform the withdraw for the premium customer
        try:
            amount = float(amount)
            if customer.withdraw(amount):
                self.update_customer_list()
        except ValueError:
            # Invalid input
            pass

if __name__ == '__main__':
    BankApp().run()
