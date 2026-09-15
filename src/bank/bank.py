class Bank():
    """
    Represents a bank account.

    Money can be deposited with deposit_money()
    Money can be withdrawn with withdraw_money()
    Account balance can be cheked with check_balance()
    Calculated interest can be addeD with apply_interest()
    If the balance is enough to pay a bill can be checked with check_sufficient_funds()
    """

    def __init__(self, balance = 0.0):
        """
           Creates an account with balance 0, if not changed at instantiation.
           :param __account_balance (float): Initial balance set to 0
        """
        if balance < 0:
            raise ValueError("Cannot deposit negative amount")
        else:
            self.__account_balance = balance

# --------------------------------------------------------------------------------

    def deposit_money(self, amount_to_deposit):
        """
        Adds amount to account balance.
        :param amount_to_deposit:
        """
        if amount_to_deposit < 1:
            raise ValueError("Cannot deposit less than 1 kr")
        else:
            self.__account_balance += amount_to_deposit

    # --------------------------------------------------------------------------------

    def withdraw_money(self, amount_to_withdraw):
        """
        Subtracts amount from account balance.
        :param amount_to_withdraw:
        """
        if amount_to_withdraw < 0:
            raise ValueError("Cannot withdraw negative amount")
        elif amount_to_withdraw > self.__account_balance:
            raise ValueError("Cannot withdraw amount greater than account balance")
        else:
            self.__account_balance -= amount_to_withdraw

    # --------------------------------------------------------------------------------

    def check_balance(self):
        """
        Checks the account balance.
        :return: Account balance
        """
        return round(self.__account_balance, 2)

    # --------------------------------------------------------------------------------

    def apply_interest(self, interest):
        """
        Applies percental interest on account balance.
        :param interest in percent:
        """
        if interest < 0 or interest > 100:
            raise ValueError("Not an interest within 1 - 100")
        else:
            self.__account_balance *= ((interest / 100) + 1)

    # --------------------------------------------------------------------------------

    def check_sufficient_funds(self, bill_amount):
        """
        Checks if funds is enough to cover bill amount.
        :param bill_amount: The amount to check
        :return: True/ False
        """
        if self.__account_balance >= bill_amount:
            return True
        else:
            return False