import cv2

img_path = "image//gakky.png"

img = cv2.imread(img_path)
 
cv2.putText(img,
            text='gakky is so cute',
            org=(10, 300),  # 文字の位置
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(0, 255, 0),  # 色
            thickness=2,  # 太さ
            lineType=cv2.LINE_4)

cv2.imshow('text', img)
cv2.waitKey(0)

cv2.circle(img,
           center=(200, 400),
           radius=60,
           color=(0, 255, 255),
           thickness=3,
           lineType=cv2.LINE_4,
           shift=0)

cv2.imshow('circle', img)
cv2.waitKey(0)

cv2.rectangle(img,
              pt1=(50, 150), #左上の座標
              pt2=(125, 250), #右下の座標
              color=(255, 255, 0),
              thickness=3,
              lineType=cv2.LINE_4,
              shift=0)

cv2.imshow('rectangle', img)
cv2.waitKey(0)