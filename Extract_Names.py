import re

simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. Ruth and Peter, their parents, 
have 3 kids. """

names = re.findall(r"[A-Z][a-z]+,?\s+", simple_string)

print(names)
