import cv2 as cv
from pygame import mixer

mixer.init()
mixer.music.load('beep.wav')

camera_id = 0

camera = cv.VideoCapture(camera_id)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

while True:

    ret, frame = camera.read()

    if ret:

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, 1.05, 15, minSize=(50, 50))

        eye = eye_cascade.detectMultiScale(gray, 1.05, 8, minSize=(10, 10))

        face_detect = 0

        eye_detect = 0

        for (x, y, w, h) in face:
            cv.rectangle(img=frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=5)
            cv.putText(frame, "Face Detected", (x + 5, y + 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            face_detect += 1

        for (x, y, w, h) in eye:
            cv.rectangle(img=frame, pt1=(x, y), pt2=(x+w, y+h), color=(255, 0, 255), thickness=3)
            cv.putText(frame, "Eye Detected", (x + 5, y + 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            eye_detect += 1

        if face_detect == 0 and eye_detect == 0:
            mixer.music.play()

        cv.imshow("Sleep Detection", frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv.destroyAllWindows()