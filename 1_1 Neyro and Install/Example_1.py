import cv2

img = cv2.imread("py.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

edges = cv2.Canny(gray, 50, 150)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)

cv2.waitKey(10000)
cv2.destroyAllWindows()

