import cv2 
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand =  hand.Hands(max_num_hands = 2) #maximo de maos que queremos identificar
mpdrw = mp.solutions.drawing_utils

while True:
    check,img = video.read()    # a img receberá em BGR então transformamos para RGB

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks  #extrai os pontos que queremos identificar na imagem da mao
    altura, largura, c = img.shape #pega a altura e largura da imagem

    pontos = []
    if handsPoints:
        for points in handsPoints:
            #print(points)
            mpdrw.draw_landmarks(img,points,hand.HAND_CONNECTIONS) #desenha os pontos e as conexoes entre eles
            for id, cord in enumerate(points.landmark): #id é o numero do ponto e cord é a coordenada x e y
                # O landmark retorna valores entre 0 e 1, entao precisamos multiplicar pela largura e altura da imagem
                cx, cy = int(cord.x * largura), int(cord.y * altura)
                cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

                pontos.append(( cx, cy))
       
        dedos = [8, 12, 16, 20]
        # para fazer a diferenciação de uma mão para outra da pra fazer a verificação da posição do polegar--ver se tem algo no media pipe
        contador = 0
        if pontos:
            if pontos[4][0] > pontos[2][0]: #verifica se o polegar está levantado
                contador +=1
            for d in dedos:
                if pontos[d][1] < pontos[d - 2][1]: #verifica se o dedo está levantado, se o valor 8 estiver a baixo de 6 está ligado
                    contador +=1
        cv2.rectangle(img, (80, 10), (200, 100), (255, 255, 0), -1)
        cv2.putText(img, str(contador), (100, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
        print(contador)

        
    cv2.imshow("Imagem", img)

    # Fecha o programa se o usuário clicar no botão X da janela
    # cv2.getWindowProperty retorna < 1 quando a janela foi fechada
    if cv2.getWindowProperty("Imagem", cv2.WND_PROP_VISIBLE) < 1:
        break

    # Fecha também se o usuário pressionar ESC (27)
    if cv2.waitKey(1) == 27:
        break

video.release() # libera a camera
cv2.destroyAllWindows()