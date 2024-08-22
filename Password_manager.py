from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()

def load_key():
    file = open("key.key", "rb")#rb= read in byte
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")            
            print('User:', user + 'Password:',fer.decrypt(passw.encode()).decode() )

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f: # 'a' helps to add something at the end of the file and creates a new file if the entered file does not exists.   
    # with helps to automatically close the file, if we dont use with we can also write as:
    # file = open('password.txt', 'a')
    # file.close()  if  we use this we should manually close the file.
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add new password or view existing ones (view, add), press q to quit ? ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == "add":
        add()

