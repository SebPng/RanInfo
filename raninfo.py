#!/usr/bin/env python3
# 💚 ℝ𝕒𝕟𝕀𝕟𝕗𝕠 𝕧1 💚

import random
import string
import argparse
import sys

# Warning when generating sensitive info
WARNING_MSG = "\033[91m/If you lose this info it is gone forever/\033[0m"

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

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_password(length=12):
    return ''.join(random.choice(chars) for _ in range(length))

def print_help():
    help_text = f"""
💚 ℝ𝕒𝕟𝕀𝕟𝕗𝕠 𝕧1 💚

Usage: raninfo [OPTIONS]

Options:
  --name            Generate a fake name
  --pass            Generate a random password
  --length [NUM]    Specify password length (default 12)
  --help            Show this help message

Examples:
  raninfo --name                  # Generates only a fake name
  raninfo --pass                  # Generates only a password of default length
  raninfo --pass --length 20      # Generates password of length 20
  raninfo --name --pass --length 16   # Generates both name and password
"""
    print(help_text)

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--name', action='store_true', help="Generate a fake name")
    parser.add_argument('--pass', dest='passwd', action='store_true', help="Generate a random password")
    parser.add_argument('--length', type=int, default=12, help="Password length (default 12)")
    parser.add_argument('--help', action='store_true', help="Show help message")

    args = parser.parse_args()

    if args.help:
        print_help()
        sys.exit(0)

    if args.name:
        print("Name:", generate_name())
    if args.passwd:
        print("Password:", generate_password(args.length))
        print(WARNING_MSG)
    if not (args.name or args.passwd or args.help):
        # Default behavior: generate both
        print("Name:", generate_name())
        print("Password:", generate_password(args.length))
        print(WARNING_MSG)

if __name__ == "__main__":
    main()