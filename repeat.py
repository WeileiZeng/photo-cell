#repeat photo 100 times
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
import math
u=10
def get_data_list_horizontal(bg,row,col,row2,col2):
#grid size row x col
#cell size w x h
#return a list of [i,j,d] of the left half of image bg. the list is sorted by d.
    width,height = bg.size
    w=width/(col+col2*2/3)
    h=height/row
    pixels_list = pix.get_list(bg.load(),width,height)
    #resize
    #u=2
    w=w/u
    h=h/u
    row=row*u
    col=col*u

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

    w=w/u
    h=h/u
    row2=row2*u
    col2=col2*u
    row=row*u
    col=col*u

    data=[]
    w0=w*col*3/2
    for i in range(row2):
        for j in range(col2):
            area = (w0+w*j,h*i,w0+w*(j+1),h*(i+1) )
            d = pix.dist_pixel(pix.get_average(pixels_list,area))
            data.append([i,j,d])
    data = sorted(data, key = lambda p:p[2])
    return data

def dimension(bg_w,bg_h,n_h,n_v):
#input: width of bg.jpg, height of bg.jpg
#       number of horizontal photos, number vertical photos
#output:row and col of horizontal photos, row and col of vertical photos
    print bg_w,bg_h
    a=(n_h+n_v)*3.0/2.0
    print a
    xx=1.0*bg_h/bg_w*a
    print xx
    x=math.ceil(xx**0.5)
    print x
    row=int(x)
    row2=int(math.ceil(row*2/3.0))
    col=n_h/row
    col2=n_v/row2
    print row,col,row2,col2
    return row,col,row2,col2

def get_img_to_paste(folder,d,pos,max):
#input: forlder, corresponding distance in bg.jpg, current position in the data_list,max number of photos in the folder


def main():
    try:
        width=96
        height=64
        ss=width,width
        bg_name='beach.jpg'
        bg = Image.open("temp/"+bg_name) #background
        n_h,n_v=256,143
        bg_w,bg_h=bg.size
        row,col,row2,col2=dimension(bg_w,bg_h,n_h,n_v)
#        row=18 #only row and row2 matters, where row/row2=3/2
#        col=14
#        row2=12
#        col2=11

        bg_data_horizontal=get_data_list_horizontal(bg,row,col,row2,col2)
        bg_data_vertical=get_data_list_vertical(bg,row,col,row2,col2)
        print bg
        #u=2  #resize
        bg = bg.resize((width*(u*col+u*col2*2/3),height*row*u),Image.ANTIALIAS)
        print bg
        n=row*col

        n=n*u*u 
        folder = 'photo/horizontal/mini/'
        for i in range(0,n):
                
            #m=n-i-1 
                m=i
                name= folder+'dist_sorted_photo'+str(m/u/u+1)+'.jpg'
                img=Image.open(name)
                d=bg_data_horizontal[i]
                bg.paste(img,(width*d[1],height*d[0]))
        print 'horizontal n = ',n
        n=row2*col2
        n=n*u*u
        folder = 'photo/vertical/mini/'
        print folder
        for i in range(0,n):            
                #m=n-i-1 
                m=i
                name= folder+'dist_sorted_photo'+str(m/u/u+1)+'.jpg'
                img=Image.open(name)
                d=bg_data_vertical[i]
                bg.paste(img,(width*col*u+height*d[1],width*d[0]))#inverse width and height
        print 'vertical n = ',n
        bg.save('temp/bg_'+bg_name)
        os.system('open temp/bg_'+bg_name)
    except IOError:
        print 'error happens'
        pass

if __name__ == "__main__":
    main()
