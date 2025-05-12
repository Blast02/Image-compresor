this is one of my first learning python project in 2022
# Image Compressor 📁➡️📁

Script Python pour compresser et redimensionner des images en masse, avec contrôle de la qualité et du pourcentage de réduction.

## 📝 Description

Ce script permet de :
- Redimensionner des images par un pourcentage personnalisé
- Compresser des images (JPEG, PNG) avec ajustement de la qualité
- Traiter un dossier entier d'images en une seule exécution
- Générer des statistiques de compression pour chaque image

## ✨ Fonctionnalités
- Choix dynamique des dossiers d'entrée/sortie
- Création automatique du dossier de sortie
- Prise en charge des formats JPG/JPEG/PNG
- Feedback visuel des économises réalisées
- Compatibilité Windows/Linux/macOS

## ⚙️ Prérequis
- Python 3.x installé
- Bibliothèque Pillow installée

## 🔧 Installation
1. Installer Pillow :
```bash
pip install Pillow
```
🚀 Utilisation
Exécutez le script et suivez les instructions :

```bash
python compress_images.py
```
Paramètres demandés :

Chemin du dossier source (ex: D:/photos/raw)

Chemin du dossier de sortie (ex: D:/photos/compressed)

Pourcentage de réduction de taille (0-100)

Niveau de qualité (1-95)

⚠️ Notes importantes
Les images sont écrasées si elles portent le même nom dans le dossier de sortie

Qualité > 90 : compression quasi invisible

Qualité < 70 : artefacts possibles

Utilisez des chemins avec / pour éviter les erreurs

📄 License
MIT License - Libre d'utilisation et modification
