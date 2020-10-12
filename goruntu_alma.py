import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()

    cv2.rectangle(goruntu,(200,200),(300,300),(25,36,98),3)
    cv2.putText(goruntu,"Muhammed",(300,300),cv2.FONT_HERSHEY_DUPLEX,1,(200,0,0),2)
    
    cv2.imshow("maga",goruntu)

    if cv2.waitKey(30) & 0xFF==('x'):
        break

kamera.release()

cv2.destroyAllWindows()

