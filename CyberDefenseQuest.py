import hashlib
import time
import random

print("Welcome, Cyber Agent! Your mission is to secure sensitive data using the CIA Triad principles: Confidentiality, Integrity, and Availability.")

# Stage 1: Confidentiality
print("\nStage 1: Confidentiality")
print("Imagine you're guarding a treasure chest. The key to this chest is your password. If the key is too simple, a thief can easily copy it and steal the treasure!")

# Generate a random strong password
strong_password = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()", k=10))
weak_passwords = ["123456", "password", "AgentX!#42", "X!Z9$7@k8"]
password_options = weak_passwords + [strong_password]
random.shuffle(password_options)

print("A hacker is trying to steal your password. Choose the strongest one:")
for i, pw in enumerate(password_options, 1):
    print(f"{i}. {pw}")

# Handle invalid input
while True:
    password = input("Select the number of your password choice: ")
    if password.isdigit() and 1 <= int(password) <= len(password_options):
        if password_options[int(password) - 1] == strong_password:
            print("✅ Great choice! You protected the data from being stolen.")
        else:
            print("❌ The hacker broke in! Try again.")
            exit()
        break
    else:
        print("❌ Invalid input! Please enter a valid number.")

# Pause to simulate mission progress
time.sleep(1)

# Stage 2: Integrity
print("\nStage 2: Integrity")
print("You’ve stored a top-secret blueprint, but a hacker wants to tamper with it. Imagine a wax seal on a letter — if the seal is broken, you know someone has meddled with it. Here, hashes are your digital seals!")
print("The hacker is trying to modify a critical file. You must verify which one is untouched!")

# Simulate original data and hash
original_data = "TopSecretFileContents"
original_hash = hashlib.sha256(original_data.encode()).hexdigest()

# Display hash without revealing data
print(f"Original file hash: {original_hash}")

# Simulate two fake files
fake_data1 = "TopSecretFileCont3nts"
fake_data2 = "T0pSecretF1leContents"
files = [("File A", original_data), ("File B", fake_data1), ("File C", fake_data2)]
random.shuffle(files)

# Display file options
print("\nThree files are presented. One is original, the others are altered!")
for i, (name, data) in enumerate(files, 1):
    print(f"{i}. {name} - {hashlib.sha256(data.encode()).hexdigest()}")

# Handle invalid input
while True:
    choice = input("Select the file number that is unmodified: ")
    if choice.isdigit() and 1 <= int(choice) <= len(files):
        if files[int(choice) - 1][1] == original_data:
            print("✅ Perfect! You identified the original file.")
        else:
            print("❌ Data tampered! Hackers misled you. Try again.")
            exit()
        break
    else:
        print("❌ Invalid input! Please enter a valid number.")

# Pause for immersion
time.sleep(1)

# Stage 3: Availability
print("\nStage 3: Availability")
print("The server is under DDoS attack! Imagine a store with a huge crowd blocking the entrance — no one can get in to buy anything. Solve this puzzle to clear the crowd and keep the store (server) open!")

math_puzzles = [
    ("(12 * 3) + (18 / 2) - 4", "29"),
    ("(8 * 4) - (10 / 2) + 6", "30"),
    ("(15 / 3) + (7 * 2) - 5", "14")
]

puzzle_question, puzzle_answer = random.choice(math_puzzles)

answer = input(f"What is {puzzle_question}? (Quick!): ")

if answer == puzzle_answer:
    print("🎉 Mission Complete! You successfully defended the data using the CIA Triad.")
    print("🏅 Congratulations, Elite Cyber Agent!")
else:
    print("❌ Wrong answer! The server crashed. Hackers won this round. Try again.")
    exit()

# Final message
print("\n✅ You've completed the advanced CIA Triad practical. Great job!")
