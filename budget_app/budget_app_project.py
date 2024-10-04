class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.__balance = 0.0

    def __repr__(self):
        header = f"{self.description.center(30, '*')}\n"
        ledger = ""
        for item in self.ledger:
            # Format description and amount
            ledger += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.__balance:.2f}"
        return header + ledger + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.__balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, category_instance):
        if self.withdraw(amount, f"Transfer to {category_instance.description}"):
            category_instance.deposit(amount, f"Transfer from {self.description}")
            return True
        return False

    def check_funds(self, amount):
        return self.__balance >= amount


def create_spend_chart(categories):
    # Step 1: Calculate total spent in each category
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        spent_amounts.append(spent)

    # Step 2: Calculate the total spent across all categories
    total_spent = sum(spent_amounts)

    # Step 3: Calculate percentage spent by each category (rounded down to nearest 10)
    spent_percentage = [(amount / total_spent) * 100 for amount in spent_amounts]
    spent_percentage = [int(percent // 10) * 10 for percent in spent_percentage]

    # Step 4: Build the bar chart (from 100% to 0%)
    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in spent_percentage:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Step 5: Add the separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Step 6: Add the category names vertically
    max_len = max(len(category.description) for category in categories)
    category_names = [category.description.ljust(max_len) for category in categories]

    for i in range(max_len):
        chart += "     "
        for name in category_names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip("\n")


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

entertainment = Category("Entertainment")
entertainment.deposit(500, "initial deposit")
entertainment.withdraw(100, "movies")
entertainment.withdraw(50, "concert")

# Output the ledger of each category
print(food)
print(clothing)
print(entertainment)

# Create the spending chart
print(create_spend_chart([food, clothing, entertainment]))
# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96
