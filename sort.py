#sort the photos in /thumbnail/ in the order of dist 
import pix
from PIL import Image
import os
def main():
    try:
        #Relative Path
        folder='photo/horizontal/mini'
        folder='photo/vertical/mini'
        max=400
        data=[]
        try:
            for i in range(1,max):
                print 'i = ',i
                name=folder+'/photo'+str(i)+'.jpg'
                d=pix.photo_dist(name)
                data.append([i,d,name])
        except IOError:
            print 'stopped when i = ',i
            pass
        #sort by distance
        data = sorted(data,key=lambda item:item[1])
        n=len(data)
        for i in range(n):
            print data[i]
            name=data[i][2]
            new_name=folder+'/dist_sorted_photo'+str(i+1)+'.jpg'
            os.system('cp '+name+' '+new_name)
            
    except IOError:
        print 'error'
        pass

if __name__ == "__main__":
    main()
