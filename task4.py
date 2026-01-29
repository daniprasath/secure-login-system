import hashlib
import os

FILE_NAME = "credentials.txt"

# Hashing function
def encrypt(password):
    return hashlib.md5(password.encode()).hexdigest()

# Register function
def register_user():
    username = input("Create username: ")
    password = input("Create password: ")

    encrypted_pass = encrypt(password)

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                stored_user = line.split(",")[0]
                if stored_user == username:
                    print("❌ Username already exists")
                    return

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + encrypted_pass + "\n")

    print("✅ User registered successfully")

# Login function
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    encrypted_pass = encrypt(password)

    if not os.path.exists(FILE_NAME):
        print("❌ No users found. Please register first.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")
            if user == username and pwd == encrypted_pass:
                print("🔓 Login successful")
                return

    print("❌ Invalid username or password")

# Menu-driven program
while True:
    print("\n--- Secure Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("👋 Program exited")
        break
    else:
        print("❌ Invalid option")