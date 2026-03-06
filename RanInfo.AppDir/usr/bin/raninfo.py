#!/usr/bin/env python3
import random
import string
import argparse
import sys

# 🟢 HEADER
print("\033[1;32mℝ𝕒𝕟𝕀𝕟𝕗𝕠 v1.1\033[0m\n")

# --- Name and Password Data ---
first_names = [
    "Alex", "Sam", "Jamie", "Taylor", "Jordan", "Morgan", "Casey", "Riley", "Cameron", "Avery",
    "Quinn", "Reese", "Dakota", "Emerson", "Parker", "Harper", "Skyler", "Rowan", "Sawyer", "Finley",
    "Blake", "Elliot", "Charlie", "Hayden", "Sage", "Kendall", "Payton", "Alexis", "Logan", "Sydney",
    "Carter", "Hunter", "Jesse", "Adrian", "Taylor", "Lane", "Phoenix", "Jordan", "River", "Morgan",
    "Tatum", "Kai", "Shawn", "Reagan", "Casey", "Drew", "Peyton", "Bailey", "Emery", "Micah"
]

last_names = [
    "Smith", "Johnson", "Lee", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
    "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark",
    "Rodriguez", "Lewis", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Torres",
    "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell",
    "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Collins"
]

chars = string.ascii_letters + string.digits + "!@#$%^&*"

# --- Changelog ---
changelog_text = """
v1.1 - New Features:
- --changelog command
- Automatic PATH setup instructions
- Generate multiple names/passwords/emails with --count
- Password strength meter
- Random email generator ending with @fgm.fk
"""

# --- Functions ---
def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_password(length=12):
    pwd = ''.join(random.choice(chars) for _ in range(length))
    strength = password_strength(pwd)
    return pwd, strength

def password_strength(pwd):
    score = 0
    if any(c.islower() for c in pwd):
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*" for c in pwd):
        score += 1
    if len(pwd) >= 12:
        score += 1
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def generate_email(name):
    username = name.lower().replace(" ", ".")
    return f"{username}@fgm.fk"

def print_help():
    help_text = """
Usage: raninfo [OPTIONS]

Options:
  --name            Generate a fake name
  --pass            Generate a random password
  --email           Generate a random email
  --length N        Password length (default 12)
  --count N         Generate multiple names/passwords/emails
  --changelog       Show version history
  --help            Show this help message
"""
    print(help_text)

# --- Main ---
def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--name', action='store_true')
    parser.add_argument('--pass', dest='passwd', action='store_true')
    parser.add_argument('--email', action='store_true')
    parser.add_argument('--length', type=int, default=12)
    parser.add_argument('--count', type=int, default=1)
    parser.add_argument('--changelog', action='store_true')
    parser.add_argument('--help', action='store_true')
    args = parser.parse_args()

    if args.help:
        print_help()
        sys.exit(0)

    if args.changelog:
        print(changelog_text)
        sys.exit(0)

    for _ in range(args.count):
        if args.name or not (args.passwd or args.email):
            name = generate_name()
            print("Name:", name)
        if args.passwd or not (args.name or args.email):
            pwd, strength = generate_password(args.length)
            print(f"Password: {pwd} ({strength})")
            print("\033[1;31m/If you lose this info it is gone forever/\033[0m")
        if args.email or not (args.name or args.passwd):
            email = generate_email(name)
            print("Email:", email)
        print("")

if __name__ == "__main__":
    main()