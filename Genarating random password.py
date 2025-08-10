import random
#random function is used for genarating random password
import string
# the string function is used to create a string type of password this will be combination of characters

def genarate_randompassword():
  letters = string.ascii_letters   #azAz
  digits = string.digits           #0-9
  special = string.punctuation     #@!#$

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
#We subtract 2 because we already added: because we already added the special char and digit soo it wont take the next
  password += random.choices(all_chars, k=length - 2)
# Shuffle to avoid predictable placement means  shiffing the places while  genarating the password
  random.shuffle(password)
  return ''.join(password)

# Generate and print a password
print("Generated Password:", generate_password())
