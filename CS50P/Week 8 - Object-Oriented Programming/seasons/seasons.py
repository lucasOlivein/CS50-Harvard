from datetime import date
import sys
import inflect
import re

def main():
    d = input("Date of Birth: ")
    pattern = r"(^[0-9]{4})-([0-9]{2})-([0-9]{2})$"
    birth = re.search(pattern, d)

    if birth and valid_birth(int(birth[1]), int(birth[2]), int(birth[3])):
        year, mounth, day = map(int, birth.groups())
        min = convert_date_to_min(date(year, mounth, day), date.today())
        print(convert_num_to_words(min))
    else:
        sys.exit("Invalid date")

# requere two values in order to assert the days difference in the test file
def convert_date_to_min(birth, today):
    dif = today - birth    
    return dif.days * 24 * 60

# Using the function inflect.num_to_word()
def convert_num_to_words(min):
    p = inflect.engine()
    return (p.number_to_words(min, andword="") + f" {p.plural_noun("minute", min)}").capitalize()

# Two condition: positive values and less than today's date.
def valid_birth(year, mounth, day):
    if all(x > 0 for x in [year, mounth, day]):
        if date(year, mounth, day) < date.today():
            return True
    
    return False
if __name__ == "__main__":
    main()
