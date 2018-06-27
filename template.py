from PIL import Image

def main():
    try:
        #Relative Path
        img = Image.open("picture.jpg")
        width, height = img.size

    except IOError:
        pass

if __name__ == "__main__":
    main()
