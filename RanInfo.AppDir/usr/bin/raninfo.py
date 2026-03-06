#!/usr/bin/env python3
import random
import string
import argparse
import re

HEADER = "\033[92mℝ𝕒𝕟𝕀𝕟𝕗𝕠 𝕧𝟙\033[0m"

first_names = [
    "Alex", "Sam", "Jamie", "Taylor", "Jordan", "Morgan", "Casey", "Riley", "Cameron", "Avery",
    "Quinn", "Reese", "Dakota", "Emerson", "Parker", "Harper", "Skyler", "Rowan", "Sawyer", "Finley",
    "Blake", "Elliot", "Charlie", "Hayden", "Sage", "Kendall", "Payton", "Alexis", "Logan", "Dakota",
    "Sydney", "Carter", "Hunter", "Jesse", "Adrian", "Taylor", "Lane", "Phoenix", "Jordan", "River",
    "Morgan", "Tatum", "Kai", "Shawn", "Reagan", "Casey", "Drew", "Peyton", "Bailey", "Emery"
]

last_names = [
    "Smith", "Johnson", "Lee", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
    "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark",
    "Rodriguez", "Lewis", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Torres",
    "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell",
    "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Collins"
]

chars = string.ascii_letters + string.digits + "!@#$%^&*"

CHANGELOG = [
    "v1.0 - Release with name & password generator",
    "v1.0.1 - Added a warning when generating passwords",
    "v1.1 - Added help menu"
    "v2.0 - Added Fake mail generator, number of names and passwords to generate, password strength checker and this very menu.",
]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_password(length=12):
    return ''.join(random.choice(chars) for _ in range(length))

def generate_email():
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    return f"{username}@fgm.fk"

def password_strength(password):
    length = len(password)
    upper = re.search(r'[A-Z]', password) is not None
    lower = re.search(r'[a-z]', password) is not None
    digit = re.search(r'\d', password) is not None
    symbol = re.search(r'[!@#$%^&*]', password) is not None
    score = sum([length>=8, upper, lower, digit, symbol])
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"

def main():
    print(HEADER)
    parser = argparse.ArgumentParser(description="ℝ𝕒𝕟𝕀𝕟𝕗𝕠 - Fake Name & Password Tool")
    parser.add_argument('--name', action='store_true', help="Generate a fake name")
    parser.add_argument('--pass', dest='passwd', action='store_true', help="Generate a random password")
    parser.add_argument('--length', type=int, default=12, help="Password length (default 12)")
    parser.add_argument('--email', action='store_true', help="Generate a random email ending with @fgm.fk")
    parser.add_argument('--strength', type=str, help="Check password strength")
    parser.add_argument('--multi', type=int, default=1, help="Generate multiple entries")
    parser.add_argument('--changelog', '-c', action='store_true', help="Show the change log")

    args = parser.parse_args()

    if args.changelog:
        print("Change Log:")
        for line in CHANGELOG:
            print("-", line)
        return

    for _ in range(args.multi):
        if args.strength:
            print("Password Strength:", password_strength(args.strength))
        else:
            if args.name:
                print("Name:", generate_name())
            if args.passwd:
                print("Password:", generate_password(args.length))
                print("\033[91m/If you lose this info it is gone forever/\033[0m")
            if args.email:
                print("Email:", generate_email())
            if not (args.name or args.passwd or args.email):
                print("Name:", generate_name())
                print("Password:", generate_password(args.length))
                print("\033[91m/If you lose this info it is gone forever/\033[0m")

if __name__ == "__main__":
    main()