import cv2
import numpy as np

# Load Haar cascade for face detection
cascade_path = "quiz_app/static/quiz_app/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Start the webcam
cap = cv2.VideoCapture(0)

# Face tracking variables
face_not_found_count = 0
MAX_ALLOWED_MISSES = 30  # Number of frames without a face before triggering an alert

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert to grayscale for better accuracy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

    if len(faces) == 0:
        face_not_found_count += 1
    else:
        face_not_found_count = 0  # Reset count when face is found

    # Alert if user is looking away for too long
    if face_not_found_count >= MAX_ALLOWED_MISSES:
        print("⚠️ ALERT: User is looking away from the screen!")

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
