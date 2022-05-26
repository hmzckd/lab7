import cv2

path = r"C:\Users\C605\PycharmProjects\lab7\pontiff.jpg"
img = cv2.imread(path)
blue, red, green = cv2.split(img)
cv2.imshow("blue", blue)
cv2.imshow("red", red)
cv2.imshow("green", green)
cv2.waitKey(0)

newImage = cv2.merge((blue+100, green+30, red+15))
cv2.imshow("New Image", newImage)
cv2.waitKey(0)

cv2.destroyAllWindows()
