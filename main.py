from cryptography.fernet import Fernet
running = True
while running:
    with open('Key.txt', 'r') as f:
        data = f.read()
    choice = input("want send or decrypt (1 or 2)")
    if choice == "1":
        print(Fernet(data).encrypt(input("Enter what do encode: ").encode()))
    if choice == "2":

        decMessage = Fernet(data).decrypt(input("enterMessgae")).decode()

        print("decrypted string: ", decMessage)
    
