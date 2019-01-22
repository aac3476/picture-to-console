import cv2
import numpy as np

img=cv2.imread('a.png')
row, col, channel = img.shape
img_gray = np.zeros((row, col))
for r in range(row):
    for l in range(col):
        img_gray[r, l] = 1 / 3 * img[r, l, 0] + 1 / 3 * img[r, l, 1] + 1 / 3 * img[r, l, 2]

img_gray[r, l] = 0.11 * img[r, l, 0] + 0.59 * img[r, l, 1] + 0.3 * img[r, l, 2]
img_binary = np.zeros_like(img_gray)
img_gray = cv2.blur(img_gray,(1,1))
img_gray = cv2.resize(img_gray,dsize=(int(img_gray.shape[1]*0.8),int(img_gray.shape[0]*0.5)),interpolation=cv2.INTER_AREA)
img_binary = cv2.resize(img_binary,dsize=(int(img_binary.shape[1]*0.8),int(img_binary.shape[0]*0.5)),interpolation=cv2.INTER_AREA)
threshold = 100
row, col = img_gray.shape
print(img_gray.shape)
str=""
for r in range(row):
    for l in range(col):
        if img_gray[r, l] >= threshold:
            img_binary[r, l] = 255
            str = str+"*"
        else:
            img_binary[r, l] = 0
            str = str+" "
    str=str+"\n"
print(str)
f=open('a.txt','w')
f.write(str)
f.close()
cv2.imshow("img", img_binary.astype("uint8"))
cv2.waitKey()











# img=cv2.imread('a.png')
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# h, w = gray.shape[:2]
# m = np.reshape(gray, [1, w * h])
# mean = m.sum() / (w * h)
# print("mean:", mean)
# ret, binary = cv2.threshold(gray, mean, 255, cv2.THRESH_BINARY)
# print(binary.shape)
# str = ""
# for i in range(binary.shape[0]):
#     for j in range(binary.shape[1]):
#         if binary[i,j]:
#             str = str+" "
#         else:
#
#             str = str+"*"
#     str=str+"\n"
# print(str)
# cv2.namedWindow("binary2", cv2.WINDOW_NORMAL)
# cv2.imshow("binary2", binary)
# cv2.waitKey (0)
# cv2.destroyAllWindows()
