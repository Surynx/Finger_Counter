import cv2 as cv
import mediapipe.python.solutions.hands as h
import mediapipe.python.solutions.drawing_utils as d

cam = cv.VideoCapture(0)

hands = h.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5
)

while True:
    success,frames = cam.read()
    if not success:
        print('Camera error')
    frames = cv.flip(frames,1)
    framesrgb = cv.cvtColor(frames,cv.COLOR_BGR2RGB)

    handmark = hands.process(framesrgb)

    if handmark.multi_hand_landmarks:
        for landmarks in handmark.multi_hand_landmarks:
            print(landmarks)
    
            d.draw_landmarks(
            image=frames,
            landmark_list=landmarks,
            connections=h.HAND_CONNECTIONS
            ) 

    cv.imshow("video",frames)
    
    if cv.waitKey(1) == ord('e'):
        break

    

    
cam.release()
cv.destroyAllWindows()