import sys
import PIL
import PIL.Image
import PIL.ImageOps

IMG_TYPES = [".jpg","jpeg",".png"]

def took_cs50(input, output):
    try:
        shirt = PIL.Image.open("shirt.png","r")
        img = PIL.Image.open(input, "r")
        img = PIL.ImageOps.fit(img, shirt.size, 3, 0, (0.5,0.5))
        img.paste(shirt, shirt)
        img.save(output)

        shirt.close()
        img.close()
    except FileNotFoundError:
       sys.exit("FIle not found")
    except PIL.UnidentifiedImageError:
        sys.exit("Unidentified Image")
    except (ValueError, TypeError):
        sys.exit("some variable error")

def main():
    

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[2][-4:].lower() in IMG_TYPES:
        sys.exit("Invalid input")
    elif sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
        sys.exit("Input and output have different extensions")
    else:
        took_cs50(sys.argv[1], sys.argv[2])

    
main()