

def my_function(string1, string2):
    print(string1)
    print(string2)


def print_default_arguments(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)


def print_keyword_arguments(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)


def print_infinit_arguments(*people):
    for person in people:
        print(person)


def do_math(num1, num2):
    return num1 + num2


def print_if(string, condition):
    if condition == True:
        print(string)


def print_for(list):
    for item in list:
        print("This person name is",item)


def print_while(current_value):
    run = True
    while run:
        if current_value == 100:
            print("Instalação concluída.")
            run = False
        else:
            print("Instalando", current_value, "%...")
            current_value +=1

