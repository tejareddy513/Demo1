import random
import string
#random function is used for genarating random password
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation
# combinations of all these 3 things
    all_chars = letters + digits + specials
  # Choose a random password length between 8 and 15
    length = random.randint(8, 15)
  # Ensure at least one digit and one special character
    password = [
        random.choice(digits),
        random.choice(specials)
    ]
  # Fill the rest of the password means excepting the reamaning charcters
    password += random.choices(all_chars, k=length - 2)
  # Shuffle to avoid predictable placement means  shiffing the places while  genarating the password
    random.shuffle(password)
    return ''.join(password)

# Generate and print a password
print("Generated Password:", generate_password())
