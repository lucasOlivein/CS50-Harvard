mounths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def formating(str):
    if '/' in str:
        mounth, day, year = str.split('/')
        if not mounth.isnumeric():
            raise ValueError()

    elif ',' in str:
        mounthDay, year = str.split(',')
        mounth, day = mounthDay.split(' ')
        year = year.strip()

        if mounth.title() not in mounths:
            raise ValueError()
        else:
            mounth = mounths.index(mounth.title()) + 1
    
    return (int(year), int(mounth), int(day))

def date(year, mounth, day):
    if day > 31 or mounth > 12:
        raise ValueError()
    
    return f"{year:04d}-{mounth:02d}-{day:02d}"

def main():
    while True:
        try:
            year, mounth, day = formating(input("Date: ").strip())
            str = date(year, mounth, day)
            break
        except Exception as e:
            pass
    
    print(str)
    


main()
