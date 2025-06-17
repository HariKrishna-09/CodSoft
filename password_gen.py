import random
import string

def gen(leng):
    if leng < 4:
        return "Password length should be at least 4"

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower+upper+digits+symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    password = password+random.choices(all_chars,k=leng-4)
    random.shuffle(password)
    return ''.join(password)


le = int(input("Enter the length of Password you require: "))
print("The Generated Password:", gen(le))
