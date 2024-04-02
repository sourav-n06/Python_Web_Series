"""
4. Write a regular expression to validate a phone number.
    """

import re

def validate_indian_phone_number(phone_number):
    # Pattern for Indian phone numbers
    pattern = r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
    return re.match(pattern, phone_number) is not None

# Example usage:
phone_number = input("Enter Indian phone number: ")
if validate_indian_phone_number(phone_number):
    print("Valid Indian phone number")
else:
    print("Invalid Indian phone number")
