#asking for name
def ask_for_name():
    input_name = input("What is your name? ")
    return input_name

#printing greeting
def greeting(user):
    print(f'Hello, {user}')

user_name_input = ask_for_name()
greeting(user_name_input)

def main():
    user_name_input = ask_for_name()
greeting(user_name_input)

main()