### chap18/balance_parentheses.py -- Written by ChatGPT

def balance_parentheses(s):
    # Count open and close parentheses
    open_count = s.count('(')
    close_count = s.count(')')
    
    # Calculate the difference to balance
    to_add = open_count - close_count
    
    # Append the necessary closing parentheses
    balanced = s + ')' * to_add
    return balanced


def main():
    # Example input that `balance_parentheses` answers correctly
    input_parentheses = "(((((((((("
    result = balance_parentheses(input_parentheses)
    print(f'Input:  {input_parentheses}')
    print(f'Output: {result}')
    
    # Example input that `balance_parentheses` answers incorrectly
    input_parentheses = "()())"
    result = balance_parentheses(input_parentheses)
    print(f'Input:  {input_parentheses}')
    print(f'Output: {result}')

if __name__ == '__main__':
    main()
