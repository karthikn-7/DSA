class Expenses:
    def __init__(self,amount,category,date,description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def addExpense(self,amount:int,category:str,date:str,description:str):

        expenses = Expenses(amount,category,date,description)
        self.expenses.append(expenses)

    def viewExpenses(self):
        for expense in self.expenses:
            print(f"Amount:{expense.amount}, Category:{expense.category}, Date:{expense.date}, Description:{expense.description}")

    def calculateTotal(self):
        total = 0
        for expense in self.expenses:
            total+= expense.amount
        print(total)

    def saveToFile(self,filename):
        with open(filename, "w") as file:
            for expense in self.expenses:
                file.write(f"{expense.amount},{expense.category},{expense.date},{expense.description}\n")

    def loadFromFile(self,filename):
        self.expenses.clear()
        with open(filename,"r") as file:
            for line in file:
                amount, category, date, description = line.strip().split(",")
                self.addExpense(float(amount),category,date,description)


if __name__ == "__main__":

    expense1 = ExpenseTracker()
    expense1.addExpense(100,"food","26/8/24","bought chicken")
    expense1.addExpense(300,"food","26/8/24","bought gothumai,maidha,carrots,beans")
    expense1.addExpense(5,"transport","26/8/24","train fare")
    expense1.viewExpenses()
    print()
    expense1.loadFromFile("expense.csv")
    expense1.viewExpenses()
    expense1.calculateTotal()






