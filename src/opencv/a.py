import cv2  # <- opencvを使えるようにする

img_path = "image//gakky.png" # 相対パス
img_path = "/Users/wakatanaoki/PythonProject/PythonWakataLesson/image/gakky.png" #絶対パス

img = cv2.imread(img_path) # 画像を読み込む

print(img.shape) # 縦×横×3色 (480,480,3)

cv2.imshow('img', img) # 画像を表示する
cv2.waitKey(0) # キーボードが押されるまで画像表示をする