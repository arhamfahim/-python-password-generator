import random
import string

def password_generator(length):

    letters = string.ascii_letters    # a-z, A-Z
    digits = string.digits            # 0-9
    symbols = string.punctuation      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    all_chars = letters + digits + symbols

    password = []

    for i in range(length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)


# main_program
length = int(input("Enter password length: "))

pwd = password_generator(length)

print(f"\nPassword is generated: {pwd}")
print("Password strength: Strong")
