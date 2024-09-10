from pdf2image import convert_from_path
from PIL import Image
import os

# Função para converter PDF em imagens e salvar como .webp
def pdf_to_webp(pdf_path, output_folder):
    # Converter o PDF em uma lista de imagens
    images = convert_from_path(pdf_path, poppler_path='./third/poppler/poppler-24.07.0/Library/bin')

    # Criar pasta de saída, se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Para cada imagem (página do PDF)
    for i, image in enumerate(images):
        # Nome do arquivo de saída
        output_file = os.path.join(output_folder, f"page_{i+1}.webp")
        # Converter e salvar como webp
        image.save(output_file, 'WEBP')

    print(f"Todas as páginas foram convertidas e salvas em {output_folder}")

# Insira o caminho do arquivo PDF
pdf_path = './input/teste.pdf'
# Insira a pasta onde quer salvar os arquivos webp
output_folder = './output'

pdf_to_webp(pdf_path, output_folder)
