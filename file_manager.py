#s'encarregara de llegir i escriure arxius, a més de validar les dades dels rotors
#funcions: 
#llegir_rotor(ruta), llegir l'arxiu, extreure cablejat i notch
#guardar_rotor(ruta,cablejat,notch), guarda una nova configuracio (per a l'opcio editar rotors)
#validar_permutacio(cablejat), verifica que tingui 26 lletres úniques
#llegir_missatge(ruta), llegeix el missatge original
#guardar_resultat(ruta,text), escriu el resultat a xifrat.txt o a desxifrat.txt

def llegir_rotor(rotor):
    try:
        with open(rotor) as file:
            linies = file.readlines()

        if not linies:
            return None
        
        cablejat = linies[0].strip().upper()

        notch = linies[1].strip().upper() if len(linies) > 1 else "Z"

        if validar_permutacio(cablejat) == False:
            raise ValueError("El cablejat no és correcte")
        
        else:
        
            return {
            "cablejat" : cablejat,
            "notch" : notch
            }

    except FileNotFoundError:
        print("ERROR: L'arxiu no s'ha trobat")
        return None
    except ValueError as error:
         print(f"ERROR: {error}")
         return None
    except Exception as error:
         print(f"ERROR: error inesperat, {error}")
         return None
    

def guardar_rotor(rotor,cablejat,notch): #S'utilitzaran com a arguments el rotor que es vulgui editar, el cablejat que introdueixi l'usuari, i el notch, que es pot afegir o no
    cablejat = cablejat.strip().upper()
    notch = notch.strip().upper()
    cablejat_provat = validar_permutacio(cablejat)
    if cablejat_provat == False:
         return False
    else:
         if notch == "":
            notch = "Z"
         else:
              pass
         with open(rotor, "w") as file:
              file.write(cablejat_provat + "\n")
              file.write(notch)
    #FALTA AFEGIR ELS TRY EXCEPT I POSSIBLES ERRORS

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
     with open(arxiu) as file:
         text = file.readlines()

def guardar_resultat(arxiu_xifrat,text_xifrat):
     with open(arxiu_xifrat, "w") as file:
        text_xifrat.strip()
        file.write(text_xifrat)