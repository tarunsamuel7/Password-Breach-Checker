# Password Breach Checker

![Language](https://img.shields.io/badge/Language-Python-blue.svg)

## Overview

A Python program to check if passwords have been compromised using the haveibeenpwned.com API.

## Features

- Utilizes the haveibeenpwned.com API to check for password breaches.
- Hashes passwords using the SHA-1 algorithm.
- Splits the hashed password, takes the first 5 characters, and queries the API for all hashed passwords that start with these initial 5 characters.
- Checks if hashed password is within the retrieved list and displays the count of breaches for that password.

## Getting Started

1. Clone the repository.
2. Install dependencies: `pip install requests`
3. Run the program: `python password_breach_checker.py path/to/passwords.txt`
