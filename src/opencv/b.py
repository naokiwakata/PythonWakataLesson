import cv2  # <- opencvを使えるようにする

img_path = "image//gakky.png"  # 相対パス

img = cv2.imread(img_path)

# 赤青反転
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb', img_rgb)
cv2.waitKey(0)

# グレースケール
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey', img_gray)
cv2.waitKey(0)

# リサイズ
img_resize = cv2.resize(img, (200,200))
cv2.imshow('resize', img_resize)
cv2.waitKey(0)

# 回転
img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotate', img_rotate)
cv2.waitKey(0)