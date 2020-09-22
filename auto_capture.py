#encoding:utf-8 

import cv2
import time

img_path = "./" #自己定義要儲存的路徑
sleep_time = 60       #自己定義要拍攝的間隔

cap = cv2.VideoCapture(0)        #開啟攝像頭

n = 0
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)     #生成攝像頭視窗
    
    name = img_path + str(n) + ".png"
    cv2.imwrite(name, frame)   #儲存路徑
    n += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):   #如果按下q 就截圖儲存並退出
        cap.release()
        cv2.destroyAllWindows()
	break

    time.sleep(sleep_time)