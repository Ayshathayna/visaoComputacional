# 🖐️ Detecção e Contagem de Dedos com OpenCV e MediaPipe

Este projeto demonstra a utilização das bibliotecas **OpenCV** para captura e exibição de vídeo e **MediaPipe Hands** para rastreamento de landmarks de mãos. A aplicação detecta até duas mãos em tempo real e calcula quantos dedos estão levantados, exibindo o resultado na tela.

## 🛠️ Tecnologias

* **Python** (Versão 3.10 ou superior)
* **OpenCV** (`cv2`): Para captura de vídeo e exibição gráfica.
* **MediaPipe**: Para detecção e rastreamento de landmarks (pontos-chave) das mãos.

## Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter o Python 3.10 ou superior instalado. Você também precisará das bibliotecas de runtime do Visual C++ para o MediaPipe funcionar no Windows.

### 2. Instalação das Dependências

Abra o terminal na pasta do projeto e instale as bibliotecas necessárias:

```bash
pip install mediapipe opencv-python
```

### 3. Execução
Execute o script principal (visao.py):

```bash
python visao.py
```
Para encerrar a aplicação, pressione a tecla ESC.

## ✨ Funcionalidades

* Rastreamento de mão em tempo real com 21 landmarks por mão.
* Desenho automático dos landmarks e das conexões (esqueleto da mão).
* Lógica para contar o número de dedos levantados (baseada na posição dos pontos 8, 12, 16, 20 e 4).
* Exibição do contador de dedos em um retângulo na tela.


