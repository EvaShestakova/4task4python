from PIL import Image
import numpy as np

try:  
    im1 = Image.open("im1.jpg")
    im2 = Image.open("im2.jpg")  
except FileNotFoundError:  
    print("Файл не найден")
    exit()
if im1.size!=im2.size:
    print("Размеры не совпадают")
    exit()
if im1.mode!='RGB' or im2.mode!='RGB':
    print("Формат не тот")
    exit()
arr1=np.array(im1)
arr2=np.array(im2)
for i in range(arr1.shape[0]):
    for j in range(arr1.shape[1]):
        if (arr2[i,j,0]==0) and (arr2[i,j,1]==0) and (arr2[i,j,2]==0):
            k=int((int(arr1[i,j,0])+int(arr1[i,j,1])+int(arr1[i,j,2]))/3)
            arr1[i,j,0]=k
            arr1[i,j,1]=k
            arr1[i,j,2]=k
img = Image.fromarray(arr1, 'RGB')
img.save("out.jpg")
