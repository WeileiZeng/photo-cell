#create thumbnail of photos to save time.
###
'''
Input: photos in a folder named photo[#].jpg
and a background image

format
small image size 960 x 640 or 640 x 960
back ground size 10x10=10x5+10x5  8 12

number of photos
horizontal 86
vertical 83
'''
from PIL import Image
import os
width=960
height=640
width=96
height=64
ss=width,width
folder = 'photo/horizontal/'
#folder = 'photo/vertical/'
max = 400 #max number of photos

def main():
    try:
        for i in range(1,max):
                name = 'photo'+str(i)+'.jpg'
                print name
                img=Image.open(folder+name)
                print img
                img.thumbnail(ss,Image.ANTIALIAS)
                img.save(folder+'mini/'+name)
    except IOError:
        print 'error happens/or finish while i = ',i
        pass

if __name__ == "__main__":
    main()
