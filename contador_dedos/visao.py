import cv2 
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand =  hand.Hands(max_num_hands = 2) #maximo de maos que queremos identificar
mpdrw = mp.solutions.drawing_utils

while True:
    check,img = video.read()    #check indica se deu certo, img é a imagem capturada
    if not check:
        break
    
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # a img receberá em BGR então transformamos para RGB
    #openCV trabalha com BGR e mediapipe com RGB
    
    results = Hand.process(imgRGB)  #devolve landmark se é esquerda ou direita e o numero de mãos detectadas
    
    handsPoints = results.multi_hand_landmarks  #extrai os pontos que queremos identificar na imagem da mao
    altura, largura, c = img.shape              #pega a altura e largura da imagem
    dedos = [8, 12, 16, 20]

    if not results.multi_hand_landmarks: 
        cv2.imshow("Imagem", img)    # mostra a imagem na tela
        
        # verifica se janela foi fechada ou ESC
        if cv2.getWindowProperty("Imagem", cv2.WND_PROP_VISIBLE) < 1: # 
           break
        if cv2.waitKey(1) == 27:
            break
        continue
    
    for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness): 
        # hand_landmarks é a posição dos pontos da mão, handedness é se é esquerda ou direita
        
        # desenha os pontos e as conexoes entre eles
        mpdrw.draw_landmarks(img, hand_landmarks, hand.HAND_CONNECTIONS)

        # converte landmarks para coordenadas de pixel
        pontos = [] # lista para armazenar os pontos da mão
        
        for id, cord in enumerate(hand_landmarks.landmark): #id é o numero do ponto e cord é a coordenada x e y
            # O landmark retorna valores entre 0 e 1, entao precisamos multiplicar pela largura e altura da imagem
            cx, cy = int(cord.x * largura), int(cord.y * altura)
            cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
            pontos.append((cx, cy))


        label = handedness.classification[0].label  # label é 'Left' ou 'Right'

        contador = 0
        
        # polegar: depende do lado da mão
        if label == 'Right':
            if pontos[4][0] < pontos[3][0]: #verifica se o polegar direito está levantado
                contador += 1
        else:
            if pontos[4][0] > pontos[3][0]: #verifica se o polegar esquerdo está levantado
                contador += 1

            # demais dedos
        for d in dedos:
            if pontos[d][1] < pontos[d - 2][1]:
                contador += 1

        # desenha um placar próximo ao pulso (landmark 0)
        x0, y0 = pontos[0]
        cv2.rectangle(img, (x0 - 10, y0 - 60), (x0 + 140, y0 - 10), (255, 255, 0), -1)
        texto = f"{label}: {contador}"
        cv2.putText(img, texto, (x0, y0 - 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
      
    cv2.imshow("Imagem", img)

    # fecha se janela foi fechada (clicou no X)
    if cv2.getWindowProperty("Imagem", cv2.WND_PROP_VISIBLE) < 1:
        break

    # fecha também se pressionar ESC
    if cv2.waitKey(1) == 27:
        break
    

video.release()
cv2.destroyAllWindows() #