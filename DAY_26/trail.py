def update_input():
    while True:
        try:
            new_id = int(input("Enter the id of expense you want to change : "))
            break
        except ValueError:
            continue
    
    while True :
        choice_amount = input("Do you want to update amount? (y/n) : ")
        if(choice_amount == 'y' or choice_amount == 'n'):
            break
        else:
            continue
    
    if(choice_amount == 'y'):
        while True:
            try:
                new_amount = int(input("Enter the amount : "))
                if (new_amount > 0):
                    break
            except ValueError:
                continue
    else:
        new_amount = None
    
    while True :
        choice_category = input("Do you want to update category? (y/n) : ")
        if(choice_category == 'y' or choice_category == 'n'):
            break
        else:
            continue
    
    if(choice_category == 'y'):
        while True:
            input_category = input("Enter the category : ")
            new_category = input_category.strip()
            if(new_category != ""):
                break
    else:
        new_category = None
    
    return new_id, new_amount, new_category

print(update_input())