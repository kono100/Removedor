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

print(f"\nSalvo como: {output_filename}\n")








# #  VERSÃO MAIS SIMPLES  #

# from rembg import remove
# from PIL import Image
# INPUT_PATH = 'praia.png'
# OUTPUT_PATH = 'praia(sf).png'
# inp = Image.open(INPUT_PATH)
# output = remove(inp)
# output.save(OUTPUT_PATH)
# print(f"\nSalvo como: {OUTPUT_PATH}\n")

