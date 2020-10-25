import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)


while True:
    _, frame = webcam.read()
    e1 = cv2.getTickCount()
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"
    
    e2 = cv2.getTickCount()    
    time = (e2 - e1)/ cv2.getTickFrequency()

    cv2.putText(frame, text, (5, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (147, 58, 31), 1)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (5, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (255, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (147, 58, 31), 1)
    cv2.putText(frame, "Performance: " + str(time), (455, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
