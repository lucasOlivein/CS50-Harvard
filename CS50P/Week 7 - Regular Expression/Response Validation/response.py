import validators


def check_email(s):
    return validators.email(s)

def main():
    if check_email(input("What's your email address?: ")):
        print("Valid")
    else:
        print("Invalid")


main()