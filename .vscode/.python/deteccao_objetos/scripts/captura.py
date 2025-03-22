import cv2

def iniciar_captura():
    # Inicializa a webcam (0 indica a câmera padrão)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao acessar a câmera!")
        return

    while True:
        ret, frame = cap.read()  # Captura um frame
        if not ret:
            break

        cv2.imshow("Captura de Vídeo", frame)  # Exibe o vídeo

        # Pressione 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    iniciar_captura()
