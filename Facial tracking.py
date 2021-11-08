from cv2 import cv2


def detect_face():
    """Detects faces in video frames using a harr cascade and draws a rectangle around them"""
    facial_cascade = cv2.CascadeClassifier('Harr cascade (Frontal face).xml')
    capture = cv2.VideoCapture(0)
    run = True
    while run:
        return_value, image = capture.read()
        face = facial_cascade.detectMultiScale(image)

        if len(face) > 0:
            x = face[0][0] + face[0][2]
            y = face[0][1] + face[0][3]
            cv2.rectangle(image, (face[0][0], face[0][1]), (x, y), (255, 255, 0))
        cv2.imshow('Facial tracking (Press "Q" to exit)', image)
        keybind = cv2.waitKey(3)
        if keybind == ord('Q') or keybind == ord('q'):
            capture.release()
            cv2.destroyAllWindows()
            run = False


detect_face()
