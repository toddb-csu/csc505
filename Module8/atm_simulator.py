# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 8: Final Project
#
# The ATM class will print all the steps in sequence for all the operations at the ATM machine.
class ATM:
    def __init__(self):
        self.state = "Idle"  # Initial state of ATM
        self.error_counter = 0  # Error counter for each incorrect PIN entered
        self.max_attempts = 2  # Max number of attempts to enter correct PIN
        self.account_balance = 250  # Initial account balance
        self.pin = "1234"  # Hardcoded PIN for demo
        self.card_inserted = False

    def transition(self, event, pin_entered=None, amount=0):
        print(f"\nCURRENT STATE: {self.state} | EVENT: {event}")

        if self.state == "Idle":
            if event == "CardInserted":
                self.card_inserted = True
                self.state = "Validating debit card"
                self.entry_action("Card Inserted")

        elif self.state == "Validating debit card":
            if event == "CardValidated":
                self.state = "Waiting for PIN"
                self.entry_action("Waiting for PIN")
            else:
                self.state = "Ejecting Card"
                self.transition("CardEjected")

        elif self.state == "Waiting for PIN":
            if event == "PINEntered":
                if pin_entered == self.pin:
                    self.error_counter = 0
                    self.state = "Validating PIN"
                    self.entry_action("PIN Entered")
                else:
                    self.error_counter += 1
                    print(f"Wrong PIN! Attempts left: {self.max_attempts - self.error_counter}")
                    if self.error_counter < self.max_attempts:
                        self.state = "Waiting for PIN"
                        self.entry_action("Waiting for PIN")
                    else:
                        self.state = "Ejecting Card"
                        self.exit_action("Card Ejected")

        elif self.state == "Validating PIN":
            if event == "PINValidated":
                self.state = "Displaying Menu"
                self.entry_action("Menu Displayed")
            else:
                self.state = "Ejecting Card"
                self.transition("CardEjected")

        elif self.state == "Displaying Menu":
            if event == "DepositSelected":
                self.state = "Processing Deposit"
                self.entry_action("Deposit Amount Entered")
            elif event == "WithdrawSelected":
                self.state = "Processing Withdrawal"
                self.entry_action("Withdrawal Amount Entered")
            elif event == "ExitSelected":
                self.state = "Ejecting Card"
                self.exit_action("Card Ejected")
                self.state = "Idle"
                self.entry_action("Idle")
            elif event == "CheckBalanceSelected":
                self.state = "Checking Balance"
                self.entry_action("Checked Balance")

        elif self.state == "Checking Balance":
            if event == "BalanceDisplayed":
                print(f"Current balance: ${self.account_balance}")
                if self.account_balance > 0:
                    self.state = "Displaying Menu"
                    self.entry_action("Menu Displayed")
                elif self.account_balance == 0:
                    self.state = "Closing Account"
                    self.entry_action("Account Closed")

        elif self.state == "Processing Deposit":
            if event == "DepositAmountEntered":
                print(f"Amount entered: ${amount}")
                if amount > 0:
                    self.account_balance += amount
                self.state = "Depositing Funds"
                self.entry_action("Funds Deposited")

        elif self.state == "Depositing Funds":
            if event == "DepositFundsSubmitted":
                self.state = "Displaying Menu"
                self.entry_action("Menu Displayed")

        elif self.state == "Processing Withdrawal":
            if event == "WithdrawAmountEntered":
                print(f"Amount entered: ${amount}")
                self.state = "Verifying Funds Available"
                self.entry_action("Verified Funds Available")

        elif self.state == "Verifying Funds Available":
            if event == "WithdrawFundsVerified":
                if (amount <= self.account_balance) and (amount > 0):
                    self.account_balance -= amount
                    self.state = "Dispensing Funds"
                    self.entry_action("Dispensed Funds")
                else:
                    print("Insufficient balance or invalid amount!")
                    self.state = "Ejecting Card"
                    self.exit_action("Card Ejected")

        elif self.state == "Dispensing Funds":
            if event == "WithdrawFundsDispensed":
                print(f"Dispensing ${amount}. New balance: ${self.account_balance}")
                self.state = "Ejecting Card"
                self.exit_action("Card Ejected")

        elif self.state == "Ejecting Card":
            if event == "CardEjected":
                self.state = "Idle"
                self.entry_action("Idle")

        elif self.state == "Closing Account":
            if event == "AccountClosed":
                print("Account closed due to zero balance.")
                self.exit_action("Account Closed")
                self.state = "Ejecting Card"
                self.exit_action("Card Ejected")

    def entry_action(self, state):
        actions = {
            "Card Inserted": "Validating card...",
            "Waiting for PIN": "Prompting customer for PIN...",
            "PIN Entered": "Validating PIN...",
            "Menu Displayed": "Displaying menu (Withdraw, Deposit, Check Balance, Exit)...",
            "Deposit Amount Entered": "Prompting customer for deposit amount...",
            "Funds Deposited": "Prompting customer for deposit funds...",
            "Checked Balance": f"Fetching balance...",
            "Withdrawal Amount Entered": "Prompting customer for withdrawal amount...",
            "Verified Funds Available": "Verifying withdrawal funds available...",
            "Dispensed Funds": "Dispensing funds...",
            "Card Ejected": "Ejecting card...",
            "Account Closed": "Closing account, notifying bank...",
            "Idle": "ATM is idle. Welcome!"
        }
        print(actions[state])

    def exit_action(self, state):
        actions = {
            "Authenticated": "Ejecting card. Thank you!",
            "Dispense Funds": "Dispensing funds...",
            "Card Ejected": "Ejecting card...",
            "Account Closed": "Account update complete. Notifying customer."
        }
        if state in actions:
            print(actions[state])


if __name__ == "__main__":
    # Simulation
    atm = ATM()
    atm.entry_action("Idle")  # Start

    # Successful flow
    atm.transition("CardInserted")
    atm.transition("CardValidated")
    atm.transition("PINEntered", pin_entered="1234")  # Correct PIN
    atm.transition("PINValidated")
    # Deposit
    atm.transition("DepositSelected")
    atm.transition("DepositAmountEntered", amount=100)
    atm.transition("DepositFundsSubmitted", amount=100)
    # Checking balance
    atm.transition("CheckBalanceSelected")
    atm.transition("BalanceDisplayed")
    # Withdrawal
    atm.transition("WithdrawSelected")
    atm.transition("WithdrawAmountEntered", amount=50)
    atm.transition("WithdrawFundsVerified", amount=50)
    atm.transition("WithdrawFundsDispensed", amount=50)
    atm.transition("CardEjected")

    # Wrong PIN flow (fail after 2 attempts)
    print("\n--- SIMULATING WRONG PIN ---")
    atm.transition("CardInserted")
    atm.transition("CardValidated")
    atm.transition("PINEntered", pin_entered="1111")  # Attempt 1
    atm.transition("PINEntered", pin_entered="2222")  # Attempt 2 (Card Ejected)
    atm.transition("CardEjected")

    # Zero balance scenario
    print("\n--- SIMULATING ZERO BALANCE ---")
    atm.account_balance = 0  # Force zero balance
    atm.transition("CardInserted")
    atm.transition("CardValidated")
    atm.transition("PINEntered", pin_entered="1234")
    atm.transition("PINValidated")
    atm.transition("CheckBalanceSelected")
    atm.transition("BalanceDisplayed")
    atm.transition("AccountClosed")
    atm.transition("CardEjected")
