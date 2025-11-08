
# Парсер команд
def parse_input(user_input): 
    cmd, *args = user_input.split() 
    cmd = cmd.strip().lower() 
    return cmd, *args

# Декоратор для обробки помилок введення у функціях додавання контактів
def input_error(func): 
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return  "❌Give me name and phone please"
        except KeyError :
            return "❌This contact does not exist"
        except IndexError :
             return ("❌ Enter user name")
        except Exception as e: 
            return f"An error occurred: {e}" 
    return inner


# Функція для додавання контакту до словника контактів
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone 
    return f" ✔ Contact '{name} {phone}' has been added to list"  

#Функція для зміни номера телефону існуючого контакту
@input_error
def change_contact(args, contacts): 
    name, new_phone = args 
    if name not in contacts:
        raise KeyError
    contacts[name] = new_phone 
    return f" ✔ Contact '{name}' has been updated with new phone number'{new_phone}'" 


#Функція для показу номера телефону існуючого контакту
@input_error
def show_phone(args, contacts):
    name = args[0] 
    return f"✔ Contact '{name}' has phone number '{contacts[name]}'"

#Функція для показу всіх контактів у словнику
@input_error
def show_all(contacts):
    if not contacts:
        return "❌ No contacts stored"
    result_lines = ["All contacts:"]
    for name, phone in contacts.items():
        result_lines.append(f"{name}: {phone}")
    return "\n".join(result_lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input: # Перевіряємо чи користувач ввів порожній рядок
                continue # Якщо порожній, пропускаємо ітерацію та запитуємо команду знову
        command, *args = parse_input(user_input) 
        print(f"Command: {command} Arguments: {args}") 
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
           print(add_contact(args, contacts))  
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))       
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
