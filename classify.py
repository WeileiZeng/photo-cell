#sort the photos into horizontal and vertical class
###
'''
Input: photos in a folder named photo[#].jpg
and a background image

format
small image size 960 x 640 or 640 x 960
back ground size 10x10=10x5+10x5  8 12
'''
from PIL import Image
import os

def main():
    try:
        max=400
        folder = 'photo/'
        folder_horizontal=folder+'horizontal/'
        folder_vertical = folder+'vertical/'
        num_horizontal=0
        num_vertical=0
        for i in range(1,max):
            name = folder+'photo'+str(i)+'.jpg'
            img=Image.open(name)
            width, height = img.size
            if width > height:
                num_horizontal+=1
                new_name = folder_horizontal+'photo'+str(num_horizontal)+'.jpg'
#               img.save(new_name)
                os.system('cp '+name+' '+new_name)
            else:
                num_vertical+=1
                new_name = folder_vertical+'photo'+str(num_vertical)+'.jpg'
#                img.save(new_name)
                os.system('cp '+name+' '+new_name)
    except IOError:
        pass
    print 'total number of photos = ',num_horizontal+num_vertical
    print 'Number of horizontal photos',num_horizontal
    print 'Number of vertical photos',num_vertical

if __name__ == "__main__":
    main()
