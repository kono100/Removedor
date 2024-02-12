from rembg import remove
from PIL import Image
import os

# IMPORTANDO IMAGEM
img_path = '2pessoas.png'
img = Image.open(img_path)

# REMOVE FUNDO DE IMAGEM
img_without_back = remove(img)

# OBTÉM O NOME DO ARQUIVO SEM A EXTENSÃO
filename, file_extension = os.path.splitext(img_path)

# INICIA O CONTADOR
counter = 1

# CONSTRÓI O NOME DO ARQUIVO COM SUFFIXO NUMERADO
output_filename = f'{filename}(SF).png'
while os.path.exists(output_filename):
    output_filename = f'{filename}(SF{counter}).png'
    counter += 1

# SALVA IMAGEM SEM FUNDO
img_without_back.save(output_filename)
