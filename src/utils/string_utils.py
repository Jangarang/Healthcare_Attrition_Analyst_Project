import re 

def pascal_to_snake(name):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', name).lower()

def snake_to_pascal(name):
    return re.sub(r'(?:^|_)(\w)', lambda m: m.group(1).upper(), name)