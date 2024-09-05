import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def vizinho_mais_proximo(image, scale_factor):
    original_height, original_width = image.shape[:2]
    new_height = int(original_height * scale_factor)
    new_width = int(original_width * scale_factor)

    # Criando uma nova imagem com as novas dimensões
    resized_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    for i in range(new_height):
        for j in range(new_width):
            # Encontrando o pixel correspondente na imagem original
            original_x = int(i / scale_factor)
            original_y = int(j / scale_factor)

            # Atribuindo o valor do pixel correspondente
            resized_image[i, j] = image[original_x, original_y]

    return resized_image

def interpolacao_bilinear(image, scale_factor):
    original_height, original_width = image.shape[:2]
    new_height = int(original_height * scale_factor)
    new_width = int(original_width * scale_factor)

    # Criando uma nova imagem com as novas dimensões
    resized_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    for i in range(new_height):
        for j in range(new_width):
            # Coordenadas na imagem original
            x = i / scale_factor
            y = j / scale_factor

            # Coordenadas dos pixels vizinhos
            x1 = int(x)
            y1 = int(y)
            x2 = min(x1 + 1, original_height - 1)
            y2 = min(y1 + 1, original_width - 1)

            # Fatores de interpolação
            r1 = x - x1
            r2 = y - y1

            # Interpolação
            for c in range(image.shape[2]):
                interpolated_value = (
                    (1 - r1) * (1 - r2) * image[x1, y1, c] +
                    (r1) * (1 - r2) * image[x2, y1, c] +
                    (1 - r1) * (r2) * image[x1, y2, c] +
                    (r1) * (r2) * image[x2, y2, c]
                )
                resized_image[i, j, c] = int(interpolated_value)

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
        print("Erro ao carregar a imagem. Verifique o caminho.")
        return

    print("Escolha o tipo de interpolação:")
    print("1. Interpolação por Vizinho Mais Próximo")
    print("2. Interpolação Bilinear")
    choice = int(input("Digite a opção desejada (1 ou 2): "))

    scale_factor = float(input("Digite o fator de escala (Ex: 0.5 para redução, 2.0 para ampliação): "))

    if choice == 1:
        scaled_image = vizinho_mais_proximo(image, scale_factor)
        output_path = 'vizinho_mais_proximo.jpg'
    elif choice == 2:
        scaled_image = interpolacao_bilinear(image, scale_factor)
        output_path = 'interpolacao_bilinear.jpg'
    else:
        print("Opção inválida.")
        return

    # Salvar a imagem resultante
    cv2.imwrite(output_path, scaled_image)
    print(f"A imagem foi salva como {output_path}")

if __name__ == "__main__":
    main()