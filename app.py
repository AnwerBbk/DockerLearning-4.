from pathlib import Path

fichier = Path("/data/stock.txt")

print("=== Gestion de Stock ===")

for ligne in fichier.read_text().splitlines():
    print(ligne)