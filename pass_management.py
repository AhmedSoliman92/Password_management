import pickle
import pyperclip
import string
import random

dictionary= {}
letters= string.ascii_letters
numbers= string.digits
punctuations= string.punctuation

def generate():
    length= input("Please enter the length of password (defualt:11): ")
    password= f'{letters}{numbers}{punctuations}'
    password=list(password)
    random.shuffle(password)
    password= random.choices(password, k= int(length))
    password= ''.join(password)
    return password

while True:
    user_id=   input("Please enter '1' to sign up or 2 to exit, or enter your username if you've already signed: ")
    
    with open("pass_man.txt", "br") as filewrite:
        dictionary= pickle.load(filewrite)
    if user_id=="2":
        break
    if user_id== "1":
        email=   input("Enter your user id: ")
        with open("usernames.txt", "a") as f:
            f.write(email)

        password= input("Enter the password(if you want to suggest password, press '1'): ")
        if password=='1':
            password= generate()
            print(f"Your password is: {password}")
        with open("pass.txt","a") as a:
            a.write(password)
    with open("usernames.txt","r") as fr:
        store_email= fr.read()

    if user_id == store_email:
        password2= input("Enter your password: ")
        with open("pass.txt","r") as ar:
            store_pass= ar.read()
        
        if password2 == store_pass:
            conf= input("To know your password press '1' to save your password '2': ")
            if "2" in conf:
                account = input("Enter your account name: ")
                acc_pass = input("Enter your account password: ")
                confirmation = input("Would you like to save it (y/n): ")
                if "y" in confirmation:
                    dictionary[account]= acc_pass

                    with open("pass_man.txt", "bw") as readfile:
                        dictionary= pickle.dump(dictionary, readfile, protocol= 2)
                    print(f"Done! your {account}'s password has been saved.")
                else:
                    print("Your data has not saved...")
            
            if "1" in conf:
                email1= input("Which account's password you want to know: ")
                with open("pass_man.txt", "br") as file:
                    dictionary= pickle.load(file)
                if email1 in dictionary:
                    print(f"Your {email1}'s password is {dictionary[email1]}")
                    print("Your password has been saved to your clipboard")
                    pyperclip.copy(dictionary[email1])
                else:
                    print("This account is not found...")