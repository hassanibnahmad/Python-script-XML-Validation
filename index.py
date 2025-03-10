import xml.etree.ElementTree as ET
# : Le module xml.etree.ElementTree fournit une interface simple pour créer et parcourir les arbres XML.

def check_xml_syntax(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot() 
        # : tree.getroot() est l'élément racine de l'arbre XML, getroot() retourne l'élément racine de l'arbre XML.
        print("✅ Le fichier XML est bien formé.")
    except ET.ParseError as e:
        print("❌ Erreur de syntaxe dans le fichier XML:", e)

# Vérification du fichier XML
xml_file = "Python_script/exemple.xml"  # Chemin du fichier XML

check_xml_syntax(xml_file) # Appel de la fonction check_xml_syntax()
