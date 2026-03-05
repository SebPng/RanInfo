#!/usr/bin/env python3
import random
import string
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Fake Name & Password Generator")
    parser.add_argument('--name', action='store_true', help="Generate a fake name")
    parser.add_argument('--pass', dest='passwd', action='store_true', help="Generate a random password")
    parser.add_argument('--length', type=int, default=12, help="Password length (default 12)")

    args = parser.parse_args()

    if args.name:
        print("Name:", generate_name())
    if args.passwd:
        print("Password:", generate_password(args.length))
    if not (args.name or args.passwd):
        print("Name:", generate_name())
        print("Password:", generate_password(args.length))

if __name__ == "__main__":
    main()