# user_input = input("Enter your text : ")

# with open ("notes.txt", "w") as file:
#     file.write("Hello World \n")
#     file.write("Python file handling \n")
#     file.write(f"User input : {user_input} \n")

# with open ("notes.txt", "r") as file:
#     read_file = file.read()
#     print(read_file)

# with open ("notes.txt", "r") as file:
#     count = 0
#     for i in file:
#         count+=1
#     print(count)




with open ("notes.txt", "a") as file:
    while True:
        print("Type 'exit' only to exit or write what you want to add in the notes")
        user_input = input("Type Here : ")

        if(user_input == "exit"):
            print("Exiting....")
            break
        else:
            file.write(f"{user_input} \n")

with open ("notes.txt", "r") as file:
    read_file = file.read()
    print(read_file)