import sys
import csv
from tabulate import tabulate

def read_file(path):
    try:
        with open(path) as file:
            reader = csv.DictReader(file)
            catalogue = dict()

            for key in reader.fieldnames:
                catalogue[key] = []
            for row in reader:
                for item in row:
                    catalogue[item].append(row[item])
            
            return catalogue
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    if len(sys.argv) < 2:
        sys.exi("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exi("Too many command-line arguments")
    if sys.argv[1][-4:] != '.csv':
        sys.exit("Not a CSV file")
    else:
        catalogue = read_file(f"{sys.argv[1]}")

    print(tabulate(catalogue, headers="keys", tablefmt="grid"))



main()