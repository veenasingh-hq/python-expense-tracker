# =================================================================
# Project 19 - ExpenseEngine: Automated Finance Analytics Tool
# =================================================================

import json
import os
from datetime import datetime

class ExpenseEngine:
    def __init__(self):
        """Initializes internal database configuration and directory routing."""
        self.file_name = "expenses.json"
        self.categories = ["Food", "Transport", "Utilities", "Entertainment", "Healthcare", "Others"]

    def _load_database(self):
        """Internal helper to stream data from local storage into application memory."""
        if not os.path.exists(self.file_name):
            return []
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def _save_database(self, data):
        """Internal helper to flush application memory state into secure local storage."""
        try:
            with open(self.file_name, "w") as file:
                json.dump(data, file, indent=2)
            return True
        except IOError as e:
            print(f"❌ Storage Write Failure: {e}")
            return False

    def log_expense(self):
        """Processes transaction details with structural verification and appends to storage."""
        print("\n--- Log New Financial Transaction ---")
        db = self._load_database()

        # 1. Title Processing
        title = input("Enter Expense Title/Description: ").strip()
        if not title:
            print("❌ Input Validation Error: Description field cannot remain vacant.")
            return

        # 2. Category Verification Loop
        print("\nAvailable Allocation Categories:")
        for idx, cat in enumerate(self.categories, 1):
            print(f" [{idx}] {cat}")
        
        try:
            cat_choice = int(input("\nSelect category index number: "))
            if cat_choice < 1 or cat_choice > len(self.categories):
                print("❌ Input Validation Error: Selected index falls outside target parameters.")
                return
            selected_category = self.categories[cat_choice - 1]
        except ValueError:
            print("❌ Type Error: Numerical parameter required.")
            return

        # 3. Currency Metric Verification
        try:
            amount = float(input("Enter Amount Spent (₹): "))
            if amount <= 0:
                print("❌ Mathematical Constraint: Monetary amount must be greater than absolute zero.")
                return
        except ValueError:
            print("❌ Type Error: Decimal value mapping required.")
            return

        # Construct unified structural transactional schema
        transaction_entry = {
            "id": f"TXN{int(datetime.now().timestamp())}",
            "title": title,
            "category": selected_category,
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        db.append(transaction_entry)
        if self._save_database(db):
            print(f"✅ System Success: Registered ₹{amount:.2f} to allocation node '{title}'.")

    def display_statement(self):
        """Queries database records to generate human-readable financial ledgers."""
        print("\n--- Consolidated Ledger Statements ---")
        db = self._load_database()

        if not db:
            print("🚫 Ledger State: No structural historical entries found in storage.")
            return

        print(f"{'TXN ID':<12} | {'Date & Time':<20} | {'Description':<20} | {'Category':<15} | {'Amount':<10}")
        print("-" * 86)
        for txn in db:
            print(f"{txn['id']:<12} | {txn['timestamp']:<20} | {txn['title']:<20} | {txn['category']:<15} | ₹{txn['amount']:<10.2f}")

    def run_analytics_engine(self):
        """Executes analytical pipelines to map mathematical usage profiles across categories."""
        print("\n--- Core Analytics & Mathematical Breakdown ---")
        db = self._load_database()

        if not db:
            print("🚫 Engine Alert: Calculation pipeline terminated due to empty dataset.")
            return

        total_outflow = sum(txn["amount"] for txn in db)
        
        # Matrix to aggregate performance weights per category
        category_weights = {cat: 0.0 for cat in self.categories}
        for txn in db:
            category_weights[txn["category"]] += txn["amount"]

        print(f"📊 Gross Consolidated Capital Outflow: ₹{total_outflow:,.2f}\n")
        print(f"{'Target Category':<15} | {'Aggregated Cost':<16} | {'Percentage Burden'}")
        print("-" * 55)
        
        for category, expenditure in category_weights.items():
            if expenditure > 0:
                percentage = (expenditure / total_outflow) * 100
                print(f"{category:<15} | ₹{expenditure:<15,.2f} | {percentage:.1f}%")
            else:
                print(f"{category:<15} | ₹{expenditure:<15,.2f} | 0.0%")

    def boot_terminal(self):
        """Establishes execution loops mapping runtime choices to core logical pipelines."""
        while True:
            print("\n" + "="*45)
            print("📊 EXPENSEENGINE: ARCHITECTURAL COMMAND CENTER")
            print("="*45)
            print("1. Log New Asset/Capital Expenditure")
            print("2. Print Detailed Transaction Ledger")
            print("3. Execute Analytical Spending Breakdown")
            print("4. Shut Down Engine")
            print("="*45)
            
            choice = input("Select operation interface (1-4): ").strip()
            
            if choice == "1":
                self.log_expense()
            elif choice == "2":
                self.display_statement()
            elif choice == "3":
                self.run_analytics_engine()
            elif choice == "4":
                print("\n👋 Disconnecting core frameworks safely. System offline.")
                break
            else:
                print("❌ Runtime Alert: Input command index invalid.")

if __name__ == "__main__":
    engine = ExpenseEngine()
    engine.boot_terminal()