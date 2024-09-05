# Image-Resizer

**Image-Resizer** é uma ferramenta simples para redimensionar imagens usando duas técnicas de interpolação: vizinho mais próximo e interpolação bilinear. Esta ferramenta suporta tanto ampliação quanto redução de imagens.

## Funcionalidades

- Redimensionamento de imagens usando interpolação por vizinho mais próximo
- Redimensionamento de imagens usando interpolação bilinear
- Suporte para ampliação e redução de imagens
- Interface gráfica para seleção de arquivos

## Tecnologias Utilizadas

- Python
- OpenCV (`cv2`)
- NumPy
- Tkinter

## Como Usar

1. Clone este repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/seu-usuario/Image-Resizer.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd Image-Resizer
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install opencv-python numpy
    ```

4. Execute o script:

    ```bash
    python image_resizer.py
    ```

5. Selecione a imagem que deseja redimensionar e escolha o tipo de interpolação desejado (vizinho mais próximo ou bilinear). Digite o fator de escala (ex.: 0.5 para reduzir pela metade ou 2.0 para dobrar o tamanho).

## Exemplo de Uso

Escolha o tipo de interpolação:

1. Interpolação por Vizinho Mais Próximo
2. Interpolação Bilinear Digite a opção desejada (1 ou 2): 1 Digite o fator de escala (Ex: 0.5 para redução, 2.0 para ampliação): 1.5
