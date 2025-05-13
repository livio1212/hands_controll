import cv2
import mediapipe as mp
from gestures import detectar_gestos

detectar_gestos()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

print("Pressione 'q' para sair")

while True:
    sucess, frame = cap.read()
    if not sucess:
        print("Erro ao acessar a webcam")
        break
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
       for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Detecdor de mãos - Livio", frame)

    if cv2.waitKey(1) & 0xFF == ord('l'):
        break
 
    
            

cap.release()
cv2.destroyAllWindows()