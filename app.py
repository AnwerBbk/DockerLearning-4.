
from pathlib import Path

fichier = Path("/data/stock.txt")

total_stock = 0

print("=== Gestion de Stock ===")

for ligne in fichier.read_text(encoding="utf-8").splitlines():
    nom, quantite, prix = ligne.split(",")

    quantite = int(quantite)
    prix = float(prix)

    valeur = quantite * prix
    total_stock += valeur

    
quantite = -5

if quantite < 0:
    print("Erreur : quantite negative interdite")
else:
    print("Quantite valide")


    print(f"Produit : {nom}")
    print(f"Quantite : {quantite}")
    print(f"Prix unitaire : {prix:.2f} DT")
    print(f"Valeur : {valeur:.2f} DT")
    print("----------------------")

print(f"Valeur totale du stock : {total_stock:.2f} DT")
