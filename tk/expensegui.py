import tkinter as tk
from tkinter import messagebox

class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def calculate_total(self):
        return sum(expense.amount for expense in self.expenses)
    

class ExpenseTrackerApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Expense Tracker")
        self.tracker = ExpenseTracker()

        self.amount_label = tk.Label(root, text= "Amount")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.category_label = tk.Label(root, text= "Category")
        self.category_label.pack()
        self.category_entry = tk.Entry(root)
        self.category_entry.pack()

        self.date_label = tk.Label(root, text= "Date")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.desc_label = tk.Label(root, text= "Description")
        self.desc_label.pack()
        self.desc_entry = tk.Entry(root)
        self.desc_entry.pack()

        self.add_button = tk.Button(root,text="Add Expense",command=self.add_expense())
        self.add_button.pack()

        self.total_button = tk.Button(root,text="Show Total",command=self.calculate_total())
        self.total_button.pack()
    

    def add_expense(self):
        amount = float(self.amount_entry.get())
        category = self.category_entry.get()
        date = self.date_entry.get()
        description = self.desc_entry.get()

        expense = Expense(amount,category,date,description)
        self.tracker.add_expense(expense)

        messagebox.showinfo("Info","Expense Added")
        self.clear_entries()

    def show_total(self):
        total = self.tracker.calculate_total()
        messagebox.showinfo("Total",f"Total Expense:{total}")
    
    def clear_entries(self):
        self.amount_entry.delete(0,tk.END)
        self.category_entry.delete(0,tk.END)
        self.date_entry.delete(0,tk.END)
        self.desc_entry.delete(0,tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()