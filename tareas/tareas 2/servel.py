
import csv

used_file = "data.csv"

def import_data():

    votes = [] # lista con los diccionarios
    file_input = input("Ingrese archivo: ")

    data = open(file_input, "r")
    titles = open(file_input, "r").readlines()[0].split(";")

    lines = data.readlines()[1:]
    # print(lines)
    # print(titles)

    for line in lines:
        line = line.split(";")
        vote = {}
        for i in range(len(titles)):

            vote[titles[i]] = line[i]

        votes.append(vote)

    return votes


### PRIMER PUNTO ###

votes_list = import_data() 



def export_tables_by_region(votes, used):


    
    with open("mesas.csv", "w", newline='') as file:
        writer = csv.writer(file)

        
        tarapaca = []
        antofagasta = []
        atacama = []
        coquimbo = []
        valparaiso = []
        higgins = []
        maule = []
        biobio = []
        araucania = []
        lagos = []
        aysen = []
        magallanes = []
        metropolitana = []
        rios = []
        arica = []
        nuble = []


        datos = []
        for i in votes:
            section = []
            if i['RegiÃ³n'] not in section and i['Local'] not in section: # mi pc traduce "Región" a "RegiÃ³n", tal vez haya que cambiarlo
                section.append(i['RegiÃ³n'])
                section.append(i['Local'])

            section.append(i['Nro. Mesa'])

            
            if section not in datos:
                datos.append(section)
                if section[0] == "DE TARAPACA":
                    tarapaca.append(section[0])
                elif section[0] == "DE ANTOFAGASTA":
                    antofagasta.append(section[0])
                elif section[0] == "DE ATACAMA":
                    atacama.append(section[0])
                elif section[0] == "DE COQUIMBO":
                    coquimbo.append(section[0])
                elif section[0] == "DE VALPARAISO":
                    valparaiso.append(section[0])
                elif section[0] == "DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS":
                    higgins.append(section[0])
                elif section[0] == "DEL MAULE":
                    maule.append(section[0])
                elif section[0] == "DEL BIOBIO":
                    biobio.append(section[0])
                elif section[0] == "DE LA ARAUCANIA":
                    araucania.append(section[0])
                elif section[0] == "DE LOS LAGOS":
                    lagos.append(section[0])
                elif section[0] == "DE AYSEN DEL GENERAL CARLOS IBAÃ‘EZ DEL CAMPO" or section[0] == "DE AYSEN DEL GENERAL CARLOS IBAÑEZ DEL CAMPO":
                    aysen.append(section[0])
                elif section[0] == "DE MAGALLANES Y DE LA ANTARTICA CHILENA":
                    magallanes.append(section[0])
                elif section[0] == "METROPOLITANA DE SANTIAGO":
                    metropolitana.append(section[0])
                elif section[0] == "DE LOS RIOS":
                    rios.append(section[0])
                elif section[0] == "DE ARICA Y PARINACOTA":
                    arica.append(section[0])
                elif section[0] == "DE ÑUBLE" or section[0] == "DE Ã‘UBLE":
                    nuble.append(section[0])

        regiones = [tarapaca, antofagasta, atacama,coquimbo,valparaiso,higgins,maule,biobio,araucania,lagos,aysen,magallanes,metropolitana,rios,arica,nuble]
        keys = ["DE TARAPACA", "DE ANTOFAGASTA", "DE ATACAMA", "DE COQUIMBO", "DE VALPARAISO", "DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS", "DEL MAULE", "DEL BIOBIO", "DE LA ARAUCANIA", "DE LOS LAGOS", "DE AYSEN DEL GENERAL CARLOS IBAÑEZ DEL CAMPO", "DE MAGALLANES Y DE LA ANTARTICA CHILENA", "METROPOLITANA DE SANTIAGO", "DE LOS RIOS", "DE ARICA Y PARINACOTA", "DE ÑUBLE"]
        values = [len(region) for region in regiones]
        writer.writerow(keys)
        writer.writerow(values)
        

    

### SEGUNDO PUNTO ###

# export_tables_by_region(votes_list, used_file)



def export_general_results(data, filename):

    with open("candidatos.csv", "w", newline='') as file:
        writer = csv.writer(file)
    
        kast = []
        boric = []
        nulo = []
        blanco = []
        for i in data:
            if i["Candidato"] == "JOSE ANTONIO KAST RIST":
                kast.append(int(i["Votos TRICEL\n"]))
            elif i["Candidato"] == "GABRIEL BORIC FONT":
                boric.append(int(i["Votos TRICEL\n"]))
            elif i["Candidato"] == "VOTOS NULOS":
                nulo.append(int(i["Votos TRICEL\n"]))
            elif i["Candidato"] == "VOTOS EN BLANCO":
                blanco.append(int(i["Votos TRICEL\n"]))

        writer.writerow(["BORIC", "KAST", "NULOS", "BLANCOS"])
        writer.writerow([sum(boric), sum(kast), sum(nulo), sum(blanco)])
    

### TERCER PUNTO ###

export_general_results(votes_list, used_file)


def export_count_by_local(data, filename):

    local = input("Ingrese un local de votación: ")

    kast = []
    boric = []
    nulo = []
    blanco = []


    for i in data:
        if i["Local"] == local:
            if i["Candidato"] == "GABRIEL BORIC FONT":
                boric.append(int(i["Votos TRICEL\n"]))
            elif i["Candidato"] == "JOSE ANTONIO KAST RIST":
                kast.append(int(i["Votos TRICEL\n"]))
            elif i["Candidato"] == "VOTOS NULOS":
                nulo.append(int(i["Votos TRICEL\n"]))
            elif i["Candidato"] == "VOTOS EN BLANCO":
                blanco.append(int(i["Votos TRICEL\n"]))

    print("Boric:", sum(boric))
    print("Kast:", sum(kast))
    print("Nulos:", sum(nulo))
    print("Blancos:", sum(blanco))




### CUARTO PUNTO ###

export_count_by_local(votes_list, used_file)