import random
import string

def randomize(chars, plain_text ,cipher_text, key):
  for letter in plain_text:
    num = random.randint(0, len(chars) - 1)
    cipher_text += chars[num]
    key.append(chars.index(letter))
  return cipher_text, key

def decrypt(chars, key, decrypt_text):
  for num in key:
    decrypt_text += chars[num]
  return decrypt_text

def main():
  chars = " " + string.punctuation + string.digits + string.ascii_letters
  chars = list(chars)

  plain_text = input("Enter a message to encrypt: ")
  cipher_text = ""
  decrypt_text = ""
  key = []

  print(chars)

  cipher_text, key = randomize(chars, plain_text, cipher_text, key)
  print(f'original message: {plain_text}')
  print(f'encrypted message: {cipher_text}')
  print(f'key: ', end='')
  for char in key:
    print(f'{char}', sep=' ', end='')
  print()
  print(f'decrypted text: {decrypt(chars, key, decrypt_text)}')

if __name__ == "__main__":
  main()