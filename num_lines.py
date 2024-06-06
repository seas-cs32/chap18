### chap18/num_lines.py -- Written by ChatGPT

def print_numbered_lines(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all lines in the file
            lines = file.readlines()

        # Loop through the lines, enumerate starts counting from 0 by default
        for index, line in enumerate(lines, start=1):
            # Print each line with its line number
            # Strip is used to remove any extra newline characters before adding our own
            print(f"{index}: {line.strip()}")

    except FileNotFoundError:
        # If the file is not found, inform the user
        print("The file was not found. Please check the file path and try again.")

# You can call the function with the path to the file you want to print
# For example: print_numbered_lines("example.txt")


def main():
    print_numbered_lines("../chap01/txts/CatInTheHat.txt")

if __name__ == '__main__':
    main()
