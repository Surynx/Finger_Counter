import cv2 as cv
import mediapipe.python.solutions.hands as h
import mediapipe.python.solutions.drawing_utils as d

#camera setup
cam = cv.VideoCapture(0)
#making landmark list
def gethandlandmark(img,draw):
    lmlist=[]

    hands = h.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5
    )
    framergb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    hand_detected = hands.process(framergb)
    
    if hand_detected.multi_hand_landmarks:
      for landmarks in hand_detected.multi_hand_landmarks:
        #print(landmarks)
        for id,lm in enumerate(landmarks.landmark): #enumerate is function for giving index during iteration
            #print(id,lm)
            hi,w,c = img.shape
            cx,cy = int(lm.x*w),int(lm.y*hi)
            lmlist.append((id,cx,cy))
            #print(lmlist)
      if draw:
       d.draw_landmarks(
          image=img,
          landmark_list=landmarks,
          connections=h.HAND_CONNECTIONS

       )

    return lmlist
#making counter
def finger_count(lmlist):
   count = 0
   if lmlist[8][2] < lmlist[6][2]:
      count +=1
   if lmlist[12][2] < lmlist[10][2]:
      count +=1
   if lmlist[16][2] < lmlist[14][2]:
      count +=1
   if lmlist[20][2] < lmlist[18][2]:
      count +=1
   if lmlist[4][1] < lmlist[2][1]:
      count +=1   
   return count
    
    
while True:
    success,frame = cam.read()
    if not success:
        print("Camera Error!")
    
    frame = cv.flip(frame,1)

    list = gethandlandmark(frame,False)
    if list:
     #print(list)
     c = finger_count(list)
     print(c)
     cv.rectangle(frame,(400,10),(600,250),(0,0,0),-1)
     cv.putText(frame,str(c),(400,250),cv.FONT_HERSHEY_PLAIN,20,(240,248,255),20)
    
    cv.imshow("Ai finger counter",frame)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()       