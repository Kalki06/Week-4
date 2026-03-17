def expense_input():
    while True:
        try:
            id_= int(input("Enter the ID : "))
            amount = int(input("Enter the Amount : "))
            category = input("Enter the Category : ")
            break
        except ValueError:
            continue

    return id_, amount, category

def id_input():
    while True:
        try:
            id_= int(input("Enter the ID : "))
            break
        except ValueError:
            continue
    return id_

def add_expense(expenses, input_id, input_amount, input_category):

    for expense in expenses:
        if(expense['id'] == input_id):
            return False

    if(input_amount <= 0):
        return False
    
    if(input_category == ""):
        return False
    
    input_expense = {
        'id' : input_id,
        'amount' : input_amount,
        'category' : input_category
    }

    expenses.append(input_expense)
    return True

def delete_expense(expenses, target_id):
    for i in range(len(expenses)):
        if(expenses[i]['id'] == target_id):
            del expenses[i]
            return True
    return False

def find_expense_by_id(expenses, target_id):
	for expense in expenses:
		if(expense['id'] == target_id):
			return expense
	return None

def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense['amount']
    return total

def save_expenses(expenses, filename):
    with open (filename, "w") as file:
        for expense in expenses:
            line = f"{expense['id']},{expense['amount']},{expense['category']}\n"
            file.write(line)

def load_expenses(filename):
    expenses = []

    try:
        with open(filename, "r") as file:
            for line in file:
                clean_line = line.strip()
                parts = clean_line.split(",")

                if len(parts) != 3:
                    continue

                try:
                    exp_id = int(parts[0])
                    exp_amount = int(parts[1])
                    exp_category = parts[2]
                except ValueError:
                    continue

                expense = {
                    "id": exp_id,
                    "amount": exp_amount,
                    "category": exp_category
                }

                expenses.append(expense)

    except FileNotFoundError:
        return []

    return expenses


def main():
    filename = "tracker.txt"
    expenses = load_expenses(filename)

    while True:
        print("Enter 1 for add")
        print("Enter 2 for delete")
        print("Enter 3 for search")
        print("Enter 4 for total")
        print("Enter 5 for exit")
        print("\n")

        user_choice = input("Enter your choice here : ")
        print("\n")

        if(user_choice == "1"):
            input_id, input_amount, in_category  = expense_input()
            result = add_expense(expenses, input_id, input_amount, in_category)

            if(result == True):
                save_expenses(expenses, filename)
                print("\n")
            else:
                print("something went wrong !! please enter valid input")
                print("\n")

        elif(user_choice == "2"):
            id_= id_input()
            result = delete_expense(expenses, id_)

            if (result == True):
                save_expenses(expenses, filename)
                print("Expense deleted successfully \n")
            else:
                print("id not found!!")
        
        elif(user_choice == "3"):
            id_= id_input()
            result = find_expense_by_id(expenses, id_)
            for key, value in result.items():
                print(f"{key} : {value}")
            print("\n")

        
        elif(user_choice == "4"):
            result = calculate_total(expenses)
            print(result)
            print("\n")
        
        elif(user_choice == "5"):
            print("Exiting.....")
            break
        else:
            print("PLEASE ENTER ONLY VALID CHOICE !!")

if __name__ == "__main__":
    main()