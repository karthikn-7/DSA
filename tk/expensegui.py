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

        self.add_button = tk.Button(root,text="Add Expense",command=self.add_expense)
        self.add_button.pack()

        self.total_button = tk.Button(root,text="Show Total",command=self.show_total)
        self.total_button.pack()

        self.show_expense_button = tk.Button(root,text="Show Expenses",command=self.show_expenses)
        self.show_expense_button.pack()


        self.expense_listbox_frame = tk.Frame(root)
        self.expense_listbox_frame.pack()

        self.expense_listbox = tk.Listbox(self.expense_listbox_frame, width=50, height=10)
        self.expense_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.expense_listbox_frame, orient="vertical")
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.Y)

        self.expense_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.expense_listbox.yview)
    

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")
            return
        category = self.category_entry.get()
        date = self.date_entry.get()
        description = self.desc_entry.get()

        if not category or not date or not description:
            messagebox.showerror("Missing Information", "Please fill in all fields.")
            return

        expense = Expense(float(amount),category,date,description)
        self.tracker.add_expense(expense)

        messagebox.showinfo("Info","Expense Added")
        self.clear_entries()

    def show_total(self):
        total = self.tracker.calculate_total()
        messagebox.showinfo("Total",f"Total Expense:{total}")
    
    def show_expenses(self):
        self.expense_listbox.delete(0,tk.END)
        for expense in self.tracker.expenses:
            display_text = f"Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}, Description: {expense.description}"
            self.expense_listbox.insert(tk.END,display_text)
    
    def clear_entries(self):
        self.amount_entry.delete(0,tk.END)
        self.category_entry.delete(0,tk.END)
        self.date_entry.delete(0,tk.END)
        self.desc_entry.delete(0,tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()