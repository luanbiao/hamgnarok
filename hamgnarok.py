import cv2
import numpy as np
import pyautogui
import time
import tkinter as tk
from PIL import Image, ImageTk
import pkg_resources
import os

def encontrar_localizacao(screenshot, imagem_recortada):
    resultado = cv2.matchTemplate(screenshot, imagem_recortada, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)
    return max_loc, max_val

def verificar_imagens():
    # Capturar a tela usando pyautogui
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Salvar a captura de tela
    cv2.imwrite('screenshot.png', screenshot)

    # Encontrar a localização da imagem1 na tela
    loc_imagem1, val_imagem1 = encontrar_localizacao(screenshot, imagem1)

    # Encontrar a localização da imagem2 na tela
    loc_imagem2, val_imagem2 = encontrar_localizacao(screenshot, imagem2)

    # Encontrar a localização da imagem3 na tela
    loc_imagem3, val_imagem3 = encontrar_localizacao(screenshot, imagem3)

    # Limpar o texto exibido anteriormente
    texto_resultado.config(text="Aguardando")

    # Verificar se encontrou a imagem1
    if val_imagem1 > 0.8:
        texto_resultado.config(text="Fase 1: Clique para pescar")
        exibir_imagem(os.path.join('player', 'Fase 1 - Clique Para Pescar.png'))
        exibir_coordenadas(loc_imagem1)

    # Verificar se encontrou a imagem2
    if val_imagem2 > 0.8:
        texto_resultado.config(text="Fase 2: Toque para Recolher")
        exibir_imagem(os.path.join('player', 'Fase 2 - Toque para Recolher.png'))
        exibir_coordenadas(loc_imagem2)

    # Verificar se encontrou a imagem3
    if val_imagem3 > 0.8:
        texto_resultado.config(text="Fase 3: Captura de Peixe")
        exibir_imagem(os.path.join('player', 'Fase 3 - Captura de Peixe.png'))
        exibir_coordenadas(loc_imagem3)

    # Atualizar a janela após a busca
    root.update_idletasks()

    # Chamar novamente após 500ms
    root.after(500, verificar_imagens)

def exibir_imagem(nome_arquivo):
    imagem = Image.open(nome_arquivo)
    imagem = imagem.resize((114, 161))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem.config(image=imagem)
    label_imagem.image = imagem

def exibir_coordenadas(loc):
    texto_coordenadas.config(text="x = " + str(loc[0]) + ", y = " + str(loc[1]))

# Criar a janela principal
root = tk.Tk()
root.title("Hamgnarok")
root.iconbitmap("icone.ico")
root.geometry("350x320")

# Carregar as imagens recortadas
imagem1 = cv2.imread(os.path.join('modelos', 'Fase 1.jpg'))
imagem2 = cv2.imread(os.path.join('modelos', 'Fase 2.jpg'))
imagem3 = cv2.imread(os.path.join('modelos', 'Fase 3.jpg'))

# Criar um rótulo para o título "Hamgnarok"
label_titulo = tk.Label(root, text="Hamgnarok", font=("Roboto", 20))
label_titulo.pack()

# Criar um rótulo para exibir a imagem
imagem_padrao = Image.open(os.path.join('player', 'Fase 4 - Standby.png'))
imagem_padrao = imagem_padrao.resize((114, 161))
imagem_padrao = ImageTk.PhotoImage(imagem_padrao)
label_imagem = tk.Label(root, image=imagem_padrao)
label_imagem.pack(pady=10)

# Criar um rótulo para exibir o resultado
texto_resultado = tk.Label(root, text="", justify="left", font=("Roboto", 14, "bold"))
texto_resultado.pack(padx=10, pady=5)

# Criar um rótulo para exibir as coordenadas
texto_coordenadas = tk.Label(root, text="", justify="left", font=("Roboto", 12))
texto_coordenadas.pack(padx=10, pady=5)

# Iniciar a verificação das imagens
verificar_imagens()

# Iniciar o loop principal da interface gráfica
root.mainloop()
