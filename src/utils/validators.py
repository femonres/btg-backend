import re


def is_valid_email(email: str) -> bool:
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None

def is_valid_phone_number(phone: str) -> bool:
    regex = r'^\+?[1-9]\d{1,14}$'
    return re.match(regex, phone) is not None