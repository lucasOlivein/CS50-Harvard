import sys

def count_lines(path):
    count = 0
    try:
        with open(path) as file:
            lines = file.readlines()

            for line in lines:
                if not line.lstrip().startswith("#") and line.lstrip() != '':
                    count += 1
    except FileNotFoundError:
        sys.exit("File not found")
    else:
        return count

def main():

    if len(sys.argv) < 2:
        sys.exi("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exi("Too many command-line arguments")
    if sys.argv[1][-3:] != '.py':
        sys.exit("Not a Python file")
    else:
        num_lines = count_lines(f"{sys.argv[1]}")

    print(num_lines)

main()