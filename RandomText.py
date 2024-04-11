import random
import string

def generate_random_text(length):
  letters = string.ascii_letters + string.digits + string.punctuation
  random_text = ''.join(random.choice(letters) for i in range(length))
  return random_text