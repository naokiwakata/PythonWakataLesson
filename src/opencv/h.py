import cv2

img_path = "image//gakky.png"

img = cv2.imread(img_path)

# 高さ、幅、チャンネルを取得
height, width, channel = img.shape

threshold = 120  # しきい値（自分で設定）

for x in range(width):
    for y in range(height):
        if img[x, y][0] > threshold:  # B(RGBのうち)の値がしきい値より大きい場合
            img[x, y] = [255, 255, 255]  # 白
        else:
            img[x, y] = [0, 0, 0]  # 黒

cv2.imshow('shirokuro', img)
cv2.waitKey(0)