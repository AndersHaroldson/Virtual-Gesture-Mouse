import cv2
import mediapipe as mp
import autopy
import pyautogui
# Mediapipe setup
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
# Get screen size
winWidth, winHeight = autopy.screen.size()
# Capture video using OpenCV
cap = cv2.VideoCapture(0)

with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.75, min_tracking_confidence=0.75) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Cannot open device camera")
      exit()

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image_height, image_width, _ = image.shape

    # Draw the hand landmarks on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
        # Finger coordinate values
        xIndexTip = hand_landmarks.landmark[8].x * winWidth
        yIndexTip = hand_landmarks.landmark[8].y * winHeight

        xThumbTip = hand_landmarks.landmark[4].x * winWidth
        yThumbTip = hand_landmarks.landmark[4].y * winHeight

        xMiddleTip = hand_landmarks.landmark[12].x * winWidth
        yMiddleTip = hand_landmarks.landmark[12].y * winHeight

        xRingTip = hand_landmarks.landmark[16].x * winWidth
        yRingTip = hand_landmarks.landmark[16].y * winHeight
        
        print(int(xThumbTip), int(yThumbTip)) 
        
        # Circles the tip of the thumb, which acts as the mouse cursor
        cv2.circle(image, (int(hand_landmarks.landmark[4].x * image_width), int(hand_landmarks.landmark[4].y * image_height)), 10, (0, 0, 255), 2)
        # Coordinate out of range error handling
        if (xThumbTip >= winWidth):
           autopy.mouse.move(winWidth-1, abs(int(yThumbTip)))
        # Coordinate out of range error handling
        elif (yThumbTip >= winHeight):
           autopy.mouse.move(abs(winWidth-int(xThumbTip)), winHeight-1)
        # Move mouse according to thumb position on camera
        else:
          autopy.mouse.move(winWidth-abs(round(xThumbTip)), abs(int(yThumbTip)))

        # Click left mouse button
        # How-to: bring your index finger down to the same x value as the tip of your thumb (just flick your index finger down)
        if abs(yIndexTip - yThumbTip) < 10:
            autopy.mouse.click(autopy.mouse.Button.LEFT)
            print("Left click")
        # Click right mouse button
        # How-to: bring your middle finger down to the same x value as the tip of your thumb (just flick your middle finger down)
        elif abs(yMiddleTip - yThumbTip) < 10:
            autopy.mouse.click(autopy.mouse.Button.RIGHT)
            print("Right click")
        # Hold down the left mouse button 
        # How-to: bring your ring finger over your thumb (y-axis) - the y-axis is used because the x-axis can result in an unintended trigger 
        elif abs(xRingTip - xThumbTip) < 10:
            pyautogui.mouseDown(button="left")
            autopy.mouse.move(winWidth-abs(round(xThumbTip)), abs(int(yThumbTip)))  
            print("hold")

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('Hand Tracking Test', cv2.flip(image, 1))
    if cv2.waitKey(1) == ord('q'):
      break
cap.release()
