#limpiar_texto(texto): Convierte a mayúsculas y elimina todo lo que no sea A-Z (acentos, espacios, números).

#avanzar_rotores(posiciones, notches): Implementa la lógica de "odómetro". Gira el rotor 1; si toca su notch, gira el 2; si el 2 toca su notch, gira el 3.

#cifrar_letra(letra, rotores, posiciones): Pasa una letra a través de los 3 rotores en sentido directo (R1 -> R2 -> R3).

#descifrar_letra(letra, rotores, posiciones): Pasa una letra a través de los 3 rotores en sentido inverso (R3 -> R2 -> R1) usando el cableado inverso.


#formatear_salida(texto_cifrado): Agrupa el texto en bloques de 5 letras separados por espacios.
import configuration

def formatejar_entrada(text):

def avançar_rotors(posicions, notches):
    p1, p2, p3 = posicions
    n1, n2, n3 = notches
    moure_rotor1 = True
    moure_rotor2 = False
    moure_rotor3 = False
    if p1 == n1:
        moure_rotor2 = True
    if p2 == n2 and moure_rotor2:
        moure_rotor3 = True

    final1 = moviment(p1)
    if moure_rotor2:
        final2 = moviment(p2)
    else:
        final2 = p2
    if moure_rotor3:
        final3 = moviment(p3)
    else:
        final3 = p3

    return [final1, final2, final3]

def xifrar_lletra(lletra,rotors,posicions):
    index_actual = a_index(lletra)
    cab1, cab2, cab3 = rotors
    p1, p2, p3 = posicions
    index_actual = passar_rotor(index_actual, cab1, p1)
    index_actual = passar_rotor(index_actual, cab2, p2)
    index_actual = passar_rotor(index_actual, cab3, p3)

    return a_lletra(index_actual)

def passar_rotor(index_entrada, rotor, posicio):
    canvi = a_index(posicio)
    
    index_ajustat = (index_entrada + canvi) % 26
    
    lletra_sortida = rotor[index_ajustat]
    index_transformat = a_index(lletra_sortida)
    
    index_final = (index_transformat - canvi) % 26
    
    return index_final
    

def desxifrar_lletra(lletra,rotors,posicions):
    index_actual = a_index(lletra)

    cab1, cab2, cab3 = rotors
    pos1, pos2, pos3 = posicions

    index_actual = passar_pel_rotor_invers(index_actual, cab3, pos3)
    index_actual = passar_pel_rotor_invers(index_actual, cab2, pos2)
    index_actual = passar_pel_rotor_invers(index_actual, cab1, pos1)

    return a_lletra(index_actual)
    

def passar_pel_rotor_invers(index_entrada, rotor, posicio_rotor):
    canvi = a_index(posicio_rotor)

    index_ajustat = (index_entrada + canvi) % 26
    lletra_a_buscar = a_lletra(index_ajustat)

    index_trobat = rotor.index(lletra_a_buscar)
    index_final = (index_trobat - canvi) % 26

    return index_final


def formatejar_sortida(text):
    resultat = []

    for i in range(0, len(text), configuration.AGRUPACIÓ):
        grup = text[i:i + mida]
        resultat.append(grup)

    return " ".join(resultat)


def a_lletra(index):
    return configuration.ALFABET[index % 26]

def a_index(lletra):
    return configuration.ALFABET.index(lletra)

def moviment(posicio):
    posicio_en_index = a_index(posicio)
    posicio_en_index += 1
    return a_lletra(posicio_en_index)

