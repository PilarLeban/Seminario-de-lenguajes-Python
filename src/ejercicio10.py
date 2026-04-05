def calculoPuntaje(punt, n, jurados):
    total = 0
    for j in jurados:
        total += punt[n][j]
    return total

def imprimoResultadosPorRonda(rtos):
    auxiliar = ""
    puesto = 1
    for r in rtos:
        auxiliar += (f"   {puesto}: {r[0]} ({r[1]} pts) \n")
        puesto += 1
    return auxiliar

def definoTablaAcumuladora():
    tablaAcumuladora = [{'Cocinero': 'Valentina', 'Puntaje total': 0, 'Rondas ganadas':
                        0, 'Mejor ronda': 0, 'Promedio': 0},
                        {'Cocinero': 'Mateo', 'Puntaje total': 0, 'Rondas ganadas':
                        0, 'Mejor ronda': 0, 'Promedio': 0},
                        {'Cocinero': 'Camila', 'Puntaje total': 0, 'Rondas ganadas':
                        0, 'Mejor ronda': 0, 'Promedio': 0},
                        {'Cocinero': 'Santiago', 'Puntaje total': 0, 'Rondas ganadas':
                        0, 'Mejor ronda': 0, 'Promedio': 0},
                        {'Cocinero': 'Lucía', 'Puntaje total': 0, 'Rondas ganadas':
                        0, 'Mejor ronda': 0, 'Promedio': 0}]
    return tablaAcumuladora

def acumuloPuntaje(tablaAcumuladora, n, puntajePorRonda):
    for i in tablaAcumuladora:
        if (i['Cocinero'] == n):
            i['Puntaje total'] += puntajePorRonda
            if (puntajePorRonda > i['Mejor ronda']):
                i['Mejor ronda'] = puntajePorRonda
    return tablaAcumuladora

def acumuloRondaGanadaYCalculoPromedio(tablaAcumuladora, ganador, numeroRonda):
    for i in tablaAcumuladora:
        if (i['Cocinero'] == ganador):   
            i['Rondas ganadas'] += 1
        i['Promedio']= i['Puntaje total']/numeroRonda
    return tablaAcumuladora

def imprimoTabla(tablaAcumuladora):
    tablaAcumuladora.sort(key = lambda x: x['Puntaje total'], reverse = True)
    print("Cocinero | Puntaje total | Rondas ganadas | Mejor ronda | Promedio")
    print("-" * 66)
    for c in tablaAcumuladora:
        print(c['Cocinero'],   "    |  ", c['Puntaje total'], "     |   ", c['Rondas ganadas'],
               "     |      ", c['Mejor ronda'], "      |      ", round(c['Promedio'], 2))
        
def devuelvoTabla(rounds, nombres, jurados):
    i = 1
    tablaAcumuladora = definoTablaAcumuladora()
    for aux in rounds:
        tema = aux['theme']
        punt = aux['scores']
        print()
        print()
        print(f"Ronda: {i} - {tema}")
        resultadosPorRonda = []

        for n in nombres:
            puntajePorRonda = calculoPuntaje(punt, n, jurados)
            resultadosPorRonda.append([n, puntajePorRonda])#  --> [['Valentina'][24], ['Camila'][26]]
            tablaAcumuladora = acumuloPuntaje(tablaAcumuladora, n, puntajePorRonda)    

        resultadosPorRonda.sort(key = lambda x: x[1], reverse = True) 
        ganador = resultadosPorRonda[0][0]
        print(f"   Ganador: {ganador} ({resultadosPorRonda[0][1]} pts) ")
        print(imprimoResultadosPorRonda(resultadosPorRonda))
        
        tablaAcumuladora = acumuloRondaGanadaYCalculoPromedio(tablaAcumuladora, ganador, i)
        if (i == len(rounds)):
            print("Tabla de posiciones final: ")

        imprimoTabla(tablaAcumuladora)
        
        input(f"Fin de ronda {i}. Tocá Enter para seguir con la siguiente ronda.")
        i += 1
    return tablaAcumuladora
    

