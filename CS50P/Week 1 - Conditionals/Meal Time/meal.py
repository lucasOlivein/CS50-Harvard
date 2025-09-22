def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    time = time.strip()
    pm = 0

    if time.find(" ") != -1:
        time, meridian = time.split(" ")

        if meridian.lower()[0] == "p":
            pm = 12

    if time.find(":") != -1:
        hour, minutes = time.split(":")
        minutes = float(minutes) / 60
    else:
        hour = float(time)
        minutes = 0

    return float(hour) + pm + minutes




if __name__ == "__main__":
    main()
