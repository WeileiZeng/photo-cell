#collect many photoes into a big one
###
'''
Input: photos in a folder named photo[#].jpg
and a background image

format
1920x1280
4800 x 3200
small image size 960 x 640 or 640 x 960
back ground size 10x10=10x5+10x5  8 12

number of photos
horizontal 86 - 256  21 x 12
vertical 83 - 143    14 x 10
'''
from PIL import Image
import os
import pix
def get_data_list_horizontal(bg,row,col,row2,col2):
#grid size row x col
#cell size w x h
    width,height = bg.size
    w=width/(col+col2*2/3)
    h=height/row
    pixels_list = pix.get_list(bg.load(),width,height)
    data=[]
    for i in range(row):
        for j in range(col):
            area = (w*j,h*i,w*(j+1),h*(i+1) )
            d = pix.dist_pixel(pix.get_average(pixels_list,area))
            data.append([i,j,d])
    data = sorted(data, key = lambda p:p[2])
    return data

def get_data_list_vertical(bg,row,col,row2,col2):
#grid size row x col
#cell size w x h
    width,height = bg.size
    w=width/(col+col2*2/3)*2/3
    h=height/row*3/2
    pixels_list = pix.get_list(bg.load(),width,height)
    data=[]
    w0=w*col*3/2
    for i in range(row2):
        for j in range(col2):
            area = (w0+w*j,h*i,w0+w*(j+1),h*(i+1) )
            d = pix.dist_pixel(pix.get_average(pixels_list,area))
            data.append([i,j,d])
    data = sorted(data, key = lambda p:p[2])
    return data

def main():
    try:
        width=960
        height=640
        ss=width,width
        row=18 #only row and row2 matters, where row/row2=3/2
        col=14
        row2=12
        col2=11
        bg = Image.open("temp/church2.jpg") #background
        bg_data_horizontal=get_data_list_horizontal(bg,row,col,row2,col2)
        bg_data_vertical=get_data_list_vertical(bg,row,col,row2,col2)
        print bg
        bg = bg.resize((width*(col+col2*2/3),height*row),Image.ANTIALIAS)
        print bg
        n=row*col
        folder = 'photo/horizontal/thumbnail/'
        for i in range(0,n):
            #m=n-i-1 
                m=i
                name= folder+'dist_sorted_photo'+str(m+1)+'.jpg'
                img=Image.open(name)
                d=bg_data_horizontal[i]
                bg.paste(img,(width*d[1],height*d[0]))
        print 'horizontal n = ',n
        n=row2*col2
        folder = 'photo/vertical/thumbnail/'
        print folder
        for i in range(0,n):            
                #m=n-i-1 
                m=i
                name= folder+'dist_sorted_photo'+str(m+1)+'.jpg'
                img=Image.open(name)
                d=bg_data_vertical[i]
                bg.paste(img,(width*col+height*d[1],width*d[0]))#inverse width and height
        print 'vertical n = ',n
        bg.save('temp/bg.jpg')
        os.system('open temp/bg.jpg')
    except IOError:
        print 'error happens'
        pass

if __name__ == "__main__":
    main()
