import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Função para redimensionar imagem usando interpolação por vizinho mais próximo
def vizinho_mais_proximo(image, scale_factor):
    original_height, original_width = image.shape[:2]
    new_height = int(original_height * scale_factor)
    new_width = int(original_width * scale_factor)

    # Criando uma nova imagem com as novas dimensões
    resized_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    # Redimensionando imagem
    for i in range(new_height):
        for j in range(new_width):
            # Encontrando o pixel correspondente na imagem original
            original_x = int(i / scale_factor)
            original_y = int(j / scale_factor)
            resized_image[i, j] = image[original_x, original_y]

    return resized_image

# Função para redimensionar imagem usando interpolação bilinear
def interpolacao_bilinear(image, scale_factor):
    original_height, original_width = image.shape[:2]
    new_height = int(original_height * scale_factor)
    new_width = int(original_width * scale_factor)

    # Criando uma nova imagem com as novas dimensões
    resized_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    # Redimensionando imagem
    for i in range(new_height):
        for j in range(new_width):
            # Coordenadas na imagem original
            x = i / scale_factor
            y = j / scale_factor

            # Coordenadas dos quatro pixels vizinhos
            x1, y1 = int(x), int(y)
            x2, y2 = min(x1 + 1, original_height - 1), min(y1 + 1, original_width - 1)

            # Fatores de interpolação
            r1, r2 = x - x1, y - y1

            # Calculando a cor interpolada
            for c in range(image.shape[2]):
                valor_interpolado = (
                    (1 - r1) * (1 - r2) * image[x1, y1, c] +
                    r1 * (1 - r2) * image[x2, y1, c] +
                    (1 - r1) * r2 * image[x1, y2, c] +
                    r1 * r2 * image[x2, y2, c]
                )
                resized_image[i, j, c] = int(valor_interpolado)

    return resized_image

def main():
    # Abrir um diálogo para selecionar a imagem
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal do Tkinter
    image_path = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")])

    if not image_path:
        print("Nenhuma imagem foi selecionada.")
        return

    # Carregar a imagem selecionada
    image = cv2.imread(image_path)
    if image is None:
        print("Erro ao carregar a imagem.")
        return

    print("Escolha o tipo de procedimento:")
    print("1. Ampliação")
    print("2. Redução")
    choice = int(input("Digite a opção desejada (1 ou 2): "))

    if choice == 1:
        scale_factor = 2.0
    elif choice == 2:
        scale_factor = 0.5
    else:
        print("Opção inválida.")
        return

    print("Aplicando interpolação por Vizinho Mais Próximo...")
    imagem_vizinho = vizinho_mais_proximo(image, scale_factor)
    cv2.imwrite('vizinho_mais_proximo.jpg', imagem_vizinho)
    print("Imagem com Vizinho Mais Próximo salva como 'vizinho_mais_proximo.jpg'")

    print("Aplicando interpolação Bilinear...")
    imagem_bilinear = interpolacao_bilinear(image, scale_factor)
    cv2.imwrite('interpolacao_bilinear.jpg', imagem_bilinear)
    print("Imagem com Interpolação Bilinear salva como 'interpolacao_bilinear.jpg'")

if __name__ == "__main__":
    main()