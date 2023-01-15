import cv2

img_path = "image//gakky.png"

img = cv2.imread(img_path)

# 高さ、幅、チャンネルを取得
height, width, channel = img.shape

threshold = 120  # しきい値（自分で設定）

for x in range(width):
    for y in range(height):
        ###
        # しきい値より色の値が大きければ白、それ以外であれば黒というコードを書く
        ###

cv2.imshow('shirokuro', img)
cv2.waitKey(0)
