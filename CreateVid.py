import os
import cv2

path = "PRO-C105-Student-Boilerplate-main\Pro_Images"

images = []

imageFiles = os.listdir(path)

for file in imageFiles:
    name,ext=os.path.splitext(file)
    if ext in [".gif",".png",".jpg",".jpeg",".jfif"]:
        filename = path+"/"+file
        images.append(filename)

count=len(images)

frame=cv2.imread(images[0])
h,w,c=frame.shape
print(h,w,c)
size=(w,h)

out = cv2.VideoWriter("Project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(count-1,0,-1):
    img=cv2.imread(images[i])
    out.write(img)
out.release()

print("Done")