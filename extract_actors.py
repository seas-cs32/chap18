### chap18/extract_actors.py -- Written by ChatGPT
import re

def extract_actors(input_string):
    # Regular expression to match actor names
    actor_pattern = re.compile(r'([A-Z][a-z]+(?: [A-Z][a-z]+)+)')
    
    # Find all matches
    actors = actor_pattern.findall(input_string)
    
    # Join the actors with a semicolon
    result = '; '.join(actors)
    
    return result

# Example usage
input_text = "Jane Tsentas and Cleo O'Hara starred in Evil Come Evil Go"
# input_text = "Aden Young and Marshall Napier starred in Shotgun Wedding"
print(extract_actors(input_text))
