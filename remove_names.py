### chap18/remove_names.py -- Written by ChatGPT
import re

def remove_names_from_line(line):
    # Pattern to find capitalized words followed by 'and' or 'starred'
    # This regex assumes that names are always before 'starred' and start with capital letters
    pattern = r'\b[A-Z][a-z]*\s(?:and\s)?[A-Z][a-z]*\s(starred)'

    # Replace the names and 'and' if it appears with 'starred'
    # This keeps the structure of the sentence but removes the names
    clean_line = re.sub(pattern, r'\1', line)

    return clean_line

# Example usage
line = "Carey Mulligan and Joel Edgerton starred in The Great Gatsby"
print(remove_names_from_line(line))