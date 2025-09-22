def covert(x):
    x = x.replace(':)','🙂')
    x = x.replace(':(','🙁')
    return x


def main():
    x = input()
    x = covert(x)
    print(x)

main()
