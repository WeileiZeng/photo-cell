# photo-cell
In this project, I use thousands of photos as 'pixels' to create/map one big background photo. Those are not exact pixels in the background photo, but an amount of pixels in some given rectangular area of the backgournd photo. Hence, I call it cells, and reach the name of this project 'photo-cell'



steps to run the program:
Input:many photos in /library/
	   one selected photo as background
output:temp/bg.jpg

1. put all photos into /library/
1.1 copy and rename the files into photo/
2. run classify.py to classify it into photo/horizontal/ and photo/vertical/
3. run thumbnail.py to make files smaller, and save it into /photo/../thumbnail/
4. run sort.py to sort photo in the order of Lab or rbg or grey value
5. run create.py to create the bg.jpg



parameter:
test cell size 96x32


update 24-Jun-18
use repeat.py to repeat each photo u*u times. It is better if we don't fix this number, but only fix the total number of photos after repeating. In this case, just try to match the pixel with corresponging photo with similar color. So some photo may be repeated more times than others. This could help to make a clearer bg.jpg.
A mapping from color to photo is needed. We can construct it inside repeat.py. The function would be similar to what we did in sort.py

