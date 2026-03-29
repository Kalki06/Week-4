def add_expense(expenses):
    while True:
        try:
            ex_id = int(input("Enter the id : "))
            ex_amount = int(input("Enter the amount : "))
            if(ex_amount > 0):
                break
        except ValueError:
            print("Pleaser enter only integer value and amount should be positive")
            continue
    
    while True:
        ex_category = input("Enter the category of the expense : ")
        ex_category = ex_category.strip()
        if(ex_category == ""):
            print("Category can't be empty")
            continue
        else:
            break
    
    ex_category = ex_category.lower()

    for expense in expenses:
        if expense['id'] == ex_id:
            print("Id must pe unique try differesnt id \n")
            return False
    
    new_expense = {
        'id' : ex_id,
        'amount' : ex_amount,
        'category' : ex_category
    }

    expenses.append(new_expense)

    return True

def delete_expense(expenses):
    while True:
        try:
            ex_id = int(input("Enter the id : "))
            break
        except ValueError:
            print("Enter id correctly \n")
            continue
    
    for i in range(len(expenses)):
        if(expenses[i]['id'] == ex_id):
            del expenses[i]
            return True

    return False

def total_expenses(expenses):
    total = 0
    
    for expense in expenses:
        total += expense['amount']
    
    return total

def search_by_category(expenses):
    found = False

    while True:
        category = input("Enter the category you want to search in : ")
        category_clean = category.strip()
        category_lower = category_clean.lower()    
        if(category_lower != ""):
            break

    if(len(expenses) != 0 ):
        for expense in expenses:
            if(expense['category'] == category_lower):
                print(f"Id : {expense['id']}")
                print(f"Amount : {expense['amount']}")
                print(f"Category : {expense['category']}\n")

                found = True
    
    if found == False:
        print(f"Nothing found in '{category_lower}' category \n")
    

def save_to_file(expenses, filename):
    try:
        with open (filename, "w") as file:
            for expense in expenses:
                line = f"{expense['id']},{expense['amount']},{expense['category']}\n"
                file.write(line)
    except FileNotFoundError:
        print(f"There is no file with '{filename}' this file name ")

def load_from_file(filename):
    expenses = []
    try:
        with open (filename, "r") as file:
            for line in file:
                clean_line = line.strip()
                parts = clean_line.split(",")

                if(len(parts) != 3):
                    continue

                try:
                    if(len(parts[2]) != 0):
                        file_exp_id = int(parts[0])
                        file_exp_amount = int(parts[1])
                        file_exp_category = parts[2].strip()
                except ValueError:
                    continue
                
                file_expense = {
                    'id' : file_exp_id,
                    'amount' : file_exp_amount,
                    'category' : file_exp_category
                }

                expenses.append(file_expense)

            return expenses
                
    except FileNotFoundError:
        print("File not found !!")

def main():
    file_name = input("Enter the file name in txt format for example ' expamle.txt' : ")

    expenses = load_from_file(file_name)

    while True:
        print("Enter 1 for adding expense. ")
        print("Enter 2 for deleting expense. ")
        print("Enter 3 for searching expense by category. ")
        print("Enter 4 for total. ")
        print("Enter 5 for exiting. \n")
        
        while True:
            try:
                user_choice = int(input("Enter the choice : "))
                break
            except ValueError:
                print("Enter the number only !!")
                continue
        
        if(user_choice == 1):
            result = add_expense(expenses)
            if(result == True):
                save_to_file(expenses, file_name)
                print("Expense is saved in the file. \n")
        
        elif(user_choice == 2):
            result = delete_expense(expenses)
            if(result == True):
                save_to_file(expenses, file_name)
                print("Expense deleted successfully. \n")
            else:
                print("Expense not found !!")

        elif(user_choice == 3):
            search_by_category(expenses)
        
        elif(user_choice == 4):
            result = total_expenses(expenses)
            print(f"You have spend total {result} \n")
        
        elif(user_choice == 5):
            print("Exiting ......")
            break
        
        else:
            continue

if __name__ == "__main__" :
    main()