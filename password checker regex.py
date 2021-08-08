import re

pattern_to_search=re.compile(r"([A-Za-z0-9$%#@]{8,}[0-9])")

password=input('user please enter a password ')

check=pattern_to_search.fullmatch(password)
print(check)

