import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!
# text = "John Cena Anya Taylor-Joy D'Angelo"
name = r"^(?!.*\s{3,}).*[A-Z][a-zA-Z-' ]*$"
name_regex = re.compile(name)
# match = name_regex.fullmatch(text)
# print(match)


phone_number = r"\(\d{3}\) \d{3}-\d{4}|\d{10}|\d{3}-\d{3}-\d{4}"
phone_regex = re.compile(phone_number)

email_address = r"\b(?![0-9])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]+\b"
email_regex = re.compile(email_address)
