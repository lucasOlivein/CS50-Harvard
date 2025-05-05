import sys
import csv

def scourgify(before):
    try:
        with open(before) as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            rows = []

            for row in reader:
                new_row = dict()
                for header in headers:
                    if header == 'name':
                        last_name, first_name = row['name'].split(',')
                        new_row['first'] = first_name.lstrip()
                        new_row['last'] = last_name
                    else:
                        new_row[header] = row[header].lstrip()
                rows.append(new_row)
            return rows
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

def write(after, file_name):
    try:
        with open(file_name, "w", newline='') as file:
            header = list(after[0].keys())
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(after)
    except:
        sys.exit("Some error")

def main():
    if len(sys.argv) < 3:
        sys.exi("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exi("Too many command-line arguments")
    if sys.argv[1][-4:] != '.csv':
        sys.exit("Not a CSV file")
    else:
        after = scourgify(f"{sys.argv[1]}")
        write(after, f"{sys.argv[2]}")
    
main()