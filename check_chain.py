### chap18/check_chain.py
import re
import sys

# Terminal colors
reset = '\033[0m'
red = '\033[31m'
blue = '\033[34m'

def increment(d, key):
    '''Increment the count for key `key` in dictionary `d`'''
    if key in d:
        if d[key] > 1:
            print(f'Actor "{red}{key}{reset}" occurs too many times')
            sys.exit()
        else:
            d[key] += 1
    else:
        d[key] = 1

def check(lines):
    '''Make sure no actor occurs more than twice'''

    # Dictionary where we keep a count of instances of each actor
    count = {}

    # Compile the fancy RE
    the_re = r'\d+:\s+([ \-\'\w]+) and ([ \-\'\w]+) starred in (.*)$'
    p = re.compile(the_re)

    # Process each line grabbing the actors and the movie
    for line in lines:
        # Skip any blank lines
        if line == '':
            continue

        # Define RE pattern and run match on current line
        m = p.match(line)

        # Error checking
        if m == None:
            # I missed a case for the RE
            assert False, f'Died on line: {line}'

        # Pull out the parts
        actor1 = m.group(1)
        actor2 = m.group(2)
        movie = m.group(3)   # currently unused
 
        # Put the actors in the dictionary
        increment(count, actor1)
        increment(count, actor2)                

    # print(count)
    print(f'{blue}No repeated actors!{reset}')

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 check_chain.py degrees32_output.txt')

    with open(sys.argv[1]) as f:
        lines = f.readlines()

        # Figure out how many initial lines to remove
        i = 0
        while 'degrees of separation' not in lines[i]:
            i += 1

        check(lines[i+1:])

if __name__ == '__main__':
    main()
