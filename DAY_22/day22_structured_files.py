expenses = [
{ "id":1 , "amount":500 , "category":"food" },
{ "id":2 , "amount":200 , "category":"transport" },
{ "id":3 , "amount":1000 , "category":"rent" }
]

def save_expenses(expenses):
    try:
        with open ("expenses.txt", "w") as file:
            for expense in expenses:
                line = f"{expense['id']},{expense['amount']},{expense['category']}\n"
                file.write(line)
    except FileNotFoundError:
        print( "File not found" )


def load_data():
    expenses = []
    try:
        with open ("expenses.txt", "r") as file:
            for line in file:
                clean_line = line.strip()

                if(len(clean_line) != 0):
                    parts = clean_line.split(",")
                    exp_id = int(parts[0])
                    exp_amount = int(parts[1])
                    exp_category = parts[2]
                    expense = {
                        'id' : exp_id,
                        'amount' : exp_amount,
                        'category' : exp_category
                    }
                    expenses.append(expense)
                else:
                    continue
            return expenses
        
    except FileNotFoundError:    
        return expenses

def print_data(expenses):
    if(len(expenses) == 0):
        print("No expenses found!!")
    else:
        for expense in expenses:
            print(f"ID : {expense['id']} | Amount : {expense['amount']} | Category : {expense['category']}")

save_expenses(expenses)
result = load_data()
print_data(result)