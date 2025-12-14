import os
import sys
import configuration
import file_manager
import enigma_machine


def netejar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def carregar_rotors():

    r1 = file_manager.llegir_rotor(configuration.ROTOR1)
    r2 = file_manager.llegir_rotor(configuration.ROTOR2)
    r3 = file_manager.llegir_rotor(configuration.ROTOR3)

    if not r1 or not r2 or not r3:
        print("[ERROR] No s'han pogut carregar tots els rotors.")
        return None

    print(f"[OK] Rotors carregats correctament: {configuration.ROTOR1}, {configuration.ROTOR2}, {configuration.ROTOR3}")
    return [r1, r2, r3]

def demanar_posicio_inicial():
    while True:
        entrada = input("Introdueix la posició inicial dels rotors (ex: A B C): ").upper().replace(" ", "")
        if len(entrada) == 3 and entrada.isalpha():
            return [entrada[0], entrada[1], entrada[2]]
        print("[ERROR] Has d'introduir exactament 3 lletres vàlides (A-Z).")

def processar_missatge(mode):
    rotors_data = carregar_rotors()
    if not rotors_data:
        return

    cablejats = [r['cablejat'] for r in rotors_data]
    notches = [r['notch'] for r in rotors_data]

    posicions = demanar_posicio_inicial()

    if mode == 'xifrar':
        arxiu_entrada = configuration.TEXT_ORIGINAL
        arxiu_sortida = configuration.TEXT_XIFRAT
        print(f"Llegint missatge original de {arxiu_entrada}...")
    else:
        arxiu_entrada = configuration.TEXT_XIFRAT
        arxiu_sortida = configuration.TEXT_DESXIFRAT
        print(f"Llegint missatge xifrat de {arxiu_entrada}...")

    text_entrada = file_manager.llegir_missatge(arxiu_entrada)

    if text_entrada is False:
        return

    resultat = ""

    for lletra in text_entrada:
        if mode == 'xifrar':
            lletra_transformada = enigma_machine.xifrar_lletra(lletra, cablejats, posicions)
        else:
            lletra_transformada = enigma_machine.desxifrar_lletra(lletra, cablejats, posicions)
            
        resultat += lletra_transformada

    if mode == 'xifrar':
        text_final = enigma_machine.formatejar_sortida(resultat)
    else:
        text_final = resultat

    if file_manager.guardar_resultat(arxiu_sortida, text_final):
        print(f"\n[OK] Procés finalitzat. Resultat guardat a '{arxiu_sortida}'.")
        print(f"Resultat parcial: {text_final[:20]}...")
    else:
        print("[ERROR] No s'ha pogut guardar l'arxiu.")
        
    input("\nPrem ENTER per tornar al menú...")

    def editar_rotor():
        print("\n--- EDITAR ROTORS ---")
        print(f"1. {configuration.ROTOR1}")
        print(f"2. {configuration.ROTOR2}")
        print(f"3. {configuration.ROTOR3}")
        opcio = input("Escull quin rotor vols editar (1-3): ")
        mapa_rotors = {'1': configuration.ROTOR1, '2': configuration.ROTOR2, '3': configuration.ROTOR3}
    
        if opcio not in mapa_rotors:
            print("[ERROR] Opció incorrecta.")
            return

        ruta_rotor = mapa_rotors[opcio]
        print(f"Editant {ruta_rotor}...")
    
        nou_cablejat = input("Introdueix la nova permutació (26 lletres úniques): ").upper()
        nou_notch = input("Introdueix el notch (lletra) [Buit per defecte 'Z']: ").upper()
    
        if file_manager.guardar_rotor(ruta_rotor, nou_cablejat, nou_notch):
            print(f"[OK] {ruta_rotor} actualitzat correctament.")
    
        input("\nPrem ENTER per tornar al menú...")

def main():
    while True:
        netejar_pantalla()
        print("************************************")
        print("      MÀQUINA ENIGMA - SIMULADOR    ")
        print("************************************")
        print("1. Xifrar missatge")
        print("2. Desxifrar missatge")
        print("3. Editar rotors")
        print("4. Sortir")
        
        opcio = input("\nSelecciona una opció: ")

        if opcio == '1':
            processar_missatge('xifrar')
        elif opcio == '2':
            processar_missatge('desxifrar')
        elif opcio == '3':
            editar_rotor()
        elif opcio == '4':
            print("Sortint del simulador...")
            sys.exit()
        else:
            input("[ERROR] Opció no vàlida. Prem ENTER per continuar.")

if __name__ == "__main__":
    main()