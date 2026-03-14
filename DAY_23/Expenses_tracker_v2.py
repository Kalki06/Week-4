
def add_expense(expenses):
    try:
        exp_id = int(input("Enter the new id : "))
        exp_amount = int(input("Enter the amount : "))
    except ValueError:
        print("Invalid input")
        return False
    
    exp_category = input("Enter the category : ")

    for expense in expenses:
        if(expense['id'] == exp_id):
            print("Id already exists !!")
            return False

    if exp_amount <= 0:
        print("Amount must be positive !!")
        return False
    
    user_exp = {
        'id' : exp_id,
        'amount' : exp_amount,
        'category' : exp_category
    }
    expenses.append(user_exp)
    return True


def delete_expense(expenses):
    try:
        exp_id = int(input("Enter the expenses id : "))
    except ValueError:
        print("Invalid input")
        return
    
    for expense in expenses:
        if(expense['id'] == exp_id):
            expenses.remove(expense)
            return True
        break
    
    return False
    
    

def search_category(expenses):

    found = False
    exp_category = input("Enter the category : ")
    
    for expense in expenses:
        if(expense['category'] == exp_category):
            print(f"Id : {expense['id']}")
            print(f"Amount : {expense['amount']}")
            print(f"Category : {expense['category']}\n")
        found = True
    
    if(found == False):
        print("No expenses found in this category")
    return 

def show_all(expenses):
    if(len(expenses) != 0):
        for expense in expenses:
            print(f"Id : {expense['id']}")
            print(f"Amount : {expense['amount']}")
            print(f"Category : {expense['category']}\n")
        return
    
    else:
        print("No expenses recorded yet.\n")

def total_expense(expenses):
    total = 0
    if(len(expenses) == 0):
        print(total)
        print("No expenses recorded yet.\n")
        return
    else:
        for expense in expenses:
            total += expense['amount']
        print(f"Total amount you spend is {total}\n")
        

def save_to_file(expenses):
    with open ("expenses.txt", "w") as file:
        for expense in expenses:
            line = f"{expense['id']},{expense['amount']},{expense['category']}\n"
            file.write(line)
    print("Data is saved.")


def load_from_file():
    new_expenses = []
    try:
        with open ("expenses.txt", "r") as file:
            for line in file:
                clean_line = line.strip()
                if(len(clean_line) == 0):
                    continue
                
                parts = clean_line.split(",")
                if(len(parts)!=3):
                    continue
                
                try:
                    exp_id = int(parts[0])
                    exp_amount = int(parts[1])
                    exp_category = parts[2]
                    user_expense = {
                        'id' : exp_id,
                        'amount' : exp_amount,
                        'category' : exp_category
                    }

                    new_expenses.append(user_expense)
                
                except ValueError:
                    continue
    except FileNotFoundError:
        return new_expenses
    
    return new_expenses

def main():
    expenses = load_from_file()

    while True:
        print("Enter 1 for add")
        print("Enter 2 for delete")
        print("Enter 3 for search")
        print("Enter 4 for to show all")
        print("Enter 5 for total")
        print("Enter 6 for exit")
        print("\n")

        user_choice = input("Enter your choice here : ")
        print("\n")

        if(user_choice == "1"):
            result = add_expense(expenses)
            if(result == True):
                save_to_file(expenses)
                print("\n")

        elif(user_choice == "2"):
            result = delete_expense(expenses)
            if (result == True):
                save_to_file(expenses)
                print("\n")
            else:
                print("id not found!!")
        
        elif(user_choice == "3"):
            search_category(expenses)
        
        elif(user_choice == "4"):
            show_all(expenses)
        
        elif(user_choice == "5"):
            total_expense(expenses)

        elif(user_choice == "6"):
            print("Exiting.....")
            break
        else:
            print("PLEASE ENTER ONLY VALID CHOICE !!")

if __name__ == "__main__":
    main()