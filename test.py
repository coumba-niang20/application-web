import csv
import json
import ast

def convertir_csv_en_json():
    liste_donnees = []
    
    with open('backend/data/eleves_valides.csv', mode='r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv)
        
        for ligne in lecteur_csv:
            nouveau_eleve = {}
            
            for cle, valeur in ligne.items():
                if cle == 'Note':
                    # Convertir la colonne Note en structure JSON
                    try:
                        nouveau_eleve['notes'] = ast.literal_eval(valeur)
                    except:
                        nouveau_eleve['notes'] = []
                        print(f"Erreur pour {ligne.get('CODE', 'inconnu')}")
                else:
                    nouveau_eleve[cle] = valeur
            
            liste_donnees.append(nouveau_eleve)
    
    # Sauvegarder en JSON
    with open('backend/data/eleves_valides.json', mode='w', encoding='utf-8') as fichier_json:
        json.dump(liste_donnees, fichier_json, indent=4, ensure_ascii=False)
    
    print(f"Conversion terminée ! {len(liste_donnees)} élèves convertis.")

if __name__ == "__main__":
    convertir_csv_en_json()

