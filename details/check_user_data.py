import re

phone_pattern = r"^\+998\d{9}$"

def validate_phone(phone: str) -> bool:
    return bool(re.match(phone_pattern, phone))


name_pattern = r"^(?:[A-Z][a-z]{1,49}|[А-ЯЁ][а-яё]{1,49})(?:\s(?:[A-Z][a-z]{1,49}|[А-ЯЁ][а-яё]{1,49}))*$"

def validate_name(name: str) -> bool:
    return bool(re.match(name_pattern, name))

