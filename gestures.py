import cv2
import mediapipe as mp
import webbrowser
import pyautogui
import time
import math 
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Controle de volume (Windows)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_ctrl = cast(interface, POINTER(IAudioEndpointVolume))

min_vol, max_vol, _ = volume_ctrl.GetVolumeRange()

# Variáveis de controle

gestures_ativos = False
tempo_execucao = {
    "navegador": 0,
    "print":0,
    "linkedin":0,
    "volume":0

}
INTERVALO = 1.5

# funçao para açoes especificas

def distancia(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

def abrir_navegador():
    print("🟢 Ação: Abrindo navegador...")
    webbrowser.open("https://www.google.com")

def capturar_tela():
    print("🟢 Ação: Capturando print da tela...")
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

def abrir_linkedin():
    print("🟢 Ação: Abrindo Linkedin...")
    webbrowser.open("https://www.linkedin.com/in/livio-costa/")


# funçao para contar os dedos levantados

def contar_dedos(mao):
    dedos_levantados = 0

    if mao.landmark[4].x < mao.landmark[3].x:
        dedos_levantados += 1
    tips = [8, 12, 16, 20]
    for tip in tips:
        if mao.landmark[tip].y < mao.landmark[tip - 2].y:
            dedos_levantados += 1
    return dedos_levantados

# funçao para detectar gestos
 
def ajustar_volume(mao):
    polegar = mao.landmark[4]
    indicador = mao.landmark[8]
    dist = distancia(polegar, indicador)

    escala = max(0.0, min(dist / 0.25, 1.0))
    volume = min_vol + escala * (max_vol - min_vol)
    volume_ctrl.SetMasterVolumeLevel(volume, None)
    
    print(f"Distância: {dist:.2f} -> Volume: {int(escala * 100)}%")

def detectar_gestos():
    global gestures_ativos
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # espelhar a imagem e converter para rgb

            frame = cv2.flip(frame, 1)
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)

            key = cv2.waitKey(5) & 0xFF
            if key == ord('g'):
                gestures_ativos = not gestures_ativos
                print("Modo ativado" if gestures_ativos else "modo desativado") 
                        
            if results.multi_hand_landmarks and gestures_ativos:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    dedos = contar_dedos(hand_landmarks)
                    atual = time.time()
                    # ativaçao dos comandos
                    # caso gesto ativado tera um intervalo de tempo

                    if gestures_ativos:
                        if dedos == 1 and atual - tempo_execucao["navegador"] > INTERVALO:
                            abrir_navegador()
                            tempo_execucao["navegador"] = atual

                        elif dedos == 2 and atual - tempo_execucao["print"] > INTERVALO:
                            capturar_tela() 
                            tempo_execucao["print"] = atual

                        elif dedos == 3 and hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y:
                            if atual - tempo_execucao["linkedin"] > INTERVALO:
                                abrir_linkedin()
                                tempo_execucao["linkedin"] = atual
                        elif dedos == 0 and atual - tempo_execucao["volume"] > 0.3:
                            ajustar_volume(hand_landmarks)
                            tempo_execucao["volume"] = atual

            cv2.imshow("Detector de gestos", frame)
            if key == 27:
                break
    cap.release()
    cv2.destroyAllWindows()       
    