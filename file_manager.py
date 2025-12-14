import configuration

#La funció llegeix l'arxiu, extreu cablejat i notch
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
    
#La funció guarda una nova configuracio (per a l'opcio editar rotors)
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

#La funció verifica que tingui 26 lletres úniques
def validar_permutacio(cablejat):
     cablejat = cablejat.strip().upper()

     for lletra in cablejat:
          if lletra not in configuration.ALFABET:
               print(f"ERROR: La permutació conté caràcters no vàlids")
               return False
          
     if len(cablejat) != 26:
        print(f"ERROR: La permutació no té el nombre de caràcters requerits (26)")
        return False
     
     if len(set(cablejat)) != 26:
        print(f"ERROR: Hi ha lletres repetides a la permutació")
        return False
     return True

#La funció llegeix el missatge original
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
     
#La funció escriu el resultat a xifrat.txt o a desxifrat.txt
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