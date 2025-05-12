from PIL import Image
import os

def compress_image(input_path, output_path, percent=100, quality=95):
    with Image.open(input_path) as img:

        width, height = img.size
        img = img.resize((int(width*percent/100), int(height*percent/100)))


        img.save(output_path, optimize=True, quality=quality)


    input_size = os.path.getsize(input_path)
    output_size = os.path.getsize(output_path)
    percent = round(100 * (input_size - output_size) / input_size, 2)
    print(f"L'image {input_path} a désormais une taille de {output_size/1000} ko contre {input_size/1000} ko avant")


input_dir = input("Entrez le chemin du dossier d'entrée (ex: D:/photo/document) : ")
output_dir = input("Entrez le chemin du dossier de sortie (ex: D:/photo/document/test) : ")


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


percent = int(input("Entrez le pourcentage de réduction de taille (0-100) : "))
quality = int(input("Entrez le niveau de qualité de compression (1-95) : "))


for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        # Chemin complet du fichier d'entrée
        input_path = os.path.join(input_dir, filename)

        # Chemin complet du fichier de sortie
        output_path = os.path.join(output_dir, filename)

        # Appliquer la fonction de compression à l'image
        compress_image(input_path, output_path, percent=percent, quality=quality)