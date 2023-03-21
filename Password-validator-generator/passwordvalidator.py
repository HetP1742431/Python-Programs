from string import digits


def validate(password):
    list_password = list(password)
    if " " in list_password or "@" in list_password or "#" in list_password:
        return("Invalid")
    elif len(list_password) < 8:
        return("Invalid")
    else:
        a,b,c,d = 0,0,0,0
        special_chars = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
        for i in range(len(list_password)):
            if list_password[i].isupper():
                a = a + 1
            elif list_password[i].islower():
                b = b + 1
            elif list_password[i].isdigit():
                c = c + 1
            elif list_password[i] in special_chars:
                d = d + 1
        if a>0 and b>0 and c>0 and d>0:
            return("Secure")
        else:
            return("Insecure")



def generate(n):
    import random
    import string 
    if n < 8:
        n = 8
    upper_list = list(string.ascii_uppercase)
    lower_list = list(string.ascii_lowercase)
    digits_list = list(string.digits)
    special_chars = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    random_list = []
    for i in range(n):
        x = random.choice(upper_list + lower_list + digits_list + special_chars)
        random_list.append(x)
    random_list[0] = random.choice(upper_list)
    random_list[1] = random.choice(lower_list)
    random_list[2] = random.choice(digits_list)
    random_list[3] = random.choice(special_chars)
    random.shuffle(random_list)
    password = ''.join(random_list)
    
    return password

password = input("Enter the password you want to test: ")
print(validate(password))

n = int(input("Enter the size of password you want to generate: "))
print(generate(n))
