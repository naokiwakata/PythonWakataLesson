import cv2

img_path = "image//gakky.png"

img = cv2.imread(img_path)

# 画像のグレースケール化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 画像の白黒2値化
ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('binary', thresh)
cv2.waitKey(0)

# 輪郭を抽出する
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 輪郭を画像に書き込む
output = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('contour', img)
cv2.waitKey(0)
