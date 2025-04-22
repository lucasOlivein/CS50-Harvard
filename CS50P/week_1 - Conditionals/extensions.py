extensions = [("gif", "image/gif"),
              ("jpg", "image/jpeg"),
              ("jpeg", "image/jpeg"),
              ("png", "image/png"),
              ("pdf", "application/pdf"),
              ("txt", "text/plain"),
              ("zip", "application/zip")]


def main():
    file = input("File name: ")

    for extension in extensions:
        if extension[0] == file.lower().rstrip().split(".")[-1]:
            print(extension[1])
            return

    print("application/octet-stream")

main()
