#Visitantes en Chile
visitantes = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
            "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
            "012": ["Julian Martinez", "Argentina", "19-09-2023"],
            "014": ["Agustin Morales", "Argentina", "28-03-2024"],
            "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
            "006": ["Maria Lopez", "Mexico", "08-12-2023"],
            "007": ["Joao Silva", "Brasil", "20-06-2024"],
	        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
            "008": ["Ana Santos", "Brasil", "03-10-2023"],
            "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
            "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
        }
opcion={("MENU PRINCIPAL",
        "1.- Turistas por pais.",
    "2.- Turista por mes.",
    "3.- Eliminar turista.",
    "4.- Salir.")}

#
#Visitantes por pais
def visitantes_por_pais(pais):
    cantidad=0
    for elemento in visitantes.values():
        if elemento[1].upper()==str(pais).upper():
            print(f"Nombre: {elemento[0]}")
            cantidad+1
    return cantidad
#
#Meses del año y pais
def visitantes_por_mes(mes,pais):
    contador_visitamte=0
    for datos_visitantes in visitantes.values():
        fecha=datos_visitantes[2]
        mes_fecha=fecha[3:5]
#
        print(int(mes_fecha))
        if int(mes_fecha)==int(mes) and datos_visitantes[1].upper()==pais.upper():
            contador_visitante+=1
            print(contador_visitante)
    porcentaje= (contador_visitamte/len(visitantes))*100
    return round(porcentaje,1)
#
#Mes de visita
visitantes_por_pais("mexico")
while True:
    mes=int(input("Ingrese el mes de visita de los visitantes(1-12): "))
    if mes<=0 or mes>12:
        print("Debe ingresar un mes entre 1-12")
        continue
    pais=input("Ingrese el pais de origen del visitante: ")
#
    porcentaje=visitantes_por_mes(mes,pais)
    print(f"El porcentaje de visitantes que visitaron chile y vienen de {pais} es de {porcentaje}%")
    break
#