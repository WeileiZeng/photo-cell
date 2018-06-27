#read pix value
from PIL import Image

#return a list for the pixels
def get_list(pixelAccess,width,height):
    pixels_list=[]
    for i in range(width):
        pixels_row_list=[]
        for j in range(height):
            pixel = pixelAccess[i,j]
            pixels_row_list.append(pixel)
        pixels_list.append(pixels_row_list)
    return pixels_list

#Uclidean distance from wikipedia page of 'color difference'
def dist_pixel(pixel):
    r,g,b=pixel
    return dist_rgb(r,g,b)
def dist_rgb(r,g,b):
#could also work for (L,a,b)
    return 2*r*r+4*g*g+3*b*b+r/2*(r*r-b*b)/256 #Uclidean distance
#    return 0.3*r+0.59*g+0.11*b  #greyscale
#return average rgb value for the selected area in the image
def get_average(pixels_list,area):
    x1,y1,x2,y2=area
    if (x2 > len(pixels_list)):
        x2=len(pixels_list)
    if (y2 > len(pixels_list[0])):
        y2=len(pixels_list[0])
    #include x1 y1, but not x2, y2
    r,g,b=0,0,0
    n=(y2-y1)*(x2-x1)
    for i in range(x1,x2):
        for j in range(y1,y2):
            pixel=pixels_list[i][j]
            r+=pixel[0]
            g+=pixel[1]
            b+=pixel[2]
    r=r/n
    g=g/n
    b=b/n
    return  r,g,b
#return dist of this photo
def photo_dist(photo_name):
    img = Image.open(photo_name)
    width,height=img.size
    pixels_list=get_list(img.load(),width,height)
    pixel=get_average(pixels_list,(0,0,width,height))
    return dist_pixel(pixel)
def main():
    try:
        #Relative Path
        img = Image.open("temp/picture.jpg") 
        pix = img.load()
        width,height=img.size
        pixels = get_list(pix,width,height)
        print(pix[0,0])
        print(pixels[0][0])
    
        print img.size
        r,g,b = get_average(pixels,(100,100,200,200))
        print r,g,b
    except IOError:
        pass

if __name__ == "__main__":
    main()
