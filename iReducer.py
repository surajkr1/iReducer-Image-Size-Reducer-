import os
import glob
import cv2

# to take input how much image to compressed as per wish of user
scale = int(input("Enter Compression % :- "))
s = 100 - scale
# Enter original image directory.
os.chdir('J:/python program/iReducer/img')
imgs = glob.glob('*.jpg')
def trans_square(imgs):
    for i,img_list in enumerate(imgs):
        
        img = cv2.imread(img_list)
        height = int(img.shape[1] * s/100)
        width = int(img.shape[0] * s/100)
        dimen = (height,width)
        # to resize images 
        resize_img = cv2.resize(img,dimen)
        #to save reduced images
        cv2.imwrite('J:/python program/iReducer/output/reduced_'+img_list+'.jpg',resize_img)

        convimg = int(os.path.getsize('J:/python program/iReducer/output/reduced_'+img_list+'.jpg')) / 1024

        # to check image size not greater than 100kb and if it is above 100kb we will delete it by program.
        if convimg > 100:
            print(convimg, "KB")
            os.remove('J:/python program/iReducer/output/reduced_'+img_list+'.jpg')
        


        
        if i == 60 : #no.of Images in your folder
            break
    return img

trans_square(imgs)