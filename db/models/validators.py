import re
from datetime import datetime

def email(email: str) -> bool:
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

# Function to validate photo URL
def url(url: str) -> bool:
    url_regex = r"^(https?://)?([a-z0-9-]+\.)+[a-z0-9-]+(/[a-z0-9-./?%&=]*)?$"
    return re.match(url_regex, url) is not None

# Function to calculate age from birthday
def age(birthday: datetime) -> int:
    today = datetime.utcnow()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

# Function to validate phone number
def phone(phone: str) -> bool:
    phone_regex = r"^\+?[1-9]\d{1,14}$"
    return re.match(phone_regex, phone) is not None