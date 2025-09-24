import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = "([0-9][0-9]?):?([0-9][0-9])? (PM|AM)"
    if time := re.search(rf"{pattern} to {pattern}", s):
        hour1, min1, merin1 = int(time[1]), time[2], time[3]
        hour2, min2, merin2 = int(time[4]), time[5], time[6]

        if not (0 < hour1 <= 12 and 0 < hour2 <= 12):
            raise ValueError
        
        if (min1 and int(min1) >= 60) or (min2 and int(min2) >= 60):
            raise ValueError

        if merin1 == 'PM' and hour1 != 12:
            hour1 += 12
        if merin2 == 'PM' and hour2 != 12:
            hour2 += 12
        
        if hour1 == 12 and merin1 == "AM":
            hour1 = 0
        if hour2 == 12 and merin2 == "AM":
            hour2 = 0

        if not min1:
            min1 = 0
        if not min2:
            min2 = 0

        return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()