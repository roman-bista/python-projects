import json
import random
import string
from pathlib import Path


class Bank:
    DATABASE = "data.json"

    def __init__(self):
        self.data = self.load_data()

    # ---------- FILE HANDLING ----------
    def load_data(self):
        if Path(self.DATABASE).exists():
            with open(self.DATABASE, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.DATABASE, "w") as f:
            json.dump(self.data, f, indent=4)

    # ---------- UTILS ----------
    def generate_account(self):
        alpha = random.choices(string.ascii_letters, k=3)
        nums = random.choices(string.digits, k=3)
        special = random.choice("@#$%")
        acc = alpha + nums + [special]
        random.shuffle(acc)
        return "".join(acc)

    def find_user(self, acc, pin):
        for user in self.data:
            if user["accountno"] == acc and user["pin"] == pin:
                return user
        return None

    # ---------- OPERATIONS ----------
    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be 18+ and PIN must be 4 digits"

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountno": self.generate_account(),
            "balance": 0
        }

        self.data.append(user)
        self.save_data()
        return True, user

    def deposit(self, acc, pin, amount):
        user = self.find_user(acc, pin)
        if not user:
            return False, "Invalid credentials"
        if amount <= 0:
            return False, "Invalid amount"

        user["balance"] += amount
        self.save_data()
        return True, user["balance"]

    def withdraw(self, acc, pin, amount):
        user = self.find_user(acc, pin)
        if not user:
            return False, "Invalid credentials"
        if amount > user["balance"]:
            return False, "Insufficient balance"

        user["balance"] -= amount
        self.save_data()
        return True, user["balance"]

    def delete_account(self, acc, pin):
        user = self.find_user(acc, pin)
        if not user:
            return False, "Invalid credentials"

        self.data.remove(user)
        self.save_data()
        return True, "Account deleted"
