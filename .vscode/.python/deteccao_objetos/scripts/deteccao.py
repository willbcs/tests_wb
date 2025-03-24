import cv2
import torch
from ultralytics import YOLO

# Carregar modelo YOLOv8 pré-treinado
modelo = YOLO("yolov8n.pt")  # Essa é a versão mais leve do YOLOv8

def detectar_objetos():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao acessar a câmera!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Realizar a detecção
        resultados = modelo(frame)  

        # Desenhar as "caixas" delimitadoras nos objetos detectados.
        for r in resultados:
            for caixa in r.boxes:
                x1, y1, x2, y2 = map(int, caixa.xyxy[0])  # Coordenadas da caixa
                conf = caixa.conf[0]  # Confiança da detecção
                classe = int(caixa.cls[0])  # Classe do objeto detectado
                nome_classe = modelo.names[classe]  # Nome da classe

                if conf > 0.5:  # Exibir apenas objetos com confiança maior que 50%
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{nome_classe} ({conf:.2f})", 
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                                0.5, (0, 255, 0), 2)

        cv2.imshow("Detecção de Objetos", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_objetos()
