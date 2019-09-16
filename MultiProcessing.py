import shutil
import requests
from threading import Thread
import time
 
def downloadImage(url, imagename):
    print(imagename + ' Download started ' + time.ctime(time.time()))
    response = requests.get(url, stream=True)
    with open(imagename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print(imagename + ' Download finished ' + time.ctime(time.time()))

url1 = 'https://vignette.wikia.nocookie.net/deathbattlefanon/images/b/b7/Epic_Iron_Man.png/revision/latest?cb=20150404070629'
url2 = 'https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/c/c0/AoU_Iron_Man_01.png/revision/latest?cb=20150309164237'
url3 = 'https://mwi.usma.edu/wp-content/uploads/2016/04/3264149-42-iron-man-iron-man-hd-8-free-spot-free-download-e1459563979846.jpg'

# downloadImage(url1,'ironMan1.png')
# downloadImage(url2,'ironMan2.png')
# downloadImage(url3,'ironMan3.jpg')

t1 = Thread(target=downloadImage, args=(url1,'ironMan1.png'))
t1.start()
t2 = Thread(target=downloadImage, args=(url2,'ironMan2.png'))
t2.start()
t3 = Thread(target=downloadImage, args=(url3,'ironMan3.jpg'))
t3.start()

print("Main Thread Exiting")