#s'encarregara de llegir i escriure arxius, a més de validar les dades dels rotors
#funcions: 
#llegir_rotor(ruta), llegir l'arxiu, extreure cablejat i notch
#guardar_rotor(ruta,cablejat,notch), guarda una nova configuracio (per a l'opcio editar rotors)
#validar_permutacio(cablejat), verifica que tingui 26 lletres úniques
#llegir_missatge(ruta), llegeix el missatge original
#guardar_resultat(ruta,text), escriu el resultat a xifrat.txt o a desxifrat.txt

import configuration

def llegir_rotor(rotor):
    try:
        with open(rotor) as file:
            linies = file.readlines()

        if not linies:
            return False
        
        cablejat = linies[0].strip().upper()

        notch = linies[1].strip().upper() if len(linies) > 1 else configuration.NOTCH_INICIAL #constant de configuration

        if validar_permutacio(cablejat) == False:
            return False
        
        else:
        
            return {
            "cablejat" : cablejat,
            "notch" : notch
            }

    except FileNotFoundError:
        print(f"ERROR: L'arxiu {rotor} no s'ha trobat")
        return False
    except Exception as error:
         print(f"ERROR: Error inesperat: {error}")
         return False
    
def guardar_rotor(rotor,cablejat,notch): #S'utilitzaran com a arguments el rotor que es vulgui editar, el cablejat que introdueixi l'usuari, i el notch, que es pot afegir o no
     try:
          cablejat = cablejat.strip().upper()
          notch = notch.strip().upper()
          cablejat_provat = validar_permutacio(cablejat)
          if cablejat_provat == False:
                    print("El cablejat introduït no és correcte")
               return False
          else:
               if notch == "":
                    notch = configuration.NOTCH_INICIAL
               else:
                    pass
               with open(rotor, "w") as file:
                    file.write(cablejat + "\n")
                    file.write(notch)
               return True
     except FileNotFoundError:
          print(f"ERROR: L'arxiu {rotor} no s'ha trobat")
          return False
     except Exception as error:
          print(f"ERROR: Error inesperat: {error}")
          return False


def validar_permutacio(cablejat):
     cablejat = cablejat.strip().upper()
     if cablejat.isalpha() == False:
          print(f"ERROR: La permutació conté caràcters no vàlids")
          return False
     if len(cablejat) != 26:
        print(f"ERROR: La permutació no té el nombre de caràcters requerits (26)")
        return False
     if len(set(cablejat)) != 26:
        print(f"ERROR: Hi ha lletres repetides a la permutació")
        return False
     return True

def llegir_missatge(arxiu):
     try:
          with open(arxiu) as file:
               text_complet = file.read()
          text_complet = text_complet.upper()
          text_final = ""
          for lletra in text_complet:
               if lletra in configuration.ALFABET:
                    text_final += lletra
          return text_final
     except FileNotFoundError:
          print(f"ERROR: L'arxiu {arxiu} no s'ha trobat")
          return False
     except Exception as error:
          print(f"ERROR: Error inesperat: {error}")
          return False

def guardar_resultat(arxiu, text):
     try:
          with open(arxiu, "w") as file:
               file.write(text.strip())
          return True
     except FileNotFoundError:
          print(f"ERROR: L'arxiu {arxiu} no s'ha trobat")
          return False
     except Exception as error:
          print(f"ERROR: Error inesperat: {error}")
          return False