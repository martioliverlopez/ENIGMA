import configuration

#La funció gestiona la llogica d'odómetre a l'hora d'avançar els rotors
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


#La funció serveix per a xifrar el text lletra a lletra
def xifrar_lletra(lletra,rotors,posicions):
    index_actual = a_index(lletra)
    cab1, cab2, cab3 = rotors
    p1, p2, p3 = posicions
    index_actual = passar_rotor(index_actual, cab1, p1)
    index_actual = passar_rotor(index_actual, cab2, p2)
    index_actual = passar_rotor(index_actual, cab3, p3)

    return a_lletra(index_actual)

#La funció serveix per al xifratge, per a fer la transacció d'entrada/sortida entre els rotors
def passar_rotor(index_entrada, rotor, posicio):
    canvi = a_index(posicio)
    
    index_ajustat = (index_entrada + canvi) % 26
    
    lletra_sortida = rotor[index_ajustat]
    index_transformat = a_index(lletra_sortida)
    
    index_final = (index_transformat - canvi) % 26
    
    return index_final
    
#La funció serveix per a desxifrar el text lletra a lletra
def desxifrar_lletra(lletra,rotors,posicions):
    index_actual = a_index(lletra)

    cab1, cab2, cab3 = rotors
    pos1, pos2, pos3 = posicions

    index_actual = passar_pel_rotor_invers(index_actual, cab3, pos3)
    index_actual = passar_pel_rotor_invers(index_actual, cab2, pos2)
    index_actual = passar_pel_rotor_invers(index_actual, cab1, pos1)

    return a_lletra(index_actual)
    
#La funció serveix per al desxifratge, per a fer la transacció d'entrada/sortida entre els rotors
def passar_pel_rotor_invers(index_entrada, rotor, posicio_rotor):
    canvi = a_index(posicio_rotor)

    index_ajustat = (index_entrada + canvi) % 26
    lletra_a_buscar = a_lletra(index_ajustat)

    index_trobat = rotor.index(lletra_a_buscar)
    index_final = (index_trobat - canvi) % 26

    return index_final

#La funció serveix per a agrupar el text resultant en grups de 5
def formatejar_sortida(text):
    mida = configuration.AGRUPACIÓ
    resultat = []

    for i in range(0, len(text), mida):
        grup = text[i:i + mida]
        resultat.append(grup)

    return " ".join(resultat)

#La funció serveix per a obtenir la lletra de l'alfabet a partir de l'index 
def a_lletra(index):
    return configuration.ALFABET[index % 26]

#La funció serveix per a obtenir l'index de l'alfabet a partir de la lletra
def a_index(lletra):
    return configuration.ALFABET.index(lletra)

#La funció serveix per a augmentar en 1 la posicio del rotor
def moviment(posicio):
    posicio_en_index = a_index(posicio)
    posicio_en_index += 1
    return a_lletra(posicio_en_index)

