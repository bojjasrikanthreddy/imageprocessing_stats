import numpy as np
import random as rd
import cv2 

def find_average(a,i,j,rows,cols):
    if (i==0 and j==0):
        l=[a[i][j+1],a[i+1][j]]
        return l
        #return (int(a[i][j+1])+int(a[i+1][j]))/2
    elif (i==0 and j==cols-1):
        l=[a[i+1][j],a[i-1][j-1]]
        return l
        #return (a[i+1][j]+a[i-1][j-1])/2
    elif (i==rows-1 and j==0):
        l=[a[i][j+1],[i-1][j]]
        return l
        #return (a[i][j+1]+a[i-1][j])/2
    elif (i==rows-1 and j==cols-1):
        l=[a[i][j-1],a[i-1][j]]
        return l
        #return (a[i][j-1]+a[i-1][j])/2
    elif (i==0 and j!=0 and j!=cols-1):
        l=[a[i+1][j]]
        return l
        #return a[i+1][j]
    elif (j==0 and i!=0 and i!=rows-1):
        l=[a[i][j+1]]
        return l
        #return a[i][j+1]
    elif (i==rows-1 and j!=0 and j!=cols-1):
        l=[a[i-1][j]]
        return l
        #return a[i-1][j]
    elif (j==cols-1 and i!=0 and i!=rows-1):
        l=[a[i][j-1]]
        return l
        #return a[i][j-1]
    else:
        l=[a[i][j-1],a[i][j+1],a[i+1][j],a[i-1][j]]
        return l
        #return (a[i][j-1]+a[i][j+1]+a[i+1][j]+a[i-1][j])/4



file_name='sri'
img=cv2.imread(file_name+'.jpeg',0)
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img)
print(type(img))
print('no of rows,columns=',len(img),len(img[0]))
sri=0

q_mean=np.zeros((len(img),len(img[0])),dtype=int)
q_var=np.zeros((len(img),len(img[0])),dtype=int)
q_min=np.zeros((len(img),len(img[0])),dtype=int)
q_max=np.zeros((len(img),len(img[0])),dtype=int)
q_avg=np.zeros((len(img),len(img[0])),dtype=int)
q_std=np.zeros((len(img),len(img[0])),dtype=int)
q_mode=np.zeros((len(img),len(img[0])),dtype=int)
q_median=np.zeros((len(img),len(img[0])),dtype=int)

for i in range(len(img)):
    for j in range(len(img[0])):
        #print(i,j)
        try:
            ret_val=find_average(img,i,j,len(img),len(img[0]))
            #if not ret_val:
            #    print('ret_val is empty')
            #else:
            #    print(ret_val)
            ret_val_mean=np.mean(ret_val)
            ret_val_var=np.var(ret_val)
            ret_val_avg=np.average(ret_val)
            ret_val_min=np.min(ret_val)
            ret_val_max=np.max(ret_val)
            ret_val_std=np.std(ret_val)
            ret_val_median=np.median(ret_val)


            q_avg[i][j]=ret_val_avg
            q_max[i][j]=ret_val_max
            q_min[i][j]=ret_val_min
            q_var[i][j]=ret_val_var
            q_mean[i][j]=ret_val_mean
            q_std[i][j]=ret_val_std
            q_median[i][j]=ret_val_median

        except:
            sri+=1
print(q_mean.shape)
print('no of rows,columns=',len(img),len(img[0]))
print(q_mean)
cv2.imwrite(file_name+'_mean.png',q_mean)
im=cv2.imread(file_name+'_mean.png',0)
cv2.imshow('mean image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(file_name+'_avg.png',q_avg)
im=cv2.imread(file_name+'_avg.png',0)
print('size of q_avg=',q_avg.shape)
cv2.imshow('avg image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(file_name+'_max.png',q_max)
im=cv2.imread(file_name+'_max.png',0)
cv2.imshow('max image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(file_name+'_min.png',q_min)
im=cv2.imread(file_name+'_min.png',0)
cv2.imshow('min image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(file_name+'_var.png',q_var)
im=cv2.imread(file_name+'_var.png',0)
cv2.imshow('var image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(file_name+'_std.png',q_std)
im=cv2.imread(file_name+'_std.png',0)
cv2.imshow('standard deviation image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(file_name+'_median.png',q_std)
im=cv2.imread(file_name+'_median.png',0)
cv2.imshow('median image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('total number of exceptions =',sri)






        