import cv2

img_path = "image//gakky.png"

img = cv2.imread(img_path)

# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# 上のリンクの内容をコピーしてxmlファイルを作成する
face_cascade_path = "src/opencv/face_cascade.xml"
face_cascade = cv2.CascadeClassifier(face_cascade_path)
# ↑機械学習でいうモデル

# グレー画像を作成
src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#　検出
faces = face_cascade.detectMultiScale(src_gray)

### これ以下にコードを書いて顔の周りに四角を描画してみよう ###